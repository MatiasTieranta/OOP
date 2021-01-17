import random

even_count = 0
divided_by_three = 0

# empty list

numbers = []
numbers_negative = []
lst_strings = []

# lets set numbers of elements to list 10
n = 10

# aks to user fill 10 numbers
for i in range(0, n):
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

for i in range(0, n):
    ele_str = input("give 10 words please :")

    lst_strings.append(ele_str)

randomlist = random.sample(range(0, 1000), 10)

sum_of_list = sum(numbers)
numbers.sort()
randomlist.sort()
lst_strings.sort()

print(numbers, lst_strings, randomlist, numbers_negative)
print("Even count in the lists are : ", even_count)
print("Numbers in list divided of three  :", divided_by_three)
