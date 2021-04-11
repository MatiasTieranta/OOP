# File: login.py
# Author: Matias Tieranta
# Description: With this we will have login function


import sys
from getpass import getpass


# Lets define how login will work
def login():
    username()
    password()


# User will input username for login
def username():
    input('Username: ')


# User will input password and password correctness is validated
def password():
    correct_password = '1234'
    user_password = getpass('Password: ')

    # If password is correct program will will succeed to storage_manager
    if user_password == correct_password:
        print('Correct welcome!')
    # Else program will tell, that password is wrong and exit program
    else:
        print('Password wrong exiting...')
        sys.exit()
