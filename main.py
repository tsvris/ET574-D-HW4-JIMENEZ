import random

class Reel:
    def __init__(self, max_value=9):
        self.max_value = max_value

    def spin(self):
        return random.randint(0, self.max_value)
class SlotMachine:
    def __init__(self):
        self.reel1 = Reel()
        self.reel2 = Reel()
        self.reel3 = Reel()