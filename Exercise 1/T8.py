# File name: Task 9 of exercise 1
# Author: Matias Tieranta
# Description: Code a simple (and textual) implementation of Rock-Paper-Scissors game. Best of 3 games wins.
import random

player_points = 0
computer_points = 0

player_turn = input("Rock, Paper, Scissors ! ")

computer_turn = random.randint(1, 3)
if computer_turn == 1:
    computer_turn = "Rock"
elif computer_turn == 2:
    computer_turn = "Paper"
elif computer_turn == 3:
    computer_turn = "Scissors"

print("player_turn", player_turn)
print("computer_turn", computer_turn)

if computer_turn == player_turn:
    print("Tie ! ")
elif computer_turn < player_turn:
    computer_points += 1
    print("Point for computer")

elif computer_turn > player_turn:
    player_points += 1
    print("point for player")

print("Player points :", player_points)
print("Computer points :", computer_points)
