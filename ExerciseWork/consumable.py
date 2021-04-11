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

        self.expiration = expiration
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_expiration_date(self):
        return self.expiration

    def set_expiration_date(self, expiration):
        self.expiration = expiration

    def __str__(self):
        st = super(Consumable, self).__str__()
        st += '\n\nweight of product is: ' + str(self.weight) + '\n\nexpiration date of product is: ' + str(
            self.expiration)
        return st
