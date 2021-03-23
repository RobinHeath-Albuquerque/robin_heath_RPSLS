import RPSLS

from Players import Players

from Lizard import Lizard

from Spock import Spock

from Paper import Paper

from Scissors import Scissors

from Rock import Rock

if __name__ == '__main__':

    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "spock"}

    win_lose_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 3, -1, 3], [4, 1, 4, 3, -1]]
    



