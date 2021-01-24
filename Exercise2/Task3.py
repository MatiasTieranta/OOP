# File name: Task 9 of exercise 1
# Author: Matias Tieranta
# Pseudocode for getting the grade of this course

# User inputs how many tasks hes/ her did in a course?

Tasks = int(input("How many task you done ?"))

# Program will return user grade.
# Atleast 13 accepted exersices 5
# Atleast 12 accepted exersices 4
# Atleast 11 accepted exersices 3
# Atleast 10 accepted exersices 2
# Atleast 9 accepted exersices 1
# Under 9 accepted course is failed.
if Tasks >= 13 and Tasks <= 20:
    print('well done! Its a 5')
elif Tasks == 12:
    print('job well done Its a 4')
elif Tasks == 11:
    print('you get a 3')
elif Tasks == 10:
    print('you get a 2')
elif Tasks == 9:
    print('you get a 1, next time better')
elif Tasks == Tasks >= 0 and Tasks <= 8:
    print('Sory to tell you this its a FAIL')
