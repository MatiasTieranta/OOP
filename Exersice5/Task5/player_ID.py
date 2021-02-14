import player_of_dices
import pickle
import dice
import random
# Lets crate menu

LOOK_UP = 1
ADD = 2
DISPLAY = 3
QUIT = 4

# Name of our
FILENAME = 'Player.dat'


def main():
    dices_of_player = load_dices()


    choice = 0

    while choice != QUIT:

        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(dices_of_player)
        elif choice == ADD:
            add(dices_of_player)
        elif choice == DISPLAY:
            display(dices_of_player)
    save_dices(dices_of_player)


def load_dices():
    try:
        input_file = open(FILENAME, 'rb')

        dices_dct = pickle.load(input_file)
        input_file.close()


    except IOError:
        dices_dct = {}
    return dices_dct


def get_menu_choice():
    print()
    print('Menu')
    print('1 LOOKUP')
    print('2 ADD')
    print('3 Display')
    print('4 QUIT')

    choice = int(input('Enter your choice :'))

    return choice


def look_up(dices_of_player):
    first_name = input('Enter a name: ')

    print(dices_of_player.get(first_name, 'That name is not found'))


def add(dices_of_students):
    first_name = input('First name of student ')
    last_name = input('Last name of student ')
    player_id = int(input('Player id '))
    for i in range(1, 6):
        dice_roll = dice.Dice()
        dice_roll.toss_number()
        dice_roll.get_sideup()
        print(dice_roll)
    entry = player_of_dices.player_of_dices(first_name, last_name, player_id)

    if first_name not in dices_of_students:
        dices_of_students[first_name] = entry
        print('the entry has been added')
    else:
        print('That name already exists')


def display(dices_of_students):
    for first_name in dices_of_students:
        print(dices_of_students.get(first_name))


def save_dices(dices_of_students):
    output_file = open(FILENAME, 'wb')

    pickle.dump(dices_of_students, output_file)

    output_file.close()


main()
