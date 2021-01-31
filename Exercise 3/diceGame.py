# File:diceTossingGame
# Author: Matias
# Description: diceGame

import random


class Dice:

    # The__init__ method initializes the sideup data attribute with 'Number one and Orange'
    def __init__(self):
        self.__sideup = '1'
        self.__colour = 'Orange'

    # The toss method generate a random number
    # int the range 0 to 6. If the number
    # 1, then sideup is set to 'Orange and number One'
    # if 2 sideup is set to 'Black and number Two'
    # if 3 sideup is set to 'White and number Three'
    # if 4 sideup is set to 'Pink and number Four'
    # if 5 sideup is set to 'Turquoise and number five'
    # if 6 sideup is set to 'Red and number Six'
    # As a extra feature we can also lose our dice and its set to 'zero and none'

    def toss_number(self):
        toss_result = random.randint(0, 6)
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
        elif toss_result == 0:
            print('Where did that dice even go ?? we need to start again...')
            self.__colour = None
    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.__sideup

    def get_colour(self):
        return self.__colour


# The main function


def main():

    # Crete an object from Dice class.
    my_dice = Dice()

    # Display the side of the dice that is facing up.
    print('This side is up : ', my_dice.get_sideup(), my_dice.get_colour())

    # Toss the dice
    print("Im tossing the dice...")
    my_dice.toss_number()

    # Display the side of the dice that is facing up.
    print('This side is up: ', my_dice.get_sideup(), my_dice.get_colour())


# Call the main function.
main()