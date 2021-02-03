# File: UserSideOfAppleShop.py
# Author: Matias Tieranta
# Description_: This program demonstrates the user side of apple shop class

import ShopSideOfAppleShopV2


def main():
    # Get the manufacturer of the phone
    manufacturer = input('Enter the manufacturer :')

    # Get the model of the phone
    model = input('Enter the model: ')

    # Get the retailprice of phone
    retail_price = float(input('enter the retail price: '))

    camera = float(input("Enter disired spesifications of phone's camera ? "))

    battery = float(input('enter battery size of phone : '))

    # Create a BankAccount object.
    phoneSpecs = ShopSideOfAppleShopV2.Cellphone(retail_price, manufacturer, model, camera, battery)

    # Display the specs of phone
    print('Here is the data that you provided : ', phoneSpecs)


main()
