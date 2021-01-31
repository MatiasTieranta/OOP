# File: ShopSideOfAppleShop
# Author: Matias Tieranta
# Description: The BankAccount class simulates a bank account


class Cellphone:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, __retailprice, owner1, owner2):
        self.__retailprice = __retailprice
        self.__owner1 = owner1
        self.__owner2 = owner2

    # The get_balance method returns retail price.
    def get_balance(self):
        return self.__retailprice

    # The get_owner1 method returns the manufacturer of phone
    def get_owner1(self):
        return self.__owner1

    # The get_owner2 method returns the model of phone
    def get_owner2(self):
        return self.__owner2

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''manufacturer: {self.__owner1} model: {self.__owner2} retailprice: {self.__retailprice} '''
