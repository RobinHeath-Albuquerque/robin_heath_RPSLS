from random import randrange
from unittest import result
from Game import Game, my_gestures
import random

x = input('Please enter your name:')
print('Hello, ' + x + '. Good luck!')

print()

print("Here are the rules:")
print()
print("Rock crushes Scissors")
print("Scissors cuts Paper")
print("Paper covers Rock")
print("Rock crushes Lizard")
print("Lizard poisons Spock")
print("Spock smashes Scissors")
print("Scissors decapitates Lizard")
print("Lizard eats Paper")
print("Paper disproves Spock")
print("Spock vaporizes Rock")
print()
print()

playerOne_score = int(0)
computer_score = int(0)
score_limit = 2

while playerOne_score != score_limit or computer_score != score_limit:
    playerOne_gesture: str = input("Please enter your gesture:")

    computer_gesture = random.choice(my_gestures)
    print('The computer chooses:' + random.choice(my_gestures))


if computer_gesture == 'rock' and playerOne_gesture == 'rock':
    print('Tie!')


