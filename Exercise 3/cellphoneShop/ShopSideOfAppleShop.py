# File: ShopSideOfAppleShop
# Author: Matias Tieranta
# Description: The BankAccount class simulates a bank account


class Cellphone:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, retailprice, manufacturer, model):
        self.__retailprice = retailprice
        self.manufacturer = manufacturer
        self.model = model

    # The get_balance method returns retail price.
    def get_balance(self):
        return self.__retailprice

    # The get_owner1 method returns the manufacturer of phone
    def get_manufacturer(self):
        return self.manufacturer
    # The get_owner2 method returns the model of phone

    def get_model(self):
        return self.model

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''manufacturer: {self.manufacturer} model: {self.model} retailprice: {self.__retailprice} '''
