import sys
from getpass import getpass


def login():
    username()
    password()


def username():
    user = input('Username: ')
    print("Username", user)


def password():
    correct_password = '1234'
    user_password = getpass('Password: ')
    if user_password == correct_password:
        print('Correct welcome !')
    else:
        print('Password wrong exiting...')
        sys.exit()
