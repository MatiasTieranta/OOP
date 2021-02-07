# File: CarTask.py
# Author: Matias Tieranta
# Description: Example how to create Car class with main function
import Car


def main():
    # Get the manufacturer of the car
    make = input('Enter the manufacturer :')

    # Get the model of the car
    model = input('Enter the model: ')

    # Get the mileage of car
    mileage = float(input('enter the milage of car: '))

    # Get the price of car

    price = float(input("enter price of car : "))

    # Get the colour of car

    colour = input("Enter disired colour of car : ")

    # Get the maxium load limit of car

    maxium_load_limit = float(input('enter maxium load limit of car : '))

    # Get the sizo of trunk

    size_of_trunk = float(input('enter size of trunk :'))

    # Create a BankAccount object.
    carSpecs = Car.Car(make, model, mileage, price, colour, maxium_load_limit, size_of_trunk)

    print('Yours car we be like this', carSpecs)


main()
