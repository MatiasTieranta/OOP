# File name: Task 5 of exercise 2
# Author: Matias Tieranta
# Code to calculate students average grade


# Lets ask five student names and their grades

stundent1Name = input("What is name of student one ?")
X = int(input('Students grade?'))
stundent2Name = input("What is name of student one ?")
Y = int(input('Students grade?'))
stundent3Name = input("What is name of student one ?")
Z = int(input('Students grade?'))
stundent4Name = input("What is name of student one ?")
Q = int(input('Students grade?'))
stundent5Name = input("What is name of student one ?")
W = int(input('Students grade?'))

# Calculate sum of grades
Grades = X + Y + Z + Q + W

# Divide grades with floor function to get average
avg_of_grades = Grades // 5

# Prints out average
print(avg_of_grades)
