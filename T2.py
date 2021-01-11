import random

# empty list

lst_numbers = []
lst_numbers_negative = []

# lets set numbers of elements to list 10
n = 10

# aks to user fill 10 numbers
for i in range(0, n):
    ele = int(input("Give 10 numbers please :"))
    if ele == 0:
        break
    elif ele < 0:
        lst_numbers_negative.append(ele)

    # add users numbers to our empty list
    lst_numbers.append(ele)  # adding the element

lst_strings = []

for i in range(0, n):
    ele_str = input("give 10 words please :")

    lst_strings.append(ele_str)

randomlist = random.sample(range(0, 1000), 10)

lst_numbers.sort()
randomlist.sort()
lst_strings.sort()

print(lst_numbers, lst_strings, randomlist, lst_numbers_negative)

