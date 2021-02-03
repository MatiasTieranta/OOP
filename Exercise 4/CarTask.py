# , make, model, mileage, price, colour, maxium_load_limit, size_of_trunk):
import Car


def main():
    # Get the manufacturer of the phone
    make = input('Enter the manufacturer :')

    # Get the model of the phone
    model = input('Enter the model: ')

    # Get the retailprice of phone
    mileage = float(input('enter the milage of car: '))

    price = float(input("enter price of car : "))

    colour = input("Enter disired colour of car : ")

    maxium_load_limit = float(input('enter maxium load limit of car : '))

    size_of_trunk = float(input('enter size of trunk :'))

    # Create a BankAccount object.
    carSpecs = Car.Car(make, model, mileage, price, colour, maxium_load_limit, size_of_trunk)

    print('Yours car we be like this', carSpecs)


main()
