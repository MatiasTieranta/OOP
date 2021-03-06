# File: CoinTossingGame
# Author: Matias
# Description: Flipping coin game
import random


class Coin:

    # The__init__ method initializes the sideup data attribute with 'Heads'
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generate a random number
    # int the range 0 to 1. If the number
    # 0, then sideup is set to 'Heads'
    # otherwise, sideup is set to 'Tails'

    def toss(self):
        if (random.randint(0, 1)) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method return the value referenced by sideup

    def get_sideup(self):
        return self.sideup


# The main function


def main():
    # Crete an object from Coin class.
    my_coin = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up: ', my_coin.get_sideup())

    # Toss the coin
    print("Im tossing the coin...")
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up: ', my_coin.get_sideup())


# Call the main function.
main()
