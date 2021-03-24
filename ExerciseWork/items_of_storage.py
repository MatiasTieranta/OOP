# File: storage.py
# Author: Matias Tieranta
# Description: Class named as storage will provide method to return to stuff to future dictionary.

# Creates class storage and inherit from it two different classes to be stored.


class Storage:
    def __init__(self, name_of_product, price, id):
        self.__name_of_product = name_of_product
        self.__price = price
        self.__id = id

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

    # Returns string
    def __str__(self):
        return f'''id of item is :{self.__id}
        \n name of product is :{self.__name_of_product} 
        \n price of product is :{self.__price}'''


class Electronics(Storage):
    def __init__(self, name_of_product, price, id, category):
        super().__init__(name_of_product, price, id)
        self.__category = category

    # Returns string
    def __str__(self):
        return f'''id of item is : {self.get_id()}
        \n name of product is : {self.get_name_of_product()} 
        \n price of product is : {self.get_price()}
        \n Category of product is : {self.__category}'''


class Consumables(Storage):
    def __init__(self, name_of_product, price, id, category):
        super().__init__(name_of_product, price, id)
        self.__category = category

    # Returns stringAA
    def __str__(self):
        return f'''\nid of item is : {self.get_id()}
        \n Name of product is : {self.get_name_of_product()} 
        \n price of product is : {self.get_price()}
        \n Category of product is : {self.__category}'''


tv = Electronics('Phillips 50" 4k tv', '499', '1', 'electronics')

beefSteak = Consumables('Atria minuuttipihvi', '2,99euro', '2', 'Consumables')
print(tv)
print(beefSteak)
