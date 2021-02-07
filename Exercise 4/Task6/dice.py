# File:diceTossingGame
# Author: Matias
# Description: diceGame

import random


class Dice:

    # The__init__ method initializes the sideup data attribute with 'Number one and Orange'
    def __init__(self):
        self.__sideup = 1

    #     # The toss method generate a random number

    def toss_number(self):
        toss_result = random.randint(0, 5)
        self.__sideup = toss_result
        if toss_result == 0:
            self.__sideup = 0
        elif toss_result == 1:
            self.__sideup = 1
        elif toss_result == 2:
            self.__sideup = 2
        elif toss_result == 3:
            self.__sideup = 3
        elif toss_result == 4:
            self.__sideup = 4
        elif toss_result == 5:
            self.__sideup = 5

    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.__sideup
