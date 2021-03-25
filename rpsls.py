import random
from Game import Game, my_rules, my_gestures
from Computer import Computer, computer
from unittest import result

x = input('Please enter your name:')
print('Hello, ' + x + '. Good luck!')
print()
print('Here are the rules:')
for x in my_rules:
    print(x)
print()
print('The best of 3 will win the game!')
print()

playerOne_score = int(0)
computer_score = int(0)
score_limit = 5
while playerOne_score != score_limit or computer_score != score_limit:
    playerOne: str = input(str("Please enter your gesture:")).lower()

    computer_move = random.choice(my_gestures)

    print("The computer chooses", computer_move)

    if computer_move == "rock" and playerOne == "rock":
        print("Tie!!")

    if computer_move == "paper" and playerOne == "paper":
        print("Tie!!")

    if computer_move == "scissors" and playerOne == "scissors":
        print("Tie!!")

    if computer_move == "lizard" and playerOne == "lizard":
        print("Tie!!")

    if computer_move == "Spock" and playerOne == "Spock":
        print("Tie!!")

    elif computer_move == "paper" and playerOne == "rock" or "Spock":
        print("The computer scores")

        computer_score = computer_score + 1
        print("The computers score is:", computer_score)

    elif computer_move == "rock" and playerOne == "paper" or "Spock":
        print(x + " scores")

        playerOne_score = playerOne_score + 1
        print("Your score is:", playerOne_score)

    elif computer_move == "rock" and playerOne == "scissors" or "lizard":
        print("The computer scores")

        computer_score = int(computer_score) + 1
        print("The computers score is:", computer_score)

    elif computer_move == "scissors" and playerOne == "rock" or "Spock":
        print(x + " scores")

        playerOne_score = playerOne_score + 1
        print("Your score is:", playerOne_score)

    elif computer_move == "paper" and playerOne == "scissors" or "lizard":
        print(x + " scores")

        playerOne_score = playerOne_score + 1
        print("Your score is:", playerOne_score)

    elif computer_move == "scissors" and playerOne == "paper" or "lizard":
        print("The computer scores")

        computer_score = int(computer_score) + 1
        print("The computers score is:", computer_score)

    elif playerOne_score == score_limit:
        print("Congrats! You won!")
    elif computer_score == score_limit:
        print("The computer won, better luck next time")
