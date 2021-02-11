# File: dice.py
# Author: Matias Tieranta
# Description: Dice that can be rolled

import random


# Class definition


class Dice:
    def __init__(self, dice_id):
        self.__side = 1
        self.__id = dice_id

    def roll_dice(self):
        self.__side = random.randint(1, 6)

    def get_side(self):
        return self.__side

    def set_side(self, dice_side):
        self.__side = dice_side.__side

    def get_id(self):
        return self.__id

    def set_id(self, dice_id):
        self.__id = dice_id

    def __str__(self):
        return 'Dice' + format(self.__id) + 'is' + ','
