# File: dice.py
# Author: Matias Tieranta
# Description: Direcotory named as Student including firstname, lastname and id and mammal


import items_of_storage
import pickle

# Lets crate menu

LOOK_UP = 1
ADD_ITEM = 2
CHANGE_ITEM = 3
DELETE_ITEM = 4
DISPLAY_ALL_ITEMS = 5
QUIT_ERP = 6

# Name of our
FILENAME = 'Storage_of_shop'


# Lets define main function and give value to menu
def main():
    storage_of_shop = load_storage()

    choice = 0

    while choice != QUIT_ERP:

        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(storage_of_shop)
        elif choice == ADD_ITEM:
            add(storage_of_shop)
        elif choice == CHANGE_ITEM:
            change(storage_of_shop)
        elif choice == DELETE_ITEM:
            delete(storage_of_shop)
        elif choice == DISPLAY_ALL_ITEMS:
            display(storage_of_shop)
    save_items(storage_of_shop)


# Loads information from our directory
def load_storage():
    try:
        input_file = open(FILENAME, 'rb')

        storage_dct = pickle.load(input_file)
        input_file.close()


    except IOError:
        storage_dct = {}
    return storage_dct


# Desing our menu
def get_menu_choice():
    print()
    print('Menu')
    print('1 LOOK UP ITEM')
    print('2 ADD PRODUCT TO STORAGE')
    print('3 CHANGE ITEM FROM STORAGE')
    print('4 DELETE ITEM FROM STORAGE')
    print('5 DISPLAY ALL ITEMS FROM STORAGE')
    print('6 QUIT')

    choice = int(input('Enter your choice :'))

    while choice < LOOK_UP or choice > QUIT_ERP:
        choice = int(input('enter valid choice'))

    return choice


# Look up allready created data
def look_up(storage_of_shop):
    name_of_product = input('Enter a name: ')

    print(storage_of_shop.get(name_of_product, 'That name is not found'))

    # Adds new data


def add(storage_of_shop):
    name_of_product = input('Give name of product')
    price = input('Price of Product ')
    id = int(input('id of product'))
    category = int(input('If you want add product to Consumables press 1 \n'
                         'if you want add product to Electronics press 2\n'
                         ': '))
    if category == 1:
        entry = items_of_storage.Consumables(name_of_product, price, id, category)
    else:
        entry = items_of_storage.Electronics(name_of_product, price, id, category)

    if name_of_product not in storage_of_shop:
        storage_of_shop[name_of_product] = entry
        print('the entry has been added')
    else:
        print('That name already exists')


def change(storage_of_shop):
    name_of_original_product = input('Enter a name: ')
    name_of_product = input('Give name of product')
    price = input('Price of Product ')
    id = int(input('id of product'))
    category = int(input('If you want add product to Consumables press 1 \n'
                         'if you want add product to Electronics press 2\n'
                         ': '))
    if category == 1:
        entry = items_of_storage.Consumables(name_of_product, price, id, category)
    else:
        entry = items_of_storage.Electronics(name_of_product, price, id, category)

    if name_of_original_product == storage_of_shop:
        storage_of_shop[name_of_original_product] = entry
    else:
        print('There is no product to change')


def delete(storage_of_shop):
    name_of_product = input('Please give me name of product you would like to remove :')
    if storage_of_shop.get(name_of_product) is not None:
        storage_of_shop.pop(name_of_product)
        print('Done')
    else:
        print(storage_of_shop.get(name_of_product, 'That id is not found'))


# Displays all data give to directory
def display(storage_of_shop):
    for name_of_product in storage_of_shop:
        print(storage_of_shop.get(name_of_product))


# lets save changes
def save_items(storage_of_shop):
    output_file = open(FILENAME, 'wb')

    pickle.dump(storage_of_shop, output_file)

    output_file.close()


main()
