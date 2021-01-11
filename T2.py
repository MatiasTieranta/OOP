# empty list
lst = []

# lets set numbers of elements to list 10
n = 10

# aks to user fill 10 numbers
for i in range(0, n):
    ele = int(input("Give 10 numbers please :"))

    # add users numbers to our empty list
    lst.append(ele)  # adding the element

lst1 = []


for i in range(0, n):
    ele_str = input("give 10 words please :")

    lst1.append(ele_str)

print(lst, lst1)
