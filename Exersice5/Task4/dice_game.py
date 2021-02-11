# File: dice_game.py
# Author: Matias Tieranta
# Description: Dice rolling game


import Dice


def make_list():
    dice_list = []

    for number in range(1, 4):
        print('Dice ', number)

        my_dice = Dice.Dice(number)

        dice_list.append(my_dice)

    return dice_list


def display_list(dice_list):
    for item in dice_list:
        print()
        print('Id', item.get_id())
        print('Side', item.get_side())


def roll_dices(dice_list):
    for item in dice_list:
        item.roll_dice()


def get_side_list(dice_list):
    side_list = []

    for item in dice_list:
        side_list.append(item.get_side())
    return side_list


def not_appended(continue_list, dice_object):
    for i in range(len(continue_list)):
        if dice_object == continue_list[i]:
            return False

    return True


def check_tie(dice_list):
    if range(len(dice_list) < 2):
        return dice_list
    else:

        tied_list = []

        side_list = get_side_list(dice_list)

        for i in range(len(side_list)):
            for j in range(i + 1, len(side_list)):

                if side_list[i] == dice_list[j]:

                    if not_appended(tied_list, dice_list[i]):
                        tied_list.append(dice_list[i])
                    if not_appended(tied_list, dice_list[j]):
                        tied_list.append(dice_list[j])

    return tied_list


def drop_lowest(dice_list):
    side_list = get_side_list(dice_list)

    smallest = min(side_list)

    for i in range(len(side_list)):
        if smallest == side_list[i]:
            dice_list.pop(i)
    return dice_list


def play_round(dices):
    print("\nLets roll the dices. ")
    roll_dices(dices)

    print('\nSituation after first roll.')
    display_list(dices)

    tied_list = check_tie(dices)

    while range(len(tied_list) > 1):
        print('\nUups, there is a tie', get_side_list(tied_list))
        roll_dices(tied_list)
        tied_list = check_tie(dices)

    print('\nIf there were ties, they are now cleared. Current situation')
    display_list(dices)

    print('\nNow we can drop the dice with lowest side')
    dices = drop_lowest(dices)

    print('\nDices still in game: ')
    display_list(dices)

    return dices


def main():
    dices = make_list()

    print('\nHere is your dices')
    display_list(dices)

    print('\n##### ROUND ONE ########')
    dices = play_round(dices)

    print('\n###### Round TWO #######')
    dices = play_round(dices)

    print("\nAnd the winner is :")
    display_list(dices)


main()
