from random import randrange
from unittest import result
from Game import Game, my_rules, my_gestures


import random


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
score_limit = 2
while playerOne_score != score_limit or computer_score != score_limit:
    playerOne_gesture: str = input("Please enter your gesture:")

    computer_gesture = random.choice(my_gestures)
    print('The computer chooses:' + random.choice(my_gestures))


