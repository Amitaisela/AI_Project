# import math

# class Node:
#     def __init__(self, state, parent=None, g=0, h=0):
#         self.state = state       # (x, y) coordinates in the grid
#         self.parent = parent     # Parent node (to track the path)
#         self.g = g               # Cost to reach this node from start
#         self.h = h               # Heuristic (estimated cost to goal)

#     def f(self):
#         return self.g + self.h   # f(n) = g(n) + h(n)

# def heuristic(node, goal):
#     """Manhattan distance heuristic for a grid."""
#     (x1, y1) = node.state
#     (x2, y2) = goal
#     return abs(x1 - x2) + abs(y1 - y2)

# def get_neighbors(node, grid_size=5):
#     """Return the valid neighboring nodes of the given node."""
#     (x, y) = node.state
#     neighbors = []

#     # Possible moves (up, down, left, right)
#     possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

#     # Only return valid moves within the grid bounds
#     for (nx, ny) in possible_moves:
#         if 0 <= nx < grid_size and 0 <= ny < grid_size:  # Ensure move is within bounds
#             neighbors.append(Node((nx, ny)))

#     return neighbors

# def rta_star(start, goal, max_depth=1, grid_size=5):
#     """Real-Time A* search algorithm in a grid world."""
#     current = Node(start, h=heuristic(Node(start), goal))

#     while current.state != goal:
#         print(f"Current node: {current.state}")

#         # Get neighbors and evaluate their heuristic values
#         neighbors = get_neighbors(current, grid_size)
#         if not neighbors:
#             return None  # No path found

#         # For each neighbor, calculate g(n) and h(n)
#         for neighbor in neighbors:
#             neighbor.g = current.g + 1  # Assume each move has a cost of 1
#             neighbor.h = heuristic(neighbor, goal)

#         # Choose the best neighbor based on f(n) = g(n) + h(n)
#         best_neighbor = min(neighbors, key=lambda n: n.f())

#         # If the best neighbor has a better f(n), move to that node
#         if best_neighbor.f() < current.f():
#             current = best_neighbor
#         else:
#             # Otherwise, update the heuristic of the current node and stay
#             current.h = best_neighbor.f()

#     return current  # Goal reached

# # Example usage
# start = (1, 1)  # Starting position in the grid (top-left corner)
# goal = (4, 4)   # Goal position in the grid (bottom-right corner)

# result = rta_star(start, goal, grid_size=5)

# if result:
#     print(f"Goal reached at {result.state}!")
# else:
#     print("No path found.")

import math


class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state       # (x, y) coordinates in the grid
        self.parent = parent     # Parent node (to track the path)
        self.g = g               # Cost to reach this node from start
        self.h = h               # Heuristic (estimated cost to goal)

    def f(self):
        return self.g + self.h   # f(n) = g(n) + h(n)


def heuristic(node, goal):
    """Manhattan distance heuristic for a grid."""
    (x1, y1) = node.state
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)


def get_neighbors(node, grid_size=5):
    """Return the valid neighboring nodes of the given node."""
    (x, y) = node.state
    neighbors = []

    # Possible moves (up, down, left, right)
    possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    # Only return valid moves within the grid bounds
    for (nx, ny) in possible_moves:
        if 0 <= nx < grid_size and 0 <= ny < grid_size:  # Ensure move is within bounds
            neighbors.append(Node((nx, ny)))

    return neighbors


def rta_star(start, goal, max_depth=1, grid_size=5):
    """Real-Time A* search algorithm in a grid world."""
    current = Node(start, h=heuristic(Node(start), goal))

    while current.state != goal:
        print(f"Current node: {current.state}")

        # Get neighbors and evaluate their heuristic values
        neighbors = get_neighbors(current, grid_size)
        if not neighbors:
            return None  # No path found

        # For each neighbor, calculate g(n) and h(n)
        for neighbor in neighbors:
            neighbor.g = current.g + 1  # Assume each move has a cost of 1
            neighbor.h = heuristic(neighbor, goal)

        # Choose the best neighbor based on f(n) = g(n) + h(n)
        best_neighbor = min(neighbors, key=lambda n: n.f())

        # If the best neighbor has a better or equal f(n), move to that node
        if best_neighbor.f() < current.f():
            current = best_neighbor
        else:
            # Update the heuristic of the current node
            current.h = best_neighbor.f()
            # Move to the best neighbor even if its f(n) is not better
            current = best_neighbor

    return current  # Goal reached


# Example usage
start = (0, 0)  # Starting position in the grid (top-left corner)
goal = (4, 4)   # Goal position in the grid (bottom-right corner)

result = rta_star(start, goal, grid_size=5)

if result:
    print(f"Goal reached at {result.state}!")
else:
    print("No path found.")
