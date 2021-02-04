import dice as dice
import cellphone as cellphone


def main():
    phones = []
    for i in range(1, 6):
        phones.append(cellphone.Cellphone(10000, 'lisääteksitä', 'lisääteksitä', 'assdased', 'asdasdasd', i))
    dice_roll = dice.Dice()
    dice_roll.toss_number()
    print(phones[dice_roll.get_sideup()-1])


# Call the main function.
main()
