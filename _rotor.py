import random
class _rotor:
    def __init__(self):
        self.offset = 0
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

    def configureRotor(self,offset):
        keys = self.dict.keys()
        values = self.dict.values()

        for x in range(0,offset):
            values.append(values[0])
        rotor = dict(zip(keys,values))
        return rotor

