import time
import random
from queue import PriorityQueue

from Heuristic import Heuristic
from generate import generate_solvable_8_puzzles


COL = 3


class Node:
    def __init__(self, p):
        self.children = []
        self.parent = None
        self.puzzle = p[:]
        self.x = 0
        self.g = self.h = float('inf')

    def printPuzzle(self):
        print()
        m = 0
        for i in range(COL):
            for j in range(COL):
                print(self.puzzle[m], end=" ")
                m += 1
            print()

    def movetoright(self):
        if ((self.x) % COL < (COL-1)):
            pc = self.puzzle[:]
            pc[self.x], pc[self.x+1] = pc[self.x+1], pc[self.x]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def movetoleft(self):
        if ((self.x) % COL > 0):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) - 1] = pc[(self.x) - 1], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def moveup(self):
        if ((self.x) - 3 > 0):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) - 3] = pc[(self.x) - 3], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def movedown(self):
        if ((self.x) + 3 < 9):
            pc = self.puzzle[:]
            pc[(self.x)], pc[(self.x) + 3] = pc[(self.x) + 3], pc[(self.x)]
            child = Node(pc)
            self.children.append(child)
            child.parent = self

    def goaltest(self):
        isGoal = True
        for i in range(len(self.puzzle)):
            if i != self.puzzle[i]:
                isGoal = False
                return isGoal
        return isGoal

    def expandNode(self):
        for i in range(len(self.puzzle)):
            if self.puzzle[i] == 0:
                self.x = i
        self.movetoright()
        self.movedown()
        self.movetoleft()
        self.moveup()


class search:
    def __init__(self):
        pass

    def breadthFirstSearch(self, root):
        openlist = []
        visited = set()
        openlist.append(root)
        visited.add(tuple(root.puzzle))
        while (True):
            currentNode = openlist.pop(0)
            if currentNode.goaltest():
                pathtosolution = search.pathtrace(currentNode)
                return pathtosolution
            currentNode.expandNode()
            for i in range(len(currentNode.children)):
                currentchild = currentNode.children[i]
                if (not (tuple(currentchild.puzzle) in visited)):
                    openlist.append(currentchild)
                    visited.add(tuple(currentchild.puzzle))

    def pathtrace(n):
        current = n
        path = []
        path.append(current)
        while current.parent != None:
            current = current.parent
            path.append(current)
        return path


if __name__ == "__main__":
    # All_puzzles = generate_solvable_8_puzzles()
    All_puzzles = [[1, 2, 3, 4, 5, 6, 0, 7, 8]]

    for puzzle in All_puzzles:
        root = Node(puzzle)

        s = search()
        solution = s.breadthFirstSearch(root)

        # solution.reverse()
        # for i in range(len(solution)):
        #     solution[i].printPuzzle()

        print("No of steps required to solve the puzzle", len(solution)-1)
