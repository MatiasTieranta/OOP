# File: CoinTossingGame
# Author: Matias
# Description: Flipping coin game
import random

toss = random.randint(0, 3)


class Coin:

    # The__init__ method initializes the sideup data attribute with 'Heads'
    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generate a random number
    # int the range 0 to 3. If the number
    # 0, then sideup is set to 'Heads'
    # if 1 sideup is set to 'Tails'
    # if 2 sideup is set to 'Upright'
    # if 3 sideup is set to 'you missed the table'

    def toss(self):
        if toss == 0:
            self.sideup = 'Heads'
        elif toss == 1:
            self.sideup = 'tails'
        elif toss == 2:
            self.sideup = 'Coin land on Upright!'
        elif toss == 3:
            self.sideup = 'Oh no you missed the table'

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
