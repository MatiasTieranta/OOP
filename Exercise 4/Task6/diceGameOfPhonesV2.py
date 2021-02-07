import dice as dice
import cellphone as cellphone


def main():
    phones = []
    for i in range(1, 6):
        phones.append(cellphone.Cellphone(10000, 'Apple', 'Iphone 7', '3000', '40', i))
    dice_roll = dice.Dice()
    dice_roll.toss_number()
    print(phones[dice_roll.get_sideup()])


# Call the main function.
main()
