# File:         quiz.py
# Author:       Matias Tieranta
# Description:  Quiz game of capitals with 10 questions.

# Welcomes user to game
print('welcome quiz of capitols')
# Open txt file to be used as directory
with open('quiz_answers.txt') as f:
    lines = f.readlines()

# Default values to be used
numRight = 0
wrong = []

# Quiz will have 10 questions
numOfQuestions = 10

# Tells to program to use first part as question and second as answer and change row
for line in lines[:numOfQuestions]:
    question, rightAnswer = line.strip().split("\t")
    answer = input(question + ' ')
    if answer == rightAnswer:
        print('Right')
        numRight += 1

# Returns correct answer to user
    else:
        print('wrong the answer is %s.' % rightAnswer)
        wrong.append(question)


# After 10 question tells points that user had
else:
    numOfQuestions = 10
    print('You got %d question right' % (numRight))
