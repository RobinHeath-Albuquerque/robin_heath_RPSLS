from random import randrange, random


class Game:
    def __init__(self, gestures, rules,):
        self.name = ()
        self.gestures = my_gestures
        self.rules = my_rules


my_gestures = ['rock', 'Spock', 'paper', 'lizard', 'scissors']


my_rules = ['Rock crushes Scissors' 'Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons '
                                                                                                       'Spock',
            'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock',
            'Spock vaporizes Rock']


def result(winner_result, player_choice, computer_choice, win=2, lose=2, tie=None):

    # accumulate the appropriate winner of game total
    if result == 'win':
        win += 1
    elif result == 'lose':
        lose += 1
    else:
        tie += 1
    return result
