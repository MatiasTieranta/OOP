import random
import cookie_demo as cookie


def main():
    # print('hello')

    choises = ['rock', 'paper', 'scissors']
    cookie_shape = random.choice(choises)

    print('computer chose:', cookie_shape)

    cookie_flavour = input('choose a flavour :')
    print('Cookie flavour will be', cookie_flavour)

    # create a cookie-object and initialize it with shape and flavour add here too. And get and set methods
    my_cookie = cookie.Cookie(cookie_shape, cookie_flavour)

    # Lets see, what my cookie state is
    print(my_cookie)

    print('Boooooring')
    cookie_flavour = input('Change flavour to : ')
    cookie_shape = input('Change shape to : ')

    my_cookie.set_flavour(cookie_flavour)
    my_cookie.set_shape(cookie_shape)

    print('\nHere is your new cookie, enjoy.\n')
    print(my_cookie)


main()
