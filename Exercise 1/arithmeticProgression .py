# File name: Task 7 of exercise 1
# Author: Matias Tieranta
# Description: Process with an arithmetic progression (AP)

# Take total numbers from user
first_Num = 0
Total_num = int(input("Enter the Total Numbers in this A.P Series: "))
diff = 2


# Count the number of terms that appeared in the AP
def term():
    return Total_num // diff


# The sum of the terms
def sum_of_terms():
    terms_sum = 0
    for i in range(first_Num, Total_num, diff):
        terms_sum += i
    return terms_sum


# sum of the squared terms
def squared_sum_of_terms():
    terms_sum = 0
    for i in range(first_Num, Total_num, diff):
        terms_sum += i ** 2
    return terms_sum


print(term())
print(sum_of_terms())
print(squared_sum_of_terms())
