import numpy as np

# List of Puzzles for user to choose from

# Dimensions of NxN sudoku matrix
N = 9
# The number of nodes to be removed from puzzle
K = 50

num_of_puzzles = 22

# set up array of puzzles and solutions
puzzles = [ [0 for i in range(N)] for j in range(N) for k in range(num_of_puzzles) ]
solutions = [ [0 for i in range(N)] for j in range(N) for k in range(num_of_puzzles) ]

# sample puzzle and solution
puzzles[0] = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
              [2, 7, 1, 3, 5, 8, 4, 9, 6],
              [4, 5, 9, 1, 7, 6, 8, 3, 2],
              [6, 8, 4, 9, 1, 7, 5, 2, 3],
              [9, 2, 7, 5, 4, 3, 6, 1, 8],
              [1, 3, 5, 6, 8, 2, 9, 4, 7],
              [5, 9, 2, 7, 6, 1, 3, 8, 4],
              [8, 4, 6, 2, 3, 5, 1, 7, 9],
              [7, 1, 3, 8, 9, 4, 2, 0, 0]]

# sample solution
solutions[0] = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
                [2, 7, 1, 3, 5, 8, 4, 9, 6],
                [4, 5, 9, 1, 7, 6, 8, 3, 2],
                [6, 8, 4, 9, 1, 7, 5, 2, 3],
                [9, 2, 7, 5, 4, 3, 6, 1, 8],
                [1, 3, 5, 6, 8, 2, 9, 4, 7],
                [5, 9, 2, 7, 6, 1, 3, 8, 4],
                [8, 4, 6, 2, 3, 5, 1, 7, 9],
                [7, 1, 3, 8, 9, 4, 2, 6, 5]]

puzzles[1] = [[0, 6, 8, 4, 2, 9, 7, 5, 1],
              [2, 0, 1, 3, 5, 8, 4, 9, 6],
              [4, 5, 0, 1, 7, 6, 8, 3, 2],
              [6, 8, 4, 0, 1, 7, 5, 2, 3],
              [9, 2, 7, 5, 0, 3, 6, 1, 8],
              [1, 3, 5, 6, 8, 0, 9, 4, 7],
              [5, 9, 2, 7, 6, 1, 0, 8, 4],
              [8, 4, 6, 2, 3, 5, 1, 0, 9],
              [7, 1, 3, 8, 9, 4, 2, 6, 0]]

solutions[1] = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
                [2, 7, 1, 3, 5, 8, 4, 9, 6],
                [4, 5, 9, 1, 7, 6, 8, 3, 2],
                [6, 8, 4, 9, 1, 7, 5, 2, 3],
                [9, 2, 7, 5, 4, 3, 6, 1, 8],
                [1, 3, 5, 6, 8, 2, 9, 4, 7],
                [5, 9, 2, 7, 6, 1, 3, 8, 4],
                [8, 4, 6, 2, 3, 5, 1, 7, 9],
                [7, 1, 3, 8, 9, 4, 2, 6, 5]]

puzzles[2] = [[3, 6, 8, 4, 2, 9, 7, 5, 0],
              [2, 7, 1, 3, 5, 8, 4, 0, 6],
              [4, 5, 9, 1, 7, 6, 0, 3, 2],
              [6, 8, 4, 9, 1, 0, 5, 2, 3],
              [9, 2, 7, 5, 0, 3, 6, 1, 8],
              [1, 3, 5, 0, 8, 2, 9, 4, 7],
              [5, 9, 0, 7, 6, 1, 3, 8, 4],
              [8, 0, 6, 2, 3, 5, 1, 7, 9],
              [0, 1, 3, 8, 9, 4, 2, 6, 5]]

solutions[2] = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
                [2, 7, 1, 3, 5, 8, 4, 9, 6],
                [4, 5, 9, 1, 7, 6, 8, 3, 2],
                [6, 8, 4, 9, 1, 7, 5, 2, 3],
                [9, 2, 7, 5, 4, 3, 6, 1, 8],
                [1, 3, 5, 6, 8, 2, 9, 4, 7],
                [5, 9, 2, 7, 6, 1, 3, 8, 4],
                [8, 4, 6, 2, 3, 5, 1, 7, 9],
                [7, 1, 3, 8, 9, 4, 2, 6, 5]]
