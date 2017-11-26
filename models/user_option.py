import argparse
from users import Users
from local_settings import connect_to_db
from pass_hash import *


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",  dest="username", default=False,
                        help="User login")
    parser.add_argument("-p", "--password", dest="password", default=False,
                        help="User password")
    parser.add_argument("-n", "--new-pass", dest="newpass", default=False,
                        help="New password")
    parser.add_argument("-l", "--list", action="store_true", dest="list", default=False,
                        help="Display all users")
    parser.add_argument("-d", "--delete", action="store_true", dest="delete", default=False,
                        help="Delete user")
    parser.add_argument("-e", "--edit", dest="edit", default=False,
                        help="Edit emeil")

    options = parser.parse_args()
    return options


def solution(options):
    con = connect_to_db('warsztat1')
    cursor = con.cursor()
    if options.username and options.password:
        if not options.edit and not options.delete:
            users = Users.load_all_users(cursor)
            users_pom = []
            usr_email = input("Podaj emeil: ")
            for user in users:
                users_pom.append(user.email)
            if usr_email in users_pom:
                print('Użytkownik o emeilu: '+user.email+' istnieje')
            else:
                user = Users()
                user.username = options.username
                usr_email = input("Podaj emeil: ")
                if usr_email:
                    user.email = usr_email
                else:
                    print("Taki emeil jest już w bazie")
                usr_pass = ''
                while len(usr_pass) < 8:
                    usr_pass = input("Podaj hasło (minimum 8 znaków): ")
                user.set_password(usr_pass, None)
                try:
                    user.save_to_db(cursor)
                except Exception:
                    print("niepoprawne dane")
        if options.edit:
            user = Users.load_user_by_login(cursor, options.username)
            if check_password(options.password, user.hashed_password):
                try:
                    if len(options.newpass) >= 8:
                        user.set_password(options.newpass, None)
                        user.save_to_db(cursor)
                    else:
                        print('Hasło powinno mieć minimum 8 znaków')
                except Exception:
                    print('Nie podałeś parametru "-n"')
            else:
                print("Hasło niepoprawne")
        if options.delete:
            user = Users.load_user_by_login(cursor, options.username)
            print(user.id, user.username+' został usunięty')
            if check_password(options.password, user.hashed_password):
                user.delete_user(cursor)
    if options.list:
        users = Users.load_all_users(cursor)
        for user in users:
            print('user: "'+user.username+'" ma emeil: '+user.email+' id.'+str(user.id))

    cursor.close()
    con.close()


if __name__ == "__main__":
    solution(set_options())
