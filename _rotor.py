#!/usr/bin/env python3
from collections import deque


class rotor:
    def __init__(self):
        self.offset = 0
        self.mapping = {
                        'A' : 'A',
                        'B' : 'B',
                        'C' : 'C',
                        'D' : 'D',
                        'E' : 'E',
                        'F' : 'F',
                        'G' : 'G',
                        'H' : 'H',
                        'I' : 'I',
                        'J' : 'J',
                        'K' : 'K',
                        'L' : 'L',
                        'M' : 'M',
                        'N' : 'N',
                        'O' : 'O',
                        'P' : 'P',
                        'Q' : 'Q',
                        'R' : 'R',
                        'S' : 'S',
                        'T' : 'T',
                        'U' : 'U',
                        'V' : 'V',
                        'W' : 'W',
                        'X' : 'X',
                        'Y' : 'Y',
                        'Z' : 'Z',
                        'a' : 'a',
                        'b' : 'b',
                        'c' : 'c',
                        'd' : 'd',
                        'e' : 'e',
                        'f' : 'f',
                        'g' : 'g',
                        'h' : 'h',
                        'i' : 'i',
                        'j' : 'j',
                        'k' : 'k',
                        'l' : 'l',
                        'm' : 'm',
                        'n' : 'n',
                        'o' : 'o',
                        'p' : 'p',
                        'q' : 'q',
                        'r' : 'r',
                        's' : 's',
                        't' : 't',
                        'u' : 'u',
                        'v' : 'v',
                        'w' : 'w',
                        'x' : 'x',
                        'y' : 'y',
                        'z' : 'z',
                        '1' : '1',
                        '2' : '2',
                        '3' : '3',
                        '4' : '4',
                        '5' : '5',
                        '6' : '6',
                        '7' : '7',
                        '8' : '8',
                        '9' : '9',
                        '0' : '0',
                        '~' : '~',
                        '!' : '!',
                        '@' : '@',
                        '#' : '#',
                        '$' : '$',
                        '%' : '%',
                        '^' : '^',
                        '&' : '&',
                        '*' : '*',
                        '(' : '(',
                        ')' : ')',
                        '-' : '-',
                        '_' : '_',
                        '=' : '=',
                        '+' : '+',
                        '[' : '[',
                        '{' : '{',
                        ']' : ']',
                        '}' : '}',
                        '|' : '|',
                        ';' : ';',
                        ':' : ':',
                        ',' : ',',
                        '<' : '<',
                        '.' : '.',
                        '>' : '>',
                        '/' : '/',
                        '?' : '?',
                        ' ' : ' '
                    }

    def configureEncoderRotor(self, offset):
        keys = deque(self.mapping.keys())
        values = deque(self.mapping.values())

        values.rotate(offset)

        self.mapping = dict(zip(keys,values))

    def configureDecoderRotor(self,offset):
        keys = deque(self.mapping.keys())
        values = deque(self.mapping.values())

        values.rotate(offset)

        self.mapping = dict(zip(values,keys))

    def rotorStepForward(self):
        keys = deque(self.mapping.keys())
        values = deque(self.mapping.values())

        values.rotate(1)

        self.mapping = dict(zip(keys,values))

    def rotorStepBackward(self):
        keys = deque(self.mapping.keys())
        values = deque(self.mapping.values())

        values.rotate(-1)

        self.mapping = dict(zip(keys,values))

