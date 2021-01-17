# File name: Task 2 - 6 of exercise 1
# Author: Matias Tieranta
# Description: Tasks to 2 - 6


import random

even_count = 0
divided_by_three = 0

# Lets create empty list

numbers = []
numbers_negative = []
list_of_words = []

# lets set numbers of elements to list to ten
max_amount_of_elements = 10

# ask's to user fill 10 numbers
for i in range(0, max_amount_of_elements):
    x = int(input("Give 10 numbers please :"))
    if x == 0:
        break
    if x < 0:
        numbers_negative.append(x)
    if x % 2 == 0:
        even_count = even_count + 1
    if x % 3 == 0:
        divided_by_three += x

    # add users numbers to our empty list
    numbers.append(x)  # adding the element

# asks to user fill 10 words
for i in range(0, max_amount_of_elements):
    word = input("give 10 words please :")
    # add users word to our empty list
    list_of_words.append(word)

# Creates ten random numbers between 0-1000
random_list_of_numbers = random.sample(range(0, 1000), 10)

# sorts elements in list
sum_of_list = sum(numbers)
numbers.sort()
random_list_of_numbers.sort()
list_of_words.sort()

# Prints out everything
print(numbers, list_of_words, random_list_of_numbers, numbers_negative)
print("Even count in the lists are : ", even_count)
print("Sum of numbers in list divisible by three :", divided_by_three)
