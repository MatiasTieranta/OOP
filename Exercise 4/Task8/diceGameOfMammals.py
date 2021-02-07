import dice as dice
import mammals as mammal
import Car


def main():
    list_of_mammals = []
    for i in range(1, 6):
        list_of_mammals.append(mammal.Mammal(10000, 'lisääteksitä', 'lisääteksitä', 'assdased', 'asdasdasd', 'asdasdasd'))
    dice_roll = dice.Dice()
    dice_roll.toss_number()
    print(list_of_mammals[dice_roll.get_sideup()-1])

    print(Car)


# Call the main function.
main()
