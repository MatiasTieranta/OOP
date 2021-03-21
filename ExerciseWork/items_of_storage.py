# File: storage.py
# Author: Matias Tieranta
# Description: Class named as Student including firstname, lastname and id and mammals

# Creates class student, with given first name, last name, id and mammal

class Storage:
    def __init__(self, manufacturer, price, id):
        self.__manufacturer = manufacturer
        self.__price = price
        self.__id = id

    # Adding accessor and mutator methods

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # Returns string
    def __str__(self):
        return f'''id of item is :{self.__id}
        \n manufacturer of product is :{self.__manufacturer} 
        \n price of product is :{self.__price}'''


class Electronics(Storage):
    def __init__(self, manufacturer, price, id, category):
        super().__init__(manufacturer, price, id)
        self.__category = category

    def __str__(self):
        return f'''id of item is :{self.get_id()}
        \n manufacturer of product is :{self.get_manufacturer()} 
        \n price of product is :{self.get_price()}
        \n Category of product is : {self.__category}'''


class Consumables(Storage):
    def __init__(self, manufacturer, price, id, category):
        super().__init__(manufacturer, price, id)
        self.__category = category

    def __str__(self):
        return f'''id of item is :{self.get_id()}
        \n Name of product is :{self.get_manufacturer()} 
        \n price of product is :{self.get_price()}
        \n Category of product is : {self.__category}'''


tv = Electronics('Phillips 50" 4k tv', '499', '1', 'electronics')

beefSteak = Consumables('Atria minuuttipihvi', '2,99euro', '2', 'Consumables')
print(tv)
print(beefSteak)
