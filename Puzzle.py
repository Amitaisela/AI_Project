import Cell


class Puzzle:
    def __init__(self, initial_state: list[int], grid=3, goal=[1, 2, 3, 4, 5, 6, 7, 8, 0]):
        self.initial_state = initial_state
        self.grid = grid
        self.goal = goal
        self.cells = self.initial_cells()

    def initial_cells(self):
        cells = []
        for i in range(self.grid):
            for j in range(self.grid):
                cell = Cell.Cell(i, j)
                cell.value = self.initial_state[i * self.grid + j]
                cells.append(cell)
        return cells

    def print_puzzle(self):
        for i in range(self.grid):
            for j in range(self.grid):
                print(self.cells[i * self.grid + j].value, end=' ')
            print()

    def is_goal(self):
        for i in range(self.grid):
            for j in range(self.grid):
                if self.cells[i * self.grid + j].value != self.goal[i * self.grid + j]:
                    return False
        return True
