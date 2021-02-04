# File:diceTossingGame
# Author: Matias
# Description: diceGame
import random


class newPhone:

    # The__init__ method initializes the sideup data attribute with 'Number one and Orange'
    def __init__(self, manufacturer, price, model):
        self.__sideup = toss_result
        self.__manufacturer = manufacturer
        self.__price = price
        self.__model = model
        self.id = 1

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
        toss_result = random.randint(1, 6)
        if toss_result == 1:
            self.__manufacturer = 'Nokia'
            self.__price = 299
            self.__model = 8.3
            self.id = 1
        elif toss_result == 2:
            self.__manufacturer = 'Samsung'
            self.__price = 799
            self.__model = 21
            self.id = 2
        elif toss_result == 3:
            self.__manufacturer = 'Apple'
            self.__price = 499
            self.__model = 1
            self.id = 3

        elif toss_result == 4:
            self.__manufacturer = 'Huawei'
            self.__price = 299
            self.__model = 'honor7'
            self.id = 4
        elif toss_result == 5:
            self.__manufacturer = 'Jolla'
            self.__price = 988
            self.__model = 'phone'
            self.id = 5
        elif toss_result == 6:
            self.__manufacturer = 'Xiaomi'
            self.__price = 999
            self.__model = '10tpro'
            self.id = 6

    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.__sideup

    def set_sideup(self):
        return self.__sideup

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self):
        return self.__manufacturer

    def get_price(self):
        return self.__price

    def set_price(self):
        return self.__price

    def get_model(self):
        return self.__model

    def set_model(self):
        return self.__model

    def __str__(self):
        return 'Your cookies is ' + format(self.__sideup) + '-shaped and taste like  ' + format( self.__manufacturer) + '.'
