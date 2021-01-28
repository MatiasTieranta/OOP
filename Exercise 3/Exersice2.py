# File: CoinTossingGame
# Author: Matias
# Description: Flipping coin game
import random


class Coin:

    # The__init__ method initializes the sideup data attribute with 'Heads'
    def __init__(self):
        self.__sideup = 'Heads'
        self.__currency = 'Euro'

    # The toss method generate a random number
    # int the range 0 to 3. If the number
    # 0, then sideup is set to 'Heads'
    # if 1 sideup is set to 'Tails'
    # if 2 sideup is set to 'Upright'
    # if 3 sideup is set to 'you missed the table'

    def toss(self):
        toss_result = random.randint(0, 3)
        if toss_result == 0:
            self.__sideup = 'Heads'
        elif toss_result == 1:
            self.__sideup = 'tails'

        elif toss_result == 2:
            self.__sideup = 'Coin land on Upright!'

        elif toss_result == 3:
            self.__sideup = 'Oh no you missed the table'

    def toss_currency(self):
        toss_result = random.randint(0, 4)
        if toss_result == 0:
            self.__currency = 'Euro'
        elif toss_result == 1:
            self.__currency = 'Pound'
        elif toss_result == 2:
            self.__currency = 'Dollar'
        elif toss_result == 3:
            self.__currency = 'Ruble'
        elif toss_result == 4:
            self.__currency = 'Yen'

    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.__sideup

    def get_currency(self):
        return self.__currency


# The main function


def main():
    # Crete an object from Coin class.
    my_coin = Coin()
    my_coin.toss_currency()
    # Currency
    print("Currency is :", my_coin.get_currency())

    # Display the side of the coin that is facing up.
    print('This side is up : ', my_coin.get_sideup())

    # Toss the coin
    print("Im tossing the coin...")
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up: ', my_coin.get_sideup())


# Call the main function.
main()
