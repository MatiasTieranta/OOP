# File: Car.py
# Author: Matias Tieranta
# Description: Example how to create Car class with accessor and mutator methods


class Car:
    def __init__(self, make, model, mileage, price, colour, maxium_load_limit, size_of_trunk):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__colour = colour
        self.__maxium_load_limit = maxium_load_limit
        self.__size_of_trunk = size_of_trunk
        self.id = 1

        # The get_balance method returns retail price.

    def get_make(self):
        return self.__make

    def set_make(self):
        return self.__make

        # The get_owner1 method returns the manufacturer of phone

    def get_model(self):
        return self.__model

    def set_model(self):
        return self.__model

    # The get_balance method returns retail price.

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self):
        return self.__mileage

    # The get_balance method returns retail price.

    def get_price(self):
        return self.__price

    def set_price(self):
        return self.__price

    # The get_balance method returns retail price.

    def get_colour(self):
        return self.__colour

    def set_colour(self):
        return self.__colour

    # The get_balance method returns retail price.

    def get_maxium_load_limit(self):
        return self.__maxium_load_limit

    def set_maxium_load_limit(self):
        return self.__maxium_load_limit

    # The get_balance method returns retail price.

    def get_size_of_trunk(self):
        return self.__size_of_trunk

    def set_size_of_trunk(self):
        return self.__size_of_trunk

    def get_id(self):
        return self.id

    def set_id(self):
        return self.id

    def __str__(self):
        return f'''manufacturer: {self.__make}
           \nmodel: {self.__model} 
           \nmileage: {self.__mileage} km
           \nprice: {self.__price} euros
           \ncolour : {self.__colour}
           \nmaxium load limit: {self.__maxium_load_limit} kg
           \nsize of trunk: {self.__size_of_trunk} litre
           \nid: {self.id}'''





