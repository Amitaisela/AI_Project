from random import shuffle


class Node:
    def __init__(self, data, level, fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x, y = self.find(self.data, '_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        """ Specifically used to find the position of the blank space """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size=3):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal, h):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return h(start.data, goal, self.n)+start.level

    def generate_legal_puzzle(self):
        while True:
            cells = []
            numbers = list(range(0, self.n*self.n))
            shuffle(numbers)

            for row in range(3):
                cells.append([])
                for col in range(3):
                    cells[row].append(numbers.pop())
                    if cells[row][col] == 0:
                        blankCell = row, col

            if self.isSolvable(cells):
                # replace 0 with '_'
                for row in range(3):
                    for col in range(3):
                        if cells[row][col] == 0:
                            cells[row][col] = '_'
                return cells

    def isSolvable(self, cells):
        """Checks if the 8-puzzle is actually solvable, by
        checking the number of inversions in the input state.
        """
        array = str(cells)
        deleted = str.maketrans(dict.fromkeys("[,]"))
        array = array.translate(deleted)
        array = array.split(" ")
        array = [int(num) for num in array]
        print(array)

        inversions = 0
        x = 0
        while x < 8:
            if (array[x] != 0):
                y = x+1
                while y < 9:
                    if (array[y] != 0):
                        if (array[x] > array[y]):
                            inversions += 1
                    y += 1
            x += 1

        if (inversions % 2) == 1:
            print(inversions)
            return False
        else:
            print(inversions)
            return True

    def process(self, h):
        """ Accept Start and Goal Puzzle state"""
        start = self.generate_legal_puzzle()
        start = [['_', 5, 8], [4, 7, 2], [9, 1, 3]]
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

        print("Start")
        for i in start:
            for j in i:
                print(j, end=" ")
            print("")
        print("Goal")
        for i in goal:
            for j in i:
                print(j, end=" ")
            print("")

        return self.Astar(start, goal, h)

    def Astar(self, start, goal, h):
        pass


def h(start, goal, n):
    temp = 0
    for i in range(0, n):
        for j in range(0, n):
            if start[i][j] != goal[i][j] and start[i][j] != '_':
                temp += 1
    return temp


puz = Puzzle()
cur, steps, opened = puz.process(h)

print("Steps:", steps)
print("Opened:", opened)
print("Path:")
for i in cur.data:
    for j in i:
        print(j, end=" ")
    print("")
