# File:
# Author:
# Description:

import item


class Electronic(item.Item):
    def __init__(self, name_of_product, price, id, category, size):
        item.Item.__init__(self, name_of_product, price, id, category)

        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_weight(self):
        return self.__size

    def __str__(self):
        st = super(Electronic, self).__str__()
        st += '\n\nsize of product is: ' + str(self.__size)
        return st
