# File name: Task 9 of exercise 1
# Author: Matias Tieranta
# Description: Code a simple (and textual) implementation of Rock-Paper-Scissors game. Best of 3 games wins.
import random

player_points = 0
computer_points = 0


def rps():
    global player_points
    global computer_points
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

    if player_turn == "Rock" and computer_turn == "Paper":
        computer_points += 1
        return "computer_turn won!!"
    elif player_turn == "Paper" and computer_turn == "Rock":
        player_points += 1
        return "player_turn won!!"
    elif player_turn == "Paper" and computer_turn == "Scissors":
        computer_points += 1
        return "computer_turn won!!"
    elif player_turn == "Scissors" and computer_turn == "Paper":
        player_points += 1
        return "player_turn won!!"
    elif player_turn == "Rock" and computer_turn == "Scissors":
        player_points += 1
        return "player_turn won!!"
    elif player_turn == "Scissors" and computer_turn == "Paper":
        computer_points += 1
        return "computer_turn won!!"
    elif player_turn == computer_turn:
        return "tie"


while (player_points < 2) and (computer_points < 2):
    print(rps())
    print("Player points :", player_points)
    print("Computer points :", computer_points)
