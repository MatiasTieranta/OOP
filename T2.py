import random

# empty list

lst_numbers = []

# lets set numbers of elements to list 10
n = 10

# aks to user fill 10 numbers
for i in range(0, n):
    ele = int(input("Give 10 numbers please :"))

    # add users numbers to our empty list
    lst_numbers.append(ele)  # adding the element

lst_strings = []

for i in range(0, n):
    ele_str = input("give 10 words please :")

    lst_strings.append(ele_str)


randomlist = random.sample(range(0, 1000), 10)

print(lst_numbers, lst_strings, randomlist)
