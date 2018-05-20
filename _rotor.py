import random
class _rotor:
    def __init__(self,offset):
        self.offset = random.randint(1,24)
        self.dict = {
                        "A" : "A",
                        "B" : "B",
                        "C" : "C",
                        "D" : "D",
                        "E" : "E",
                        "F" : "F",
                        "G" : "G",
                        "H" : "H",
                        "I" : "I",
                        "J" : "J",
                        "K" : "K",
                        "L" : "L",
                        "M" : "M",
                        "N" : "N",
                        "O" : "O",
                        "P" : "P",
                        "Q" : "Q",
                        "R" : "R",
                        "S" : "S",
                        "T" : "T",
                        "U" : "U",
                        "V" : "V",
                        "W" : "W",
                        "X" : "X",
                        "Y" : "Y",
                        "Z" : "Z"
        }

    def configureRotor(self):
        keys = self.dict.keys()
        values = self.dict.values()


