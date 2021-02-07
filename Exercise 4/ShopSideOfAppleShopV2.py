# File: ShopSideOfAppleShop.py
# Author: Matias Tieranta
# Description: The BankAccount class simulates a shop side of apple shop


class Cellphone:

    # The __init__ method initializes retail prize, model and manufacturer

    def __init__(self, retailprice, manufacturer, model, battery, camera):
        self.__retailprice = retailprice
        self.manufacturer = manufacturer
        self.model = model
        self.id = 1
        self.__battery = battery
        self.__camera = camera

    # The get_balance method returns retail price.
    def get_balance(self):
        return self.__retailprice

    # The get_owner1 method returns the manufacturer of phone
    def get_manufacturer(self):
        return self.manufacturer

    # The get_owner2 method returns the model of phone

    def get_model(self):
        return self.model

    def get_id(self):
        return self.id

    def set_id(self):
        return self.id

    def get_batterysize(self):
        return self.__battery

    def set_batterysize(self):
        return self.__battery

    def get_camera(self):
        return self.__camera

    def set_camera(self):
        return self.__camera

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''manufacturer: {self.manufacturer}
        \nmodel: {self.model} 
        \nretailprice: {self.__retailprice}
        \ncamera has {self.__camera}pixels
        \npixels battery size is : {self.__battery}mh 
        \nid of product: {self.id}'''


