# File: ShopSideOfAppleShop.py
# Author: Matias Tieranta
# Description: The BankAccount class simulates a shop side of apple shop


class Mammal:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, id, species, name, size, weight, dimensions):
        self.__id = id
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimensions = dimensions

    def get_id(self):
        return self.__id

    def set_id(self):
        return self.__id

    def get_species(self):
        return self.__species

    def set_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def set_size(self):
        return self.__size

    def get_weight(self):
        return self.__weight

    def set_weight(self):
        return self.__weight

    def get_dimensions(self):
        return self.__dimensions

    def set_dimensions(self):
        return self.__dimensions

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''id: {self.__id}
        \nspecies: {self.__species} 
        \nname: {self.__name}
        \nsize: {self.__size}
        \nweight: {self.__weight}
        \ndimensions: {self.__dimensions}'''


