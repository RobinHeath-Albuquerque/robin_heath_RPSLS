from random import randrange
from unittest import result

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


def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print("Error name")


def number_to_name(number):
    if number == 0:
        return 'rock'
    if number == 1:
        return 'Spock'
    if number == 2:
        return 'paper'
    if number == 3:
        return 'lizard'
    if number == 4:
        return 'scissors'
    else:
        print("Error number")


def rpsls(player_choice):
    print()
    print(x + ' chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print()
    print('Computer chooses ' + comp_choice)
    difference = (comp_number - player_number) % 5
    if difference == 1 or difference == 2:
        print('Computer Wins!')
    elif difference == 4 or difference == 3:
        print(x + ' wins!')
    elif difference == 0:
        print(x + ' computer tie!')
