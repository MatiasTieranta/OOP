# File: dice_game.py
# Author: Matias Tieranta
# Description: Dice rolling game


import students_mammals
import pickle

# Lets crate menu

LOOK_UP = 1
ADD = 2
DISPLAY = 3
QUIT = 4


# Name of our
FILENAME = 'Student.dat'


def main():
    pets_of_students = load_animals()

    choice = 0

    while choice != QUIT:

        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(pets_of_students)
        elif choice == ADD:
            add(pets_of_students)
        elif choice == DISPLAY:
            display(pets_of_students)
    save_animals(pets_of_students)


def load_animals():
    try:
        input_file = open(FILENAME, 'rb')

        animal_dct = pickle.load(input_file)
        input_file.close()


    except IOError:
        animal_dct = {}
    return animal_dct


def get_menu_choice():
    print()
    print('Menu')
    print('1 LOOKUP')
    print('2 ADD')
    print('3 Display')
    print('4 QUIT')

    choice = int(input('Enter your choice :'))

    return choice


def look_up(pets_of_students):
    first_name = input('Enter a name: ')

    print(pets_of_students.get(first_name, 'That name is not found'))


def add(pets_of_students):
    first_name = input('First name of student ')
    last_name = input('Last name of student ')
    student_id = int(input('Student id '))
    mammal_of_student = input('Mammal of student ')

    entry = students_mammals.Student(first_name, last_name, student_id, mammal_of_student)

    if first_name not in pets_of_students:
        pets_of_students[first_name] = entry
        print('the entry has been added')
    else:
        print('That name already exists')


def display(pets_of_students):
    for first_name in pets_of_students:
        print(pets_of_students.get(first_name))


def save_animals(pets_of_students):
    output_file = open(FILENAME, 'wb')

    pickle.dump(pets_of_students, output_file)

    output_file.close()


main()