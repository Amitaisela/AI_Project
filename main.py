from eightPuzzle import *


def main():
    # Create the puzzle
    puzzle = EightPuzzle()

    if not puzzle.isSolvable():
        print("Puzzle is not solvable.")


if __name__ == "__main__":
    main()
