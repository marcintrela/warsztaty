import argparse
from users import Users
from local_settings import connect_to_db
from pass_hash import *

def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",
                        action="store_true", dest="username", default=False,
                        help="User login")
    parser.add_argument("-p", "--password",
                        action="store_true", dest="password", default=False,
                        help="User password")
    parser.add_argument("-n", "--new-pass",
                        action="store_true", dest="newpass", default=False,
                        help="New password")
    parser.add_argument("-l", "--list",
                        action="store_true", dest="list", default=False,
                        help="Display all users")
    parser.add_argument("-d", "--delete",
                        action="store_true", dest="delete", default=False,
                        help="Delete user")
    parser.add_argument("-e", "--edit",
                        action="store_true", dest="edit", default=False,
                        help="Edit emeil")

    options = parser.parse_args()
    return options


def solution(options):

    if options.username and options.password:
        con = connect_to_db('warsztat1')
        cursor = con.cursor()
        user = Users.load_user_by_login(options.username)
        print(user.username)

        cursor.close()
        con.close()


if __name__ == "__main__":
    solution(set_options())