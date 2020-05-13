# List of Puzzles for user to choose from

# Dimensions of NxN sudoku matrix
N = 9
# The number of nodes to be removed from puzzle
K = 50

#sample puzzle
puzzle = [ [0 for i in range(N)] for j in range(N) ]
puzzle = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
          [2, 7, 1, 3, 5, 8, 4, 9, 6],
          [4, 5, 9, 1, 7, 6, 8, 3, 2],
          [6, 8, 4, 9, 1, 7, 5, 2, 3],
          [9, 2, 7, 5, 4, 3, 6, 1, 8],
          [1, 3, 5, 6, 8, 2, 9, 4, 7],
          [5, 9, 2, 7, 6, 1, 3, 8, 4],
          [8, 4, 6, 2, 3, 5, 1, 7, 9],
          [7, 1, 3, 8, 9, 4, 2, 0, 0]]

# sample solution
solution = [[3, 6, 8, 4, 2, 9, 7, 5, 1],
            [2, 7, 1, 3, 5, 8, 4, 9, 6],
            [4, 5, 9, 1, 7, 6, 8, 3, 2],
            [6, 8, 4, 9, 1, 7, 5, 2, 3],
            [9, 2, 7, 5, 4, 3, 6, 1, 8],
            [1, 3, 5, 6, 8, 2, 9, 4, 7],
            [5, 9, 2, 7, 6, 1, 3, 8, 4],
            [8, 4, 6, 2, 3, 5, 1, 7, 9],
            [7, 1, 3, 8, 9, 4, 2, 6, 5]]
