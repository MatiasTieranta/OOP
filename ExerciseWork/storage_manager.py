# File:
# Author:
# Description:

import login
import electronic
import consumable
import pickle
import uuid

# Lets crate menu

LOOK_UP = 1
ADD_ITEM = 2
CHANGE_ITEM = 3
DELETE_ITEM = 4
DISPLAY_ALL_ITEMS = 5
QUIT_ERP = 6

# Name of our
FILENAME = 'storage'


# Lets define main function and give value to menu
def main():
    login.login()
    storage = load_storage()

    choice = 0

    while choice != QUIT_ERP:
        divider()

        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(storage)
        elif choice == ADD_ITEM:
            add(storage)
        elif choice == CHANGE_ITEM:
            change(storage)
        elif choice == DELETE_ITEM:
            delete(storage)
        elif choice == DISPLAY_ALL_ITEMS:
            display(storage)
    save_items(storage)


# Loads information from our directory
def load_storage():
    try:
        input_file = open(FILENAME, 'rb')

        storage_dct = pickle.load(input_file)
        input_file.close()

    except IOError:
        storage_dct = {}
    return storage_dct


# Creates divider for program to look more clear
def divider():
    print('\n#####################################\n')


# Desing our menu
def get_menu_choice():
    print('Menu')
    print('1 LOOK UP ITEM')
    print('2 ADD PRODUCT TO STORAGE')
    print('3 CHANGE ITEM FROM STORAGE')
    print('4 DELETE ITEM FROM STORAGE')
    print('5 DISPLAY ALL ITEMS FROM STORAGE')
    print('6 QUIT')

    try:
        choice = int(input('\nEnter your choice: '))
    except ValueError:
        print("It's not integer")
        return 0

    if choice < LOOK_UP or choice > QUIT_ERP:
        print('\nInvalid choice!')
        return 0

    return choice


# Look up already created data
def look_up(storage):
    divider()
    id_to_lookup = input('Enter a id of product: ').strip()
    product = storage.get(id_to_lookup)
    if product is None:
        print('Id is not found')
        return None
    else:
        print()
        print(product)
        return product


def add(storage):
    divider()
    print('if you want add product to Electronics press 1')
    print('if you want add product to Consumables press 2')

    try:
        category = int(input('\nEnter category of product: '))
    except ValueError:
        print("It's not integer")
        return

    if category == 1:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        size = input('Give dimensions of product: ')
        # Generates unique id for product with uuid
        entry = electronic.Electronic(name_of_product, price, str(uuid.uuid4()), category, size)

    elif category == 2:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        expiration = input('expiration date is: ')
        weight = input('Weigh of product: ')
        # Generates unique id for product with uuid
        entry = consumable.Consumable(name_of_product, price, str(uuid.uuid4()), category, expiration, weight)

    else:
        print('Invalid category')
        return

    storage[entry.get_id()] = entry
    print('\nthe entry has been added')


def change(storage):
    divider()
    product = look_up(storage)
    if product is None:
        return
    if product.get_category() == 1:
        price = input('Price of Product: ')
        size = input('Give dimensions of product: ')
        entry = electronic.Electronic(product.get_name_of_product(), price, product.get_id(), product.get_category(),
                                      size)
    else:
        price = input('Price of Product: ')
        expiration = input('expiration date is: ')
        weight = input('Weigh of product: ')
        entry = consumable.Consumable(product.get_name_of_product(), price, product.get_id(), product.get_category(),
                                      expiration, weight)

    storage[product.get_id()] = entry
    print(entry)


def delete(storage):
    divider()
    id_to_delete = input('Please give id of product you would like to remove: ')
    if storage.get(id_to_delete) is not None:
        storage.pop(id_to_delete)
        print('\nDone')
    else:
        print('\nThat product is not found')


# Displays all data give to directory
def display(storage):
    for name_of_product in storage:
        divider()
        print(storage.get(name_of_product))


# lets save changes
def save_items(storage):
    output_file = open(FILENAME, 'wb')

    pickle.dump(storage, output_file)

    output_file.close()


