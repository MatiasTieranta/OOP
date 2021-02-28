# File: mammals.py
# Author: Matias Tieranta
# Description: Example how does python inherits work with two sub classes

# Lets create base class
class Mammal:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, id, name, size, weight, dimensions):
        self.__id = id
        self.__name = name
        self.__size = size
        self.__weight = weight
        self.__dimensions = dimensions

    # Defines get and set to be used to sub classes
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


# Lets create domestic class from mammals
class domestic_animal(Mammal):

    def __init__(self, id, name, size, weight, dimensions, domestic, diet, noise):
        super().__init__(id, name, size, weight, dimensions)
        self.__isDomestic = domestic
        self.__diet = diet
        self.__noise = noise

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return 'id of mammal is' + self.get_id() + '\nname of mammals is ' + self.get_name() + \
               '\nsize of animal' + self.get_size() + '\nWeight of mammal is' + self.get_weight() + \
               '\nDimension of mammal is' + \
               self.get_dimensions() + '\ndiet of mammals is' + self.__diet + \
               '\nNoise of mammals is' + self.__noise + '\nAnimal is:' + self.__isDomestic


# Lets create wild animals class from mammals

class wild_animal(Mammal):
    def __init__(self, id, name, size, weight, dimensions, wild, diet, noise):
        super().__init__(id, name, size, weight, dimensions)
        self.__isWild = wild
        self.__diet = diet
        self.__noise = noise

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return 'id of mammal is' + self.get_id() + '\nname of mammals is ' + self.get_name() + \
               '\nsize of animal' + self.get_size() + '\nWeight of mammal is' + self.get_weight() + \
               '\nDimension of mammal is' + \
               self.get_dimensions() + '\ndiet of mammals is' + self.__diet + \
               '\nNoise of mammals is' + self.__noise + '\nAnimal is:' + self.__isWild


# Give values to inherit classes
bat = wild_animal(' 1', 'Bat', ' small', ' 200g', ' 10', 'Wild animal', ' insects', ' Na-nana-nana-na')
whale = wild_animal(' 2', 'Whale', 'huge', ' 1000kg', ' 10m', ' Wild animal', ' makril', ' Tick')
sealion = wild_animal(' 3', 'SeaLion', ' big', ' 300kg', ' 300cm', ' Wild animal', ' sardines vocals', 'threat vocals')

cat = domestic_animal(' 4', 'cat', ' normal', ' 4kg', ' 20cm', 'Domestic animal', ' fish', 'meowww')
dog = domestic_animal(' 5', 'dog', ' normal', ' 4kg', ' 20cm', ' Domestic animal', ' steak', 'barking')
bunny = domestic_animal(' 6', 'bunny', ' small', ' 2kg', ' 15cm', ' Domestic animal', ' carrots', 'sniff')


# Lets print out all classes
print('Here are some wild animals')
print(bat)
print()
print(whale)
print()
print(sealion)
print()
print()
print('Here are some domestic animals')
print(cat)
print()
print(dog)
print()
print(bunny)
