from Players import Players
import random
from Game import Game, my_gestures


class Computer(Players):

    def __init__(self, choice):
        self.choice = random.choice

    def make_gesture(self):
        print(self.choice)


computer = Computer
