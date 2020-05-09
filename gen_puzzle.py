import numpy as np
import random
import math
import tkinter
import time
#Sparro

class Sudoku:

    N = 9
    K = 20
    sqrtN = 3
    puzzle = [[]]
    count = 0

    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.sqrtN = int(math.sqrt(N))
        self.puzzle = [ [0 for i in range(N)] for j in range(N)]
        self.count = 0

    # returns current state of the puzzle
    # @puzzle                   option for a manually entered puzzle instead of object's puzzle
    def get_puzzle(self, puzzle = None):
        if puzzle == None:
            puzzle = self.puzzle
        return puzzle

    """ main function that calls other functions to create the matrix/puzzle """
    # diagonal blocks are filled first because they are independent from each other
    # remaining blocks are solved for using the same function for solving the puzzle later
    # A number K cells are randomly selected and their values removed to allow for solving
    def create_puzzle(self):
        self.fill_diagonal_blocks()

        self.solve_remaining_cells()

        return self.removeKcells()

    # These 3 function fill in diagonal blocks as they are independent from one another
    def fill_diagonal_blocks(self):
        for i in range(0, N, self.sqrtN):
            self.fill_block(i, i)

    # fills in specified diagonal block
    # @row              starting row of diagonal block
    # @col              starting column of diagonal block
    def fill_block(self, row, col):
        for i in range(self.sqrtN):
            for j in range(self.sqrtN):
                num = random.randrange(1, N+1)
                while self.possible_for_block(row, col, num, self.puzzle) is False:
                    num = random.randrange(1, N+1)
                self.puzzle[row+i][col+j] = num

    # checks to see if the random number is already within this block
    # @row              starting row of diagonal block
    # @col              starting column of diagonal block
    # @num              number that is checked for in block
    # @puzzle           option for a manually entered puzzle instead of object's puzzle
    def possible_for_block(self, row, col, num, puzzle):
        for i in range(self.sqrtN):
            for j in range(self.sqrtN):
                if puzzle[row+i][col+j] == num:
                    return False
        return True

    # fills in the remaining blocks recursively and stops after first solve if found
    # @solve_found              if True, a solve has been found and function terminates
    # @real_solve               if True, all possible solutions will be returned; not just first (only used after puzzle is generated)
    # @puzzle                   if None, uses the current object's puzzle;
    #                            otherwise uses puzzle passed in
    def solve_remaining_cells(self, solve_found = False, real_solve = False, puzzle = None):
        if puzzle == None:
            puzzle = self.puzzle
        numlist = list(range(1, N+1))

        for row in range(N):
            for col in range(N):
                if puzzle[row][col] == 0:
                    random.shuffle(numlist)
                    for num in numlist:
                        if self.possible_overall(row, col, num, puzzle):
                            puzzle[row][col] = num
                            solve_found = self.solve_remaining_cells(solve_found, real_solve, puzzle)
                            if solve_found == True and real_solve == False:
                                return solve_found
                            if self.count > 1:
                                return False
                            puzzle[row][col] = 0
                    return
        if real_solve is True:
            self.count += 1
            if self.count > 1:
                return False
        return True

    # finds if the number in this location is allowed for the current puzzle by sudoku rules
    # @row              starting row of diagonal block
    # @col              starting column of diagonal block
    # @num              number that is checked for in block
    # @puzzle           option for a manually entered puzzle instead of object's puzzle
    def possible_overall(self, row, col, num, puzzle):
        # checks row for number
        for i in range(N):
            if puzzle[row][i] == num:
                return False
        # checks col for number
        for i in range(N):
            if puzzle[i][col] == num:
                return False

        x = (col//self.sqrtN)*self.sqrtN
        y = (row//self.sqrtN)*self.sqrtN

        return self.possible_for_block(y, x, num, puzzle)

    # removes K cell values from the puzzle and changes them to 0 to allow for solve
    def removeKcells(self):
        puzzle_to_solve = [ [0 for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                puzzle_to_solve[i][j] = self.puzzle[i][j]
        cells_left = K

        while cells_left != 0:
            for i in range(N):
                for j in range(N):
                    self.puzzle[i][j] = puzzle_to_solve[i][j]
            cell_row = random.randrange(0, N)
            cell_col = random.randrange(0, N)

            if self.puzzle[cell_row][cell_col] != 0:
                self.puzzle[cell_row][cell_col] = 0
                if self.solve_remaining_cells():
                    cells_left -= 1
                    puzzle_to_solve[cell_row][cell_col] = 0

        return puzzle_to_solve


if __name__ == "__main__" :

     start = time.time()
     # Dimensions of NxN sudoku matrix
     N = 9
     # The number of nodes to be removed from puzzle
     K = 50

     # creates puzzle with nodes missing and attempts to then solve it
     sudoku_puzzle = Sudoku(N, K)
     puzzle = sudoku_puzzle.create_puzzle()
     print(np.matrix(puzzle))
     one_solution = sudoku_puzzle.solve_remaining_cells(False, True, puzzle)

     # checks if there is only one solution for the current puzzle
     try_count = 0
     while one_solution is False:
         try_count += 1
         sudoku_puzzle.count = 0  #sets # of solutions to 0 for next check
         # after 20 tries a new puzzle is generated
         if try_count % 50 == 0:
             # checks for a timeout
             if try_count >= 300:
                 print("Timeout: Possibly due to excessive node removal.  Try decreasing K")
                 break
             sudoku_puzzle = Sudoku(N, K)
             puzzle = sudoku_puzzle.create_puzzle()
             print(np.matrix(puzzle))
             one_solution = sudoku_puzzle.solve_remaining_cells(False, True, puzzle)
         # tries to remove a different K nodes from puzzle
         else:
             puzzle = sudoku_puzzle.removeKcells()
             one_solution = sudoku_puzzle.solve_remaining_cells(False, True, puzzle)
         print(one_solution)

     # prints final_puzzle that has only one solution
     if try_count < 300:
        final_puzzle = sudoku_puzzle.get_puzzle()
        print("\nN = "+str(N))
        print("K = "+str(K))
        print("Nodes remaining = "+str(N*N-K))
        print("Puzzle to solve = ")
        print(np.matrix(puzzle))
        print("Final solved puzzle = ")
        print(np.matrix(final_puzzle))

        elapsed_time = (time.time() - start)
        print("Run time: {:.4f} seconds".format(elapsed_time))
