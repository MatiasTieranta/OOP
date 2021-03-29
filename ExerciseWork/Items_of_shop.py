class Items:
    def __init__(self, name_of_product, price, id, category):
        self.__name_of_product = name_of_product
        self.__price = price
        self.__id = id
        self.__category = category

    # Adding accessor and mutator methods

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name_of_product(self):
        return self.__name_of_product

    def set_name_of_product(self, name_of_product):
        self.__name_of_product = name_of_product

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    # Returns string
    def __str__(self):
        return f'''id of item is :{self.__id}
        \n name of product is :{self.__name_of_product} 
        \n price of product is :{self.__price}
        \n category of product is: {self.__category}'''
