from random import randint
from Game import Game, my_rules, my_gestures
from Computer import Computer, computer


x = input('Please enter your name:')
print('Hello, ' + x + '. Good luck!')
print()
print('Here are the rules:')
for x in my_rules:
    print(x)
print()
print('The best of 3 will win the game!')
print()

computer_gesture = my_gestures[randint(0, 4)]
playerOne = False

while playerOne == False:
    playerOne = input("Please enter your gesture:")
print("Computer Chooses " + my_gestures[randint(0, 4)])
if playerOne == computer_gesture:
    print("Tie!")
elif playerOne == "rock":
    if computer_gesture == "paper" or "spock":
        print("Computer Wins!")
    else:
        print(x + "Wins!")
elif playerOne == "paper":
    if computer_gesture == "lizard" or "scissors":
        print("Computer Wins!")
    else:
        print(x + "Wins!")
elif playerOne == "scissors":
    if computer_gesture == "rock" or "spock":
        print("Computer Wins!")
    else:
        print(x + "Wins!")
elif playerOne == "lizard":
    if computer_gesture == "rock" or "scissors":
        print("Computer Wins!")
    else:
        print(x + "Wins!")
elif playerOne == "Spock":
    if computer_gesture == "paper" or "lizard":
        print("Computer Wins!")
    else:
        print(x + "Wins!")
else:
    print("Please enter a valid gesture!")

playerOne_score = int(0)
computer_score = int(0)
score_limit = 5
