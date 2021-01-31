# File: accountTest_demo.py
# Author: Matias Tieranta
# Description_: This program demonstrates the BankAccount class

import ShopSideOfAppleShop


def main():
    # Get the manufacturer of the phone
    manufacturer = input('Enter the manufacturer :')

    # Get the model of the phone
    model = input('Enter the model: ')

    # Get the retailprice of phone
    retail_price = float(input('enter the retail price: '))

    # Create a BankAccount object.
    phoneSpecs = ShopSideOfAppleShop.Cellphone(retail_price, manufacturer, model)

    # Display the balance
    print(phoneSpecs)


main()
