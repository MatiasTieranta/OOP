# File:         cleaning_day.py
# Author:       Matias Tieranta
# Description: Lets create code for summer cleaning and preparation for covid19

class House:

    # The __init__ method initializes first name last name and id

    def __init__(self, address, windows, floors, surfaces, windows_cleaned, bed_made, floors_vacuumed, surfaces_cleaned,
                 fridge, toilet_papers):
        self.__address = address
        self.__windows = windows
        self.__floors = floors
        self.__surfaces = surfaces
        self.__windows_cleaned = windows_cleaned
        self.__bed_made = bed_made
        self.__floors_vacuumed = floors_vacuumed
        self.__surfaces_cleaned = surfaces_cleaned
        self.__fridge = fridge
        self.__toilet_papers = toilet_papers

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_windows(self):
        return self.__windows

    def set_windows(self, windows):
        self.__windows = windows

    def get_floors(self):
        return self.__floors

    def set_floors(self, floors):
        self.__floors = floors

    def get_surfaces(self):
        return self.__surfaces

    def set_surfaces(self, surfaces):
        self.__surfaces = surfaces

    def set_windows_cleaned(self, windows_cleaned):
        self.__windows_cleaned = windows_cleaned

    def set_bed_made(self, bed_made):
        self.__bed_made = bed_made

    def set_floor_vacuumed(self, floors_vacuumed):
        self.__floors_vacuumed = floors_vacuumed

    def set_surfaces_cleaned(self, surfaces_cleaned):
        self.__surfaces_cleaned = surfaces_cleaned

    def set_fridge(self, fridge):
        self.__fridge = fridge

    def set_toilet_papers(self, toilet_papers):
        self.__toilet_papers = toilet_papers

    def __str__(self):
        return f'''  
            \nAddress of home: {self.__address}
            \nAmount of windows: {self.__windows}
            \nAmount of floors : {self.__floors}
            \nAmount of surfaces: {self.__surfaces}
            \nis windows cleaned: {self.__windows_cleaned}
            \nIs bed made: {self.__bed_made}
            \nIs floors vacuumed: {self.__floors_vacuumed}
            \nIs surfaces cleaned: {self.__surfaces_cleaned}
            \nIs fridge full: {self.__fridge}
            \nIs there enought toilet papers: {self.__toilet_papers}
            


'''


state1 = House('geneerinen osoite 12', '4', '1', '5', 'no', 'no', 'no', 'no', 'no', 'no')
print(state1)
print('Lets start cleaning')

state2 = House('geneerinen osoite 12', '4', '1', '5', 'Yes', 'Yes', 'no', 'no', 'no', 'no')
state3 = House('geneerinen osoite 12', '4', '1', '5', 'Yes', 'Yes', 'Yes', 'Yes', 'no', 'no')
state4 = House('geneerinen osoite 12', '4', '1', '5', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes')
state5 = House('geneerinen osoite 12', '4', '1', '5', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Too much')


print(state2)

print('Lets continue')

print(state3)

print('We need to go shopping')

print(state4)

print('Not enough toilet papers')

print(state5)

