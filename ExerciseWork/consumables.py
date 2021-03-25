import Items_of_shop


class Consumables(Items_of_shop.Storage):
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
        st = super(Consumables, self).__str__()
        st += '\n weight of product is :' + str(self.weight) + '\n expiration date of product is :' + str(
            self.expiration)
        return st
