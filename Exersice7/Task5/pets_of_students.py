# File:         pets_of_students.py
# Author:       Matias Tieranta
# Description:  Demo how does inheritance work

class Students:

    # The __init__ method initializes first name last name and id

    def __init__(self, first_name, last_name, student_ID):
        self.__student_ID = student_ID
        self.__firstname = first_name
        self.__lastname = last_name
        self.__pets = []

    # Let's define how to get and set

    def get_first_name(self):
        return self.__firstname

    def set_firs_name(self, first_name):
        self.__firstname = first_name

    def get_last_name(self):
        return self.__lastname

    def set_last_name(self, last_name):
        self.__lastname = last_name

    def get_student_ID(self):
        return self.__student_ID

    def set_student_ID(self, student_ID):
        self.__student_ID = student_ID

    # The __str__ method returns a string indicating the objects state
    def __str__(self):
        return f'''id: {self.__student_ID}
        \nFirst name: {self.__firstname}
        \nLast name: {self.__lastname}
        '''


# Inherit pets from students ?
class Pet(Students):
    # The __init__ method also species and a name

    def __init__(self, first_name, last_name, student_ID, species, name):
        super().__init__(first_name, last_name, student_ID)
        self.__name = name
        self.__Species = species

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_species(self):
        return self.__Species

    def set_species(self, species):
        self.__Species = species
    # The __str__ method returns a string indicating the objects state

    def __str__(self):
        return f'''id: {self.get_student_ID()}
            \nFirst name: {self.get_first_name()}
            \nLast name: {self.get_last_name()}
            \nName of Pet: {self.__name}
            \nSpecie of pet: {self.__Species}
            '''


# lets print jaakon koira and give it values
jaakon_koira = Pet('Jaakko', 'Virtanen', '11', 'Koira', 'Musti')

print(jaakon_koira)
