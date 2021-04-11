# File: Consumables.py
# Author:Matias Tieranta
# Description: consumables is inheritance class from item


# Imports item class to be inherited
import item


class Consumable(item.Item):

    # The __init__ method accepts arguments for the
    # Consumable name of product, price, id, category, expiration date and weight

    def __init__(self, name_of_product, price, id, category, expiration, weight):
        super().__init__(name_of_product, price, id, category)

        # Initialize the expirarion and weight attribute
        self.expiration = expiration
        self.weight = weight

    # The get_weight method is the accessor for the
    # weight attribute
    def get_weight(self):
        return self.weight

    # The set_weight method is the mutator for the
    # weight attribute
    def set_weight(self, weight):
        self.weight = weight

    # The get_expiration_date method is the accessor for the
    # expiration attribute
    def get_expiration_date(self):
        return self.expiration

    # The set_expiration_date method is the mutator for the
    # expiration_date attribute
    def set_expiration_date(self, expiration):
        self.expiration = expiration

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        st = super(Consumable, self).__str__()
        st += '\n\nweight of product is: ' + str(self.weight) + '\n\nexpiration date of product is: ' + str(
            self.expiration)
        return st
