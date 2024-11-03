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

def rta_star(start_state, max_iterations=100):
    current_state = start_state
    path = []

    for _ in range(max_iterations):
        if current_state.is_goal():
            return path
        
        # Get all neighbors and sort by heuristic cost (Manhattan distance)
        neighbors = current_state.get_neighbors()
        neighbors.sort(key=lambda s: s.manhattan_distance())

        # Select the best neighbor
        best_neighbor = neighbors[0]

        # Add the best move to the path
        path.append(best_neighbor)
        
        # Move to the best neighbor
        current_state = best_neighbor

    return None  # No solution found within the iteration limit

# Example usage
if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    start_state = PuzzleState(initial_board)

    print("Initial State:")
    print(start_state)

    algorithm = input("Choose an algorithm (A* / RTA*): ").strip().lower()

    if algorithm == "a*":
        print("\nA* Solution Path:")
        path = a_star(start_state)
        if path:
            for step in path:
                print(step)
                print("------")
        else:
            print("No solution found.")
    
    elif algorithm == "rta*":
        print("\nRTA* Solution Path:")
        path = rta_star(start_state)
        if path:
            for step in path:
                print(step)
                print("------")
        else:
            print("No solution found.")
    
    else:
        print("Invalid algorithm choice. Please choose either 'A*' or 'RTA*'.")
