import argparse
from message import Message
from users import Users
from local_settings import connect_to_db
from pass_hash import *
import datetime


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",  dest="username", default=False,
                        help="User login")
    parser.add_argument("-p", "--password", dest="password", default=False,
                        help="User password")
    parser.add_argument("-t", "--to", dest="to_emeil", default=False,
                        help="Receiver message")
    parser.add_argument("-l", "--list", action="store_true", dest="list", default=False,
                        help="Display all users")
    parser.add_argument("-d", "--delete", action="store_true", dest="delete", default=False,
                        help="Delete user")
    parser.add_argument("-s", "--send", dest="send", default=False,
                        help="Text message")

    options = parser.parse_args()
    return options


def solution(options):
    con = connect_to_db('warsztat1')
    cursor = con.cursor()
    users_tab = {}
    users = Users.load_all_users(cursor)
    for user in users:
        users_tab[user.email] = (user.id, user.username, user.hashed_password)
    if options.username and options.password:
        if options.list:
            check_emeil = input('Podaj emeil: ')
            if check_emeil in users_tab:
                for k, v in users_tab.items():
                    if k == check_emeil:
                        user_id = v[0]
                        print(user_id)
                user = Users.load_user_by_id(cursor, user_id)
                print(user.id, user.username, user.hashed_password)
                print(options.username, user.email)
                if user.username == options.username and check_password(options.password, user.hashed_password):
                    messages = Message.load_all_message_for_user(cursor, user.id)
                    for message in messages:
                        print('Wiadomości do ' + options.username + ': ' + message.text_message +
                            ', ' + str(message.create_date)+', od '+str(message.from_user))
                else:
                    print('niepoprawne dane')
            else:
                print('nie ma takiego użytkownika')
        if options.to_emeil and options.send:
            check_receiver = int(options.to_emeil)
            id_tab = []
            for values in users_tab.values():
                id_tab.append(values[0])
            id_tab = tuple(id_tab)
            if check_receiver in id_tab:
                check_emeil = input('Podaj emeil: ')
                if check_emeil in users_tab:
                    for k, v in users_tab.items():
                        if k == check_emeil:
                            user_id = v[0]
                    user = Users.load_user_by_id(cursor, user_id)
                    if user.username == options.username and check_password(options.password, user.hashed_password):
                        message = Message()
                        message.from_user = user.id
                        message.to_user = options.to_emeil
                        message.text_message = options.send
                        now = datetime.datetime.now()
                        now = now.strftime('%Y-%m-%d')
                        message.create_date = now
                        message.save_to_db(cursor)
                        print('Komunikat wysłany')
                    else:
                        print('Podałeś niepoprawny emeil')
            else:
                print('nie ma takiego odbiorcy')
    cursor.close()
    con.close()


if __name__ == "__main__":
    solution(set_options())
