import numpy as np
import random
import math
import gen_puzzle as gen
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import puzzle_list as pl


if __name__ == "__main__":

    # Dimensions of NxN sudoku matrix
    N = pl.N
    # The number of nodes to be removed from puzzle
    K = pl.K

    """
    # creates puzzle with nodes missing and attempts to then solve it
    sudoku_puzzle = gen.Sudoku(N, K)
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
         sudoku_puzzle = gen.Sudoku(N, K)
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
    """

    puzzle = pl.puzzle
    solution = pl.solution

    # initializes size, title, and tkinter gui itself
    gui = Tk()
    gui.title("Sparro Sudoku")
    gui.geometry("1250x800")

    # validates user input and produces appropriate response
    result_msg = Label(gui)
    def get_value():
        global result_msg
        result_msg.destroy()
        for i in range(N):
            for j in range(N):
                if puzzle[i][j] == 0:
                    if float(user_solution[i][j].get()) != solution[i][j]:
                        result_msg = Label(sub_right, text = "Incorrect. Try again", font = sub_font, bg = "red")
                        result_msg.grid(row=0, column = 0, rowspan = 3)
                        sub_right.config(bg='red')
                        return False
        result_msg = Label(sub_right, text = "You're a genius!", font = sub_font, bg = "green")
        result_msg.grid(row=0, column = 0, rowspan = 3)
        sub_right.config(bg='green')
        return True


    #font and font size
    title_font = tkFont.Font(family= "Courier", size = 40)
    puzzle_font = tkFont.Font(family= "Courier", size = 40)
    puzzle_list_font = tkFont.Font(family= "Courier", size = 20)
    sub_font = tkFont.Font(family= "Courier", size = 20)

    # title bar for Sudoku puzzle
    title_right = Frame(gui, bg = "blue")
    title_right_text = Label(title_right, text = "Sparro Sudoku", font = title_font, bg = "blue")
    title_right_text.pack()

    # menu on left of GUI
    menu_left = Frame(gui, width = 150, height = 150, bg = "red")
    menu_item = Label(menu_left, text = "List of Puzzles Here*", font = puzzle_list_font, bg = "red")
    menu_item.pack()

    # Sudoku puzzle in middle of GUI
    puzzle_area = Canvas(gui, width = 150, height = 200, background = "blue")

    # user solution submission area on right of GUI
    sub_right = Frame(gui, width = 50, height = 150, bg = "orange")
    sub_right_text = Label(sub_right, text = "Sub-Area Here*", font = sub_font, bg = "orange")
    sub_button = Button(sub_right, text = "Submit", height = 2, width = 10, command = get_value)
    sub_right_text.grid(row=0, column = 0, rowspan = 3, sticky = 'e')
    sub_button.grid(row = 3, column = 0, sticky = 'se')
    sub_right.rowconfigure(0, weight=1)

    # deciding how GUI is formatted
    title_right.grid(row=0, column=0, columnspan = 3, sticky='nsew')
    menu_left.grid(row=1, column=0, rowspan=2, sticky='nsew')
    puzzle_area.grid(row=1, column=1, rowspan=2, sticky='nsew')
    sub_right.grid(row=1, column=2, rowspan=2, sticky='nsew')

    # weight to puzzle_area so tkinter knows where to use unallocated space
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_rowconfigure(1, weight=1)
    gui.grid_columnconfigure(1, weight=2)
    gui.grid_columnconfigure(2, weight=1)

    # creates menu of puzzles that will appear in puzzle area upon click
    """for i in range(len(pl.puzzle))
        label = Label(menu_left, text = "Puzzle #"+str(i))"""

    # creates NxN grid with gridlines distributed evenly in the canvas window for puzzle
    idx = 0
    while idx < N:
        puzzle_area.rowconfigure(idx, weight=1)
        puzzle_area.columnconfigure(idx, weight=1)
        ttk.Separator(puzzle_area, orient=VERTICAL).grid(column=idx, row=0, rowspan=N, sticky='nse')
        ttk.Separator(puzzle_area, orient=VERTICAL).grid(column=0, row=idx, columnspan=N, sticky='sew')
        idx += 1

    # inputs puzzle into the canvas window with 0's as available user inputs
    user_solution = [ ['0' for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] != 0:
                label = Label(puzzle_area, text = str(puzzle[i][j]), font = puzzle_font, bg = "blue")
                label.grid(row=i, column=j)
                user_solution[i][j] = label
            else:           # creates user input for the nodes removed by gen_puzzle.py
                entry = Entry(puzzle_area, font = puzzle_font, justify = 'center', width = 2, bg = "blue", bd = 2)
                entry.grid(row=i, column=j)
                user_solution[i][j] = entry

    gui.config(background="black")
    gui.mainloop()
