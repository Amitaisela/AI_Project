import Puzzle


class Search:
    def __init__(self):
        pass

    def breadthFirstSearch(self, Puzzle: Puzzle):
        pass
        # finish

    def astar(self, Puzzle: Puzzle, huristic):
        pass
        # finish

    def rta_start(self, Puzzle: Puzzle, huristic):
        pass
        # finish

    def pathtrace(n):
        pass
        # finish

    def find_root(self, Puzzle: Puzzle):
        for i in range(Puzzle.grid):
            for j in range(Puzzle.grid):
                if Puzzle.cells[i * Puzzle.grid + j].value == 0:
                    return [i, j]
