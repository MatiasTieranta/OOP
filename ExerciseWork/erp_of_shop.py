# File: dice.py
# Author: Matias Tieranta
# Description: Direcotory named as Student including firstname, lastname and id and mammal

import Login
import electronics
import consumables
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
        print('\n#####################################')

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

    try:
        choice = int(input('\nEnter your choice :'))
    except ValueError:
        print("It's not integer")
        return 0

    if choice < LOOK_UP or choice > QUIT_ERP:
        print('\nInvalid choice !')
        return 0

    return choice


# Look up allready created data
def look_up(storage_of_shop):
    name_of_product = input('Enter a name: ')
    product = storage_of_shop.get(name_of_product)
    if product is None:
        print('Name is not found')
        return None
    else:

        print(product)
        return product

    # Adds new data


def add(storage_of_shop):
    category = int(input('if you want add product to Electronics press 1 \n'
                         'If you want add product to Consumables press 2 \n'
                         ': '))
    if category == 1:
        name_of_product = input('Give name of product :')
        price = input('Price of Product :')
        id = int(input('id of product :'))
        size = input('give size of product :')

        entry = electronics.Electronics(name_of_product, price, id, category, size)
    else:
        name_of_product = input('Give name of product :')
        price = input('Price of Product :')
        id = int(input('id of product :'))
        expiration = input('expiration date is :')
        weight = input('Weigh of product : ')
        entry = consumables.Consumables(name_of_product, price, id, category, expiration, weight)

    if name_of_product not in storage_of_shop:
        storage_of_shop[name_of_product] = entry
        print('the entry has been added')
    else:
        print('That name already exists')


def change(storage_of_shop):
    product = look_up(storage_of_shop)
    if product is None:
        return
    if product.get_category() == 1:
        price = input('Price of Product :')
        id = int(input('id of product :'))
        size = input('give size of product :')
        entry = electronics.Electronics(product.get_name_of_product(), price, id, product.get_category(), size)
    else:
        price = input('Price of Product :')
        id = int(input('id of product :'))
        expiration = input('expiration date is :')
        weight = input('Weigh of product : ')
        entry = consumables.Consumables(product.get_name_of_product(), price, id, product.get_category(), expiration,
                                        weight)

    storage_of_shop[product.get_name_of_product()] = entry
    print(entry)


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
        print('\n#####################################\n')
        print(storage_of_shop.get(name_of_product))


# lets save changes
def save_items(storage_of_shop):
    output_file = open(FILENAME, 'wb')

    pickle.dump(storage_of_shop, output_file)

    output_file.close()


Login.login()
main()
