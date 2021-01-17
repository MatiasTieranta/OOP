# Series Using Math Formula

# Take the Input from the User
first_Num = 0
Total_num = int(input("Enter the Total Numbers in this A.P Series: "))
diff = 2


#
def term():
    return Total_num // diff


def sum_of_terms():
    terms_sum = 0
    for i in range(first_Num, Total_num, diff):
        terms_sum += i
    return terms_sum


def squared_sum_of_terms():
    terms_sum = 0
    for i in range(first_Num, Total_num, diff):
        terms_sum += i ** 2
    return terms_sum


print(term())
print(sum_of_terms())
print(squared_sum_of_terms())
