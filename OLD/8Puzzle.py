# class PuzzleState:
#     def __init__(self, board):
#         # Ensure the board is a list of 9 elements
#         assert len(board) == 9, "Board must have exactly 9 elements."
#         self.board = board

#     def __repr__(self):
#         # Display the board in a 3x3 format
#         return "\n".join([
#             f"{self.board[0:3]}",
#             f"{self.board[3:6]}",
#             f"{self.board[6:9]}"
#         ])

#     # Helper to find the index of the empty tile
#     def get_empty_index(self):
#         return self.board.index(0)

#     # Function to generate new states based on possible moves
#     def get_neighbors(self):
#         neighbors = []
#         empty_index = self.get_empty_index()
        
#         # Possible moves based on empty_index
#         moves = {
#             'up': empty_index - 3,
#             'down': empty_index + 3,
#             'left': empty_index - 1 if empty_index % 3 != 0 else -1,
#             'right': empty_index + 1 if (empty_index + 1) % 3 != 0 else -1
#         }
        
#         # Execute valid moves
#         for direction, new_index in moves.items():
#             if 0 <= new_index < 9:
#                 new_board = self.board[:]
#                 new_board[empty_index], new_board[new_index] = new_board[new_index], new_board[empty_index]
#                 neighbors.append(PuzzleState(new_board))
        
#         return neighbors


# # Define the goal state for the puzzle
# GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# # Example usage
# if __name__ == "__main__":
#     # Example initial state
#     initial_board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
#     initial_state = PuzzleState(initial_board)

#     print("Initial State:")
#     print(initial_state)
#     print("\nNeighbors:")
#     for neighbor in initial_state.get_neighbors():
#         print(neighbor)
#         print("------")



import heapq

class PuzzleState:
    def __init__(self, board, g_cost=0, parent=None):
        assert len(board) == 9, "Board must have exactly 9 elements."
        self.board = board
        self.g_cost = g_cost  # Cost from the start node
        self.parent = parent  # Pointer to parent state for path reconstruction

    def __repr__(self):
        return "\n".join([
            f"{self.board[0:3]}",
            f"{self.board[3:6]}",
            f"{self.board[6:9]}"
        ])

    def __lt__(self, other):
        # Required for priority queue ordering by f(n) = g(n) + h(n)
        return (self.g_cost + self.manhattan_distance()) < (other.g_cost + other.manhattan_distance())

    def get_empty_index(self):
        return self.board.index(0)

    def get_neighbors(self):
        neighbors = []
        empty_index = self.get_empty_index()
        moves = {
            'up': empty_index - 3,
            'down': empty_index + 3,
            'left': empty_index - 1 if empty_index % 3 != 0 else -1,
            'right': empty_index + 1 if (empty_index + 1) % 3 != 0 else -1
        }
        for direction, new_index in moves.items():
            if 0 <= new_index < 9:
                new_board = self.board[:]
                new_board[empty_index], new_board[new_index] = new_board[new_index], new_board[empty_index]
                neighbors.append(PuzzleState(new_board, self.g_cost + 1, self))
        return neighbors

    def manhattan_distance(self):
        # Calculates the Manhattan Distance heuristic
        distance = 0
        for i, tile in enumerate(self.board):
            if tile != 0:  # Don't calculate for the empty tile
                target_x, target_y = divmod(GOAL_STATE.index(tile), 3)
                current_x, current_y = divmod(i, 3)
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def is_goal(self):
        return self.board == GOAL_STATE

GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def a_star(start_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (start_state.g_cost + start_state.manhattan_distance(), start_state))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.is_goal():
            return reconstruct_path(current)

        closed_set.add(tuple(current.board))

        for neighbor in current.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue

            f_cost = neighbor.g_cost + neighbor.manhattan_distance()
            heapq.heappush(open_list, (f_cost, neighbor))

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return path[::-1]

# Example usage
if __name__ == "__main__":
    initial_board = [8, 7, 4, 1, 2, 0, 3, 5, 6]
    start_state = PuzzleState(initial_board)

    print("Initial State:")
    print(start_state)

    path = a_star(start_state)
    if path:
        print("\nSolution Path:")
        for step in path:
            print(step)
            print("------")
    else:
        print("No solution found.")
