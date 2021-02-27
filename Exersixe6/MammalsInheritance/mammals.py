# File: ShopSideOfAppleShop.py
# Author: Matias Tieranta
# Description: The BankAccount class simulates a shop side of apple shop


class Mammal:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, id, name, size, weight, dimensions):
        self.__id = id
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimensions = dimensions

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_dimensions(self):
        return self.__dimensions

    def set_dimensions(self, dimensions):
        self.__dimensions = dimensions

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''id: {self.__id}
        \nname: {self.__name}
        \nsize: {self.__size}
        \nweight: {self.__weight}
        \ndimensions: {self.__dimensions}'''


class Whale(Mammal):

    def __init__(self, id, name, size, weight, dimensions, diet, noise):
        super().__init__(id, name, size, weight, dimensions)
        self.__diet = diet
        self.__noise = noise

    def __str__(self):
        return 'id of mammal is' + self.get_id() + '\nname of mammals is ' + self.get_name() + \
               '\nWeight of mammal is' + self.get_weight() + '\nDimension of mammal is' + \
               self.get_dimensions() + '\ndiet of mammals is' + self.__diet + '\nNoise of mammals is' + self.__noise


class Bat(Mammal):

    def __init__(self, id, name, size, weight, dimensions, diet, noise):
        super().__init__(id, name, size, weight, dimensions)
        self.__diet = diet
        self.__noise = noise

    def __str__(self):
        return 'id of mammal is' + self.get_id() + '\nname of mammals is ' + self.get_name() + \
               '\nWeight of mammal is' + self.get_weight() + '\nDimension of mammal is' + \
               self.get_dimensions() + '\ndiet of mammals is' + self.__diet + '\nNoise of mammals is' + self.__noise


class SeaLion(Mammal):

    def __init__(self, id, name, size, weight, dimensions, diet, noise):
        super().__init__(id, name, size, weight, dimensions)
        self.__diet = diet
        self.__noise = noise

    def __str__(self):
        return 'id of mammal is' + self.get_id() + '\nname of mammals is ' + self.get_name() + \
               '\nWeight of mammal is' + self.get_weight() + '\nDimension of mammal is' + \
               self.get_dimensions() + '\ndiet of mammals is' + self.__diet + '\nNoise of mammals is' + self.__noise


whale = Whale(' 1', 'Whale', 'long', ' rellylong', '31231S', ' makril', ' Tick')
bat = Bat(' 2', ' Bat', ' long', ' 200g', ' 20cm', ' insects', ' Na-nana-nana-na')
sealion = SeaLion(' 3', 'SeaLion', ' 300kg', ' 300kg', ' 300cm', ' sardines', ' threat vocals')

print(whale)
print()
print(bat)
print()
print(sealion)