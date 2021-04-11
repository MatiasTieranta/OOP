# File: item.py
# Author: Matias Tieranta
# Description: This module includes base __init__ which we will inherit later

# The Item class holds general data about to be used later

class Item:

    # the __init__ method accepts arguments for the
    # name of product price id and category. It initializes
    # the data attributes with these values

    def __init__(self, name_of_product, price, id, category):
        self.__name_of_product = name_of_product
        self.__price = price
        self.__id = id
        self.__category = category

    # Adding accessor and mutator methods

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name_of_product(self):
        return self.__name_of_product

    def set_name_of_product(self, name_of_product):
        self.__name_of_product = name_of_product

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''id of item is: {self.__id}
        \nname of product is: {self.__name_of_product} 
        \nprice of product is: {self.__price}
        \ncategory of product is: {self.__category}'''
