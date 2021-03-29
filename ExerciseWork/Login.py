import sys


class UserLogon():

    def login(self):
        username = input('Username: ')
        print("Username", username)

    def password(self):
        correct_password = 'salasana123!'
        user_password = input('Password: ')
        if user_password == correct_password:
            print('Correct welcome !')
        else:
            sys.exit()


def func(obj):
    obj.login()
    obj.password()


obj_user_logon = UserLogon()
func(obj_user_logon)

