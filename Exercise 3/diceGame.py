# File: CoinTossingGame
# Author: Matias
# Description: Flipping coin game
import random


class Dice:

    # The__init__ method initializes the sideup data attribute with 'Heads'
    def __init__(self):
        self.__sideup = '1'
        self.__colour = 'Orange'

    # The toss method generate a random number
    # int the range 0 to 3. If the number
    # 0, then sideup is set to 'Heads'
    # if 1 sideup is set to 'Tails'
    # if 2 sideup is set to 'Upright'
    # if 3 sideup is set to 'you missed the table'

    def toss_number(self):
        toss_result = random.randint(1, 6)
        self.__sideup = toss_result
        if toss_result == 1:
            self.__colour = 'Orange'
        elif toss_result == 2:
            self.__colour = 'Black'
        elif toss_result == 3:
            self.__colour = 'White'
        elif toss_result == 4:
            self.__colour = 'Pink'
        elif toss_result == 5:
            self.__colour = 'Turquoise'
        elif toss_result == 6:
            self.__colour = 'Red'

    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.__sideup

    def get_colour(self):
        return self.__colour


# The main function


def main():
    # Crete an object from Coin class.
    my_dice = Dice()

    # Display the side of the coin that is facing up.
    print('This side is up : ', my_dice.get_sideup(), my_dice.get_colour())

    # Toss the coin
    print("Im tossing the coin...")
    my_dice.toss_number()

    # Display the side of the coin that is facing up.
    print('This side is up: ', my_dice.get_sideup(), my_dice.get_colour())


# Call the main function.
main()
