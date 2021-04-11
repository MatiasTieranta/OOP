# File: electronic
# Author: Matias Tieranta
# Description: electronic is inheritance class from item

# Imports item class to be inherited
import item


class Electronic(item.Item):

    # The __init__ method accepts arguments for the
    # Electronic's name of product, price, id, category, size

    def __init__(self, name_of_product, price, id, category, size):
        # Call the superclass __init__ method annd pass
        # the required arguments. Self argument is also passed

        item.Item.__init__(self, name_of_product, price, id, category)

        # Initialize the __size attribute
        self.__size = size

    # The set_size method is the mutator for the
    # __size attribute
    def set_size(self, size):
        self.__size = size

    # The get_size method is the accessor for the
    # __size attribute
    def get_size(self):
        return self.__size

    # __str__ returns wanted string
    def __str__(self):
        st = super(Electronic, self).__str__()
        st += '\n\nsize of product is: ' + str(self.__size)
        return st
