# File: storage_manager.py
# Author: Matias Tieranta
# Description: This pr

import login
import electronic
import consumable
import pickle
import uuid

# Global constants for menu choices

LOOK_UP = 1
ADD_ITEM = 2
CHANGE_ITEM = 3
DELETE_ITEM = 4
DISPLAY_ALL_ITEMS = 5
QUIT_ERP = 6

# Global constant for the file name
FILENAME = 'storage'


# Main function
def main():
    # Calls login function
    login.login()

    # Loads the existing contact dictionary and assign it to storage
    storage = load_storage()

    # Initialize a variable for the user's choice
    choice = 0

    # Process menu selections until user decide to quit
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

    # Save the items to storage
    save_items(storage)


# Loads information from our directory
def load_storage():
    try:
        # Opens the storage.dat file
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary
        storage_dct = pickle.load(input_file)

        # Close the dictionary
        input_file.close()

    except IOError:
        # If couldn't open the file, create new one
        storage_dct = {}

    # Returns to dictionary
    return storage_dct


# Creates divider for program to look more clear
def divider():
    print('\n#####################################\n')


# Displays the menu and validates choice from user
def get_menu_choice():
    print('Menu')
    print('1 LOOK UP ITEM')
    print('2 ADD PRODUCT TO STORAGE')
    print('3 CHANGE ITEM FROM STORAGE')
    print('4 DELETE ITEM FROM STORAGE')
    print('5 DISPLAY ALL ITEMS FROM STORAGE')
    print('6 QUIT')

    try:
        # Get the user's input
        choice = int(input('\nEnter your choice: '))
    # Validates input of user
    except ValueError:
        print("It's not integer")
        return 0

    if choice < LOOK_UP or choice > QUIT_ERP:
        print('\nInvalid choice!')
        return 0

    return choice


# Looks up an item in the specified dictionary
def look_up(storage):
    # adds divider to output
    divider()
    # gets the id to look up
    id_to_lookup = input('Enter a id of product: ').strip()
    product = storage.get(id_to_lookup)
    # Validates user input
    if product is None:
        print('Id is not found')
        return None
    else:
        # Looks item up from dictionary
        print()
        print(product)
        return product


# Adds a new entry into specified dictionary
def add(storage):
    # adds divider to output
    # divider()

    # First User is asked to decide what category the product is
    print('if you want add product to Electronics press 1')
    print('if you want add product to Consumables press 2')

    # Validates user input
    try:
        category = int(input('\nEnter category of product: '))
    except ValueError:
        print("It's not integer")
        return
    # If user choice is 1 product will be added to Electronic
    if category == 1:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        size = input('Give dimensions of product: ')
        # Generates unique id for product with uuid
        entry = electronic.Electronic(name_of_product, price, str(uuid.uuid4()), category, size)

    # If user choice is 2 product will be added to Electronic
    elif category == 2:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        expiration = input('expiration date is: ')
        weight = input('Weigh of product: ')
        # Generates unique id for product with uuid
        entry = consumable.Consumable(name_of_product, price, str(uuid.uuid4()), category, expiration, weight)

    # Validates category choice of user
    else:
        print('Invalid category')
        return
    # If everything goes as intended adds item to dictionary
    storage[entry.get_id()] = entry
    print('\nthe entry has been added')


# User has also chance to manipulate allready created products
def change(storage):
    # adds divider to output
    divider()
    # Looks up item using look_up command witch we created earlier
    product = look_up(storage)
    # Validates user input
    if product is None:
        return

    # If user choice is 1 product will be added to Electronic

    if product.get_category() == 1:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        size = input('Give dimensions of product: ')
        entry = electronic.Electronic(name_of_product, price, product.get_id(), product.get_category(),
                                      size)
        # If user choice is 2 product will be added to Electronic
    else:
        name_of_product = input('Give name of product: ')
        price = input('Price of Product: ')
        expiration = input('expiration date is: ')
        weight = input('Weigh of product: ')
        entry = consumable.Consumable(name_of_product, price, product.get_id(), product.get_category(),
                                      expiration, weight)
    # If everything goes as intended updated
    storage[product.get_id()] = entry
    print(entry)


# User has chance to delete the product from storage
def delete(storage):
    # adds divider to output
    divider()

    # User will give id witch he/she want's to remove
    id_to_delete = input('Please give id of product you would like to remove: ')
    if storage.get(id_to_delete) is not None:
        storage.pop(id_to_delete)
        print('\nDone')
    # User input validation
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
