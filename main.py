import RPSLS

from Game import Game
from Players import Players

from Lizard import Lizard

from Spock import Spock

from Paper import Paper

from Scissors import Scissors

from Rock import Rock

if __name__ == '__main__':
    game = Game()
    game.run_game()

RPSLS.rpsls("rock")
RPSLS.rpsls("Spock")
RPSLS.rpsls("paper")
RPSLS.rpsls("lizard")
RPSLS.rpsls("scissors")

