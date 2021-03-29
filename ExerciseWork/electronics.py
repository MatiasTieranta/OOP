import Items_of_shop


class Electronics(Items_of_shop.Items):
    def __init__(self, name_of_product, price, id, category, size):
        Items_of_shop.Items.__init__(self, name_of_product, price, id, category)

        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_weight(self):
        return self.__size

    def __str__(self):
        st = super(Electronics, self).__str__()
        st += '\n size of product is :' + str(self.__size)
        return st
