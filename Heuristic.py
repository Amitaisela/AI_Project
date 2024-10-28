from math import sqrt
import numpy as np


class Heuristic:
    # euclidian distance
    @staticmethod
    def euclidean(node, goal):
        return sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

    # manhattan distance
    @staticmethod
    def manhattan(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    @staticmethod
    def optimistic_pessimistic(node, goal, huristic, c, mu, sigma):
        """return a value that is a combination of the huristic value and a random noise
            c is used to determine if optimistic or pessimistic huristic is used
        """
        # not final, a placeholder for now
        noise = np.random.normal(mu, sigma)
        return c * (huristic(node, goal) + noise)

    @staticmethod
    def Linear_Conflict(node, goal):
        pass

    @staticmethod
    def Misplaced_Tiles(node, goal):
        pass

    @staticmethod
    def Relaxed_Adjancey(node, goal):
        pass
