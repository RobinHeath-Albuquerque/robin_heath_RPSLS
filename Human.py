from Players import Players


class Human(Players):

    def make_gesture(self):
        print(self.gestures)


playerOne = Human()

playerOne.make_gesture()
