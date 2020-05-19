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

    # default puzzle, solution, and user_solution
    puzzle = pl.puzzles[0]
    solution = pl.solutions[0]
    user_solution = [ ['0' for i in range(N)] for j in range(N)]

    # initializes size, title, and tkinter gui itself
    gui = Tk()
    gui.title("Sparro Sudoku")
    gui.geometry("1250x800")

    # inputs puzzle into the canvas window with 0's as available user inputs
    puzzle_area = Canvas(gui)
    result_msg = Label(gui)
    solution_area = Canvas(gui)
    def create_puzzle(puzzle):
        global puzzle_area, result_msg, solution_area
        result_msg.destroy()
        puzzle_area.destroy()
        solution_area.destroy()

        # Sudoku puzzle in middle of GUI
        puzzle_area = Canvas(gui, width = 150, height = 200, background = "blue")
        puzzle_area.grid(row=1, column=1, rowspan=2, sticky='nsew')

        # creates NxN grid with gridlines distributed evenly in the canvas window for puzzle
        idx = 0
        while idx < N:
            puzzle_area.rowconfigure(idx, weight=1)
            puzzle_area.columnconfigure(idx, weight=1)
            ttk.Separator(puzzle_area, orient=VERTICAL).grid(column=idx, row=0, rowspan=N, sticky='nse')
            ttk.Separator(puzzle_area, orient=VERTICAL).grid(column=0, row=idx, columnspan=N, sticky='sew')
            idx += 1

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

    # validates user input and produces appropriate response
    def get_value():
        global result_msg, puzzle, user_solution
        result_msg.destroy()
        solution_area.destroy()
        for i in range(N):
            for j in range(N):
                if puzzle[i][j] == 0:
                    if float(user_solution[i][j].get()) != solution[i][j]:
                        result_msg = Label(sub_right, text = "Incorrect. Try again", font = sub_font, bg = "red")
                        result_msg.place(relx = 0.5, rely = 0.5, anchor=CENTER)
                        sub_right.config(bg='red')
                        return False
        result_msg = Label(sub_right, text = "You're a genius!", font = sub_font, bg = "green")
        result_msg.place(relx = 0.5, rely = 0.5, anchor=CENTER)
        sub_right.config(bg='green')
        return True


    # allows user to choose a puzzle by clicking on a specific puzzle label
    def choose_puzzle(event, i):
        puzzle = pl.puzzles[i]
        solution = pl.solutions[i]
        create_puzzle(puzzle)

    # shows the answer of the puzzle to the user
    def show_answer():
        global puzzle, solution

        # Sudoku puzzle in sub_area
        solution_area = Canvas(sub_right, width = 100, height = 100, background = "blue")
        solution_title = Label(sub_right, text = "Puzzle Solution:", font = solution_title_font, bg = "red")
        solution_title.place(relx = 0.5, rely = 0.02, anchor=CENTER)
        solution_area.place(relx = 0.5, rely = 0.28, anchor=CENTER)

        # creates NxN grid with gridlines distributed evenly in the canvas window for puzzle
        idx = 0
        while idx < N:
            solution_area.rowconfigure(idx, weight=1)
            solution_area.columnconfigure(idx, weight=1)
            ttk.Separator(solution_area, orient=VERTICAL).grid(column=idx, row=0, rowspan=N, sticky='nse')
            ttk.Separator(solution_area, orient=VERTICAL).grid(column=0, row=idx, columnspan=N, sticky='sew')
            idx += 1

        for i in range(N):
            for j in range(N):
                if puzzle[i][j] == 0:
                    label = Label(solution_area, text = str(solution[i][j]), font = solution_font, bg = "orange")
                    label.grid(row=i, column=j)
                else:
                    label = Label(solution_area, text = str(solution[i][j]), font = solution_font, bg = "blue")
                    label.grid(row=i, column=j)

    #font and font size
    title_font = tkFont.Font(family= "Courier", size = 40)
    puzzle_font = tkFont.Font(family= "Courier", size = 40)
    solution_title_font = tkFont.Font(family="Courier", size = 20)
    solution_font = tkFont.Font(family="Courier", size = 28)
    puzzle_list_title_font = tkFont.Font(family="Courier", size = 28)
    puzzle_list_category_font = tkFont.Font(family="Courier bold", size = 22)
    puzzle_list_font = tkFont.Font(family= "Courier", size = 18)
    sub_font = tkFont.Font(family= "Courier", size = 20)

    # title bar for Sudoku puzzle
    title_right = Frame(gui, bg = "blue")
    title_right_text = Label(title_right, text = "Sparro Sudoku", font = title_font, bg = "blue")
    title_right_text.pack()

    # menu on left of GUI
    menu_left = Frame(gui, width = 150, height = 150, bg = "red")
    menu_title = Label(menu_left, text = "Choose a puzzle:", font = puzzle_list_title_font, bg = "red")
    menu_easy_title = Label(menu_left, text = "Easy", font = puzzle_list_category_font, bg = "red")
    menu_medium_title = Label(menu_left, text = "Medium", font = puzzle_list_category_font, bg = "red")
    menu_hard_title = Label(menu_left, text = "Hard", font = puzzle_list_category_font, bg = "red")
    menu_title.pack()

    # user solution submission area on right of GUI
    sub_right = Frame(gui, width = 200, height = 150, bg = "orange")
    sub_button = Button(sub_right, text = "Submit", height = 2, width = 10, command = get_value)
    sub_show_answer = Button(sub_right, text = "Show Answer", height = 2, width = 10, command = show_answer)
    sub_button.place(relx = 0.18, rely = 0.98, anchor = CENTER)
    sub_show_answer.place(relx = 0.82, rely = 0.98, anchor = CENTER)

    # deciding how GUI is formatted
    title_right.grid(row=0, column=0, columnspan = 3, sticky='nsew')
    menu_left.grid(row=1, column=0, rowspan=2, sticky='nsew')
    sub_right.grid(row=1, column=2, rowspan=2, sticky='nsew')

    # weight to puzzle_area so tkinter knows where to use unallocated space
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_rowconfigure(1, weight=1)
    gui.grid_columnconfigure(1, weight=2)
    gui.grid_columnconfigure(2, weight=1)

    # creates menu of puzzles that will appear in puzzle area upon click
    num_of_puzzles = pl.num_of_puzzles
    label = [0 for i in range(num_of_puzzles)]
    for i in range(num_of_puzzles):
        if i == 0:
            menu_easy_title.pack()
        elif i == 8:
            menu_medium_title.pack()
        elif i == 16:
            menu_hard_title.pack()
        label[i] = Label(menu_left, text = "Puzzle #"+str(i+1), bg = "red", font = puzzle_list_font)
        label[i].bind("<Button-1>", lambda event, arg=i: choose_puzzle(event, arg))
        label[i].pack()

    create_puzzle(puzzle)

    gui.config(background="black")
    gui.mainloop()
