# File: accountTest_demo.py
# Author: Matias Tieranta
# Description_: This program demonstrates the BankAccount class

import ShopSideOfAppleShop


def main():
    # Get the manufacturer of the phone
    owner1 = input('Enter the manufacturer :')

    # Get the model of the fone
    owner2 = input('Enter the owner: ')

    # Get the retailprice of phone
    retail_price = float(input('enter the retail price: '))

    # Create a BankAccount object.
    savings = ShopSideOfAppleShop.Cellphone(retail_price, owner1, owner2)

    # Display the balance
    print(savings)


main()
