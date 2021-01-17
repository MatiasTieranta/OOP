# File name: Task 9 of exercise 1
# Author: Matias Tieranta
# Description: Function that prints out random number between 1-6

# Lets import random module to generate our random number
from random import randint


# We need only one number between of 1 and 6
# First lest define our input as Number
# Then we will choose limits for in this case one number between 1 and 6
# Define our function as a random_number and prints it out when calling it

def random_number():
    return randint(1, 6)


# Call to our function
print(random_number())
