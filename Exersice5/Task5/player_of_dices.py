# File: dice.py
# Author: Matias Tieranta
# Description: Class named as Player including firstname, lastname and id

# Lets crate class player and give it first name, last name, anf id and initialize it
class player_of_dices:
    def __init__(self, firstname, lastname, id):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__id = id
        self.__sideup = 1

    # Lets se mutator and accessor methods
    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_sideup(self):
        return self.__sideup

    def set_sideup(self, sideup):
        self.__sideup = sideup

    # Returns wanted string

    def __str__(self):
        return 'First name of student is' + format(self.__firstname) + 'Last name of student is' + format(
            self.__lastname) + 'Id of player is' + format(self.__id) + 'toss number of player is' + format(self.__sideup) +'.'
