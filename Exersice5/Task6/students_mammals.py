# File: dice.py
# Author: Matias Tieranta
# Description: Class named as Student including firstname, lastname and id and mammals


class Student:
    def __init__(self, first_name, last_name, id, mammals):
        self.__firstname = first_name
        self.__lastname = last_name
        self.__id = id
        self.__mammal = mammals

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, first_name):
        self.__firstname = first_name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, last_name):
        self.__lastname = last_name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_mammal(self):
        return self.__mammal

    def set_mammal(self, mammals):
        self.__mammal = mammals

    def __str__(self):
        return f'''first name of student is : {self.__firstname}
        \nLast name of student is : {self.__lastname} 
        \nid of student is: {self.__id}
        \nmammal of student is:0 {self.__mammal}'''
