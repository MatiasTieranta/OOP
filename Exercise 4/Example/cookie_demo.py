class Cookie:

    # Initialize data attribute
    # __shape and __flavour are data attributes
    # They are both private
    def __init__(self, init_shape, init_flavor):
        self.__shape = init_shape
        self.__flavour = init_flavor
        # if you need to add attribute  add here

    # Accessor methods (get), mutator method (set)

    def set_shape(self, desire_shape):
        self.__shape = desire_shape

    def get_shape(self):
        return self.__shape

    def set_flavour(self, desired_flavour):
        self.__flavour = desired_flavour

    def get_flavour(self):
        return self.__flavour

# Return the object's state (= values of the data attribute)
    def __str__(self):
        return 'Your cookies is '+ format(self.__shape) + '-shaped and taste like  ' + format(self.__flavour) + '.'
