# File:
# Author:
# Description:


import sys
from getpass import getpass


def login():
    username()
    password()


# Mockup for login
def username():
    input('Username: ')


def password():
    correct_password = '1234'
    user_password = getpass('Password: ')
    if user_password == correct_password:
        print('Correct welcome!')
    else:
        print('Password wrong exiting...')
        sys.exit()
