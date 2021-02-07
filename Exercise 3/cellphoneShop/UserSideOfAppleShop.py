# File: UserSideOfAppleShop.py
# Author: Matias Tieranta
# Description_: This program demonstrates the user side of apple shop class

import ShopSideOfAppleShop


def main():
    # Get the manufacturer of the phone
    manufacturer = input('Enter the manufacturer :')

    # Get the model of the phone
    model = input('Enter the model: ')

    # Get the retailprice of phone
    retail_price = float(input('enter the retail price: '))

    # Create a phonespecs object.
    phone_specs = ShopSideOfAppleShop.Cellphone(retail_price, manufacturer, model)

    # Display the specs of phone
    print('Here is the data that you provided : ', phone_specs)


main()
