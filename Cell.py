import numpy as np


class Cell:
    def __init__(self, value, cords=(-1, -1)):
        self.value = value
        self.children = []
        self.parent = None
        self.cords = cords
        self.g = self.h = float('inf')

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

    def __eq__(self, other):
        return self.value == other.value
