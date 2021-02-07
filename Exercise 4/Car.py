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

        # The get_make method returns maker.

    def get_make(self):
        return self.__make

    def set_make(self):
        return self.__make

        # The get_model method returns the model of car

    def get_model(self):
        return self.__model

    def set_model(self):
        return self.__model

    # The get_mileage method returns mileage.

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self):
        return self.__mileage

    # The get_price returns price of car.

    def get_price(self):
        return self.__price

    def set_price(self):
        return self.__price

    # The get_colour method returns colour.

    def get_colour(self):
        return self.__colour

    def set_colour(self):
        return self.__colour

    # The get_maxium_load_limit returns maxium load limit.

    def get_maxium_load_limit(self):
        return self.__maxium_load_limit

    def set_maxium_load_limit(self):
        return self.__maxium_load_limit

    # The get_size of trunk method returns size of trunk.

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





