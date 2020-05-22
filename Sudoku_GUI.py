import numpy as np
import random
import math
import gen_puzzle as gen
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import puzzle_list as pl
import time
#Sparro

# creates title bar for Sudoku puzzle
def create_title():
    title = Frame(gui, bg = "DodgerBlue2")
    title.grid(row=0, column=0, columnspan = 3, sticky='nsew')

    title_text = Label(title, text = "Sparro Sudoku", font = title_font, bg = "DodgerBlue2")
    title_text.pack()

# creates title bar to display current puzzles being shown
# @i                puzzle number to be displayed
def create_puzzle_title_bar(i):
    puzzle_title_bar = Frame(gui, bg = "DodgerBlue2",  highlightbackground="black", highlightthickness=2)
    puzzle_title_bar.grid(row=1, column=1, sticky = 'nsew')
    title_bar_label = Label(puzzle_title_bar, text = "Puzzle #"+str(i), font = puzzle_title_bar_font, bg = "DodgerBlue2")

    # first puzzle is to be named "Test Puzzle"
    if i == 0:
        title_bar_label = Label(puzzle_title_bar, text = "Test Puzzle", font = puzzle_title_bar_font, bg = "DodgerBlue2")

    title_bar_label.pack()

# creates menu on left of GUI
def create_menu():
    menu_left = Frame(gui, width = 150, height = 150, bg = "brown2", highlightbackground="black", highlightthickness=2)
    menu_left.grid(row=1, column=0, rowspan=2, sticky='nsew')

    menu_title = Label(menu_left, text = "Choose a puzzle:", font = puzzle_list_title_font, bg = "brown2")
    menu_easy_title = Label(menu_left, text = "Easy", font = puzzle_list_category_font, bg = "brown2")
    menu_medium_title = Label(menu_left, text = "Medium", font = puzzle_list_category_font, bg = "brown2")
    menu_hard_title = Label(menu_left, text = "Hard", font = puzzle_list_category_font, bg = "brown2")
    menu_title.pack()


    # Test puzzle created for troubleshooting and user to learn about GUI's operation
    test_label = Label(menu_left, text = "Test Puzzle", bg = "brown2", font = puzzle_list_font)
    test_label.bind("<Button-1>", lambda event, arg=0: choose_puzzle(event, arg))
    test_label.pack()

    # creates menu of puzzles that will appear in puzzle area upon click
    num_of_puzzles = pl.num_of_puzzles
    label = [0 for i in range(num_of_puzzles+1)]
    for i in range(1, num_of_puzzles+1):
        if i == 1:
            menu_easy_title.pack()
        elif i == 8:
            menu_medium_title.pack()
        elif i == 16:
            menu_hard_title.pack()
        label[i] = Label(menu_left, text = "Puzzle #"+str(i), bg = "brown2", font = puzzle_list_font)
        label[i].bind("<Button-1>", lambda event, arg=i: choose_puzzle(event, arg))
        label[i].pack()

# redraws lines as window is resized
def redraw_lines(event):
    width = event.width
    height = event.height
    canvas = event.widget
    canvas.coords("horizontal", 0, 0, width, 0)
    canvas.coords("vertical", 0, 0, 0, height)

# inputs puzzle into the canvas window with 0's as available user inputs
def create_puzzle():
    global puzzle_area, result_msg, puzzle, solution
    puzzle_area.destroy()
    result_msg.destroy()
    create_sub()

    # Sudoku puzzle in middle of GUI
    puzzle_area = Canvas(gui, width = 150, height = 200, background = "DodgerBlue2")
    puzzle_area.grid(row=2, column=1, sticky='nsew')

    # creates NxN grid distributed evenly in the canvas window for puzzle
    idx = 0
    while idx < N:
        puzzle_area.rowconfigure(idx, weight=1)
        puzzle_area.columnconfigure(idx, weight=1)
        idx += 1

    for i in range(N):
        for j in range(N):
            # calls function to redraw lines
            puzzle_unit=Canvas(puzzle_area, width=60, height=10, highlightthickness=0, bg='DodgerBlue2')
            puzzle_unit.bind("<Configure>", redraw_lines)

            # create thicker lines every 3 rows/columns for Sudoku purposes
            if i % 3 == 0 and i > 0:
                puzzle_unit.create_line(0,0,0,0, tags=("horizontal"), width = 8)
            if j % 3 == 0 and j > 0:
                puzzle_unit.create_line(0,0,0,0, tags=("vertical"), width = 8)
                puzzle_unit.create_line(0,0,0,0, tags=("horizontal"), width = 1)
            else:
                puzzle_unit.create_line(0,0,0,0, tags=("horizontal"), width = 1)
                puzzle_unit.create_line(0,0,0,0, tags=("vertical"), width = 1)

            puzzle_unit.grid(row=i, column=j, sticky="nsew")

            if puzzle[i][j] != 0:   # if node not removed a label is produced
                label = Label(puzzle_unit, text = str(puzzle[i][j]), font = puzzle_font, bg = "DodgerBlue2")
                label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                user_solution[i][j] = label
            else:                   # creates user input for the nodes removed by gen_puzzle.py
                entry = Entry(puzzle_unit, font = puzzle_font, justify = 'center', width = 1, bg = "DodgerBlue2")
                entry.config(highlightthickness = 1, highlightbackground = 'LightCyan2', highlightcolor = 'LightCyan2')
                entry.place(relx = 0.5, rely = 0.5, anchor = CENTER)
                user_solution[i][j] = entry

# creates submisstion area or refreshes its state
def create_sub():
    global sub_right
    sub_right.destroy()

    # user solution submission area on right of GUI
    sub_right = Frame(gui, width = 280, height = 150, bg = "gold2", highlightbackground="black", highlightthickness=2)
    sub_right.grid(row=1, column=2, rowspan=2, sticky='nsew')

    # creates buttons for submitting and showing answers
    sub_button = Button(sub_right, text = "Submit", height = 2, width = 10, command = check_answer)
    sub_show_answer = Button(sub_right, text = "Show Answer", height = 2, width = 10, command = show_answer)
    sub_button.place(relx = 0.18, rely = 0.97, anchor = CENTER)
    sub_show_answer.place(relx = 0.82, rely = 0.97, anchor = CENTER)

# validates user input and produces appropriate response
def check_answer():
    global result_msg, puzzle, solution
    result_msg.destroy()
    create_sub()

    #verifies each user entry matches solution
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 0:
                if float(user_solution[i][j].get()) != solution[i][j]:
                    result_msg = Label(sub_right, text = "Incorrect. Try again", font = sub_font, bg = "brown2")
                    # checks if one of the entered values is an impossible Sudoku entry (i.e. > 9)
                    if float(user_solution[i][j].get()) >= 10:
                        result_msg = Label(sub_right, text = "One of your entered values is greater than 10", font = sub_font, bg = "brown2")
                        result_msg.config(wraplength = 250)
                    result_msg.place(relx = 0.5, rely = 0.5, anchor=CENTER)
                    sub_right.config(bg='brown2')
                    return False
    # if no user entered values are incorrect a success msg is shown
    result_msg = Label(sub_right, text = "You're a genius!", font = sub_font, bg = "green")
    result_msg.place(relx = 0.5, rely = 0.5, anchor=CENTER)
    sub_right.config(bg='green')
    return True


# allows user to choose a puzzle by clicking on a specific puzzle label
def choose_puzzle(event, i):
    global puzzle, solution
    puzzle = pl.puzzles[i]
    solution = pl.solutions[i]
    create_puzzle_title_bar(i)
    create_puzzle()

# shows the answer of the puzzle to the user
def show_answer():
    global puzzle, solution
    result_msg.destroy()
    sub_right.config(bg = 'gold2')

    # Sudoku puzzle in sub_area
    solution_area = Canvas(sub_right, width = 100, height = 100, background = "DodgerBlue2")
    solution_title = Label(sub_right, text = "Puzzle Solution:", font = solution_title_font, bg = "gold2")
    solution_title.place(relx = 0.5, rely = 0.04, anchor=CENTER)
    solution_area.place(relx = 0.5, rely = 0.34, anchor=CENTER)

    # creates NxN grid distributed evenly in the canvas window for puzzle
    idx = 0
    while idx < N:
        solution_area.rowconfigure(idx, weight=1)
        solution_area.columnconfigure(idx, weight=1)
        idx += 1

    for i in range(N):
        for j in range(N):
            solution_unit = Canvas(solution_area, width = '32', height = '42', highlightthickness=0, bg='DodgerBlue2')
            solution_unit.bind("<Configure>", redraw_lines)

            # create thicker lines every 3 rows/columns for Sudoku purposes
            if i % 3 == 0 and i > 0:
                solution_unit.create_line(0,0,0,0, tags=("horizontal"), width = 5)
            if j % 3 == 0 and j > 0:
                solution_unit.create_line(0,0,0,0, tags=("vertical"), width = 5)
                solution_unit.create_line(0,0,0,0, tags=("horizontal"), width = 1)
            else:
                solution_unit.create_line(0,0,0,0, tags=("horizontal"), width = 1)
                solution_unit.create_line(0,0,0,0, tags=("vertical"), width = 1)

            solution_unit.grid(row=i, column=j, sticky="nsew")

            if puzzle[i][j] == 0:
                label = Label(solution_unit, text = str(solution[i][j]), font = solution_font, bg = "brown2")
            else:
                label = Label(solution_unit, text = str(solution[i][j]), font = solution_font, bg = "DodgerBlue2")

            label.place(relx = 0.5, rely = 0.5, anchor = CENTER)


if __name__ == "__main__":

    # Dimensions of NxN sudoku matrix
    N = pl.N

    # initializes size, title, and tkinter gui itself
    gui = Tk()
    gui.title("Sparro Sudoku")
    gui.geometry("1250x800")

    # global variables to be changed throughout user interaction
    puzzle = pl.puzzles[0]
    solution = pl.solutions[0]
    user_solution = [ ['0' for i in range(N)] for j in range(N)]
    puzzle_area = Canvas(gui)
    result_msg = Label(gui)
    sub_right = Frame(gui)

    # weight to puzzle_area so tkinter knows where to use unallocated space
    gui.grid_columnconfigure(0, weight=1)
    gui.grid_rowconfigure(2, weight=2)
    gui.grid_columnconfigure(1, weight=2)
    gui.grid_columnconfigure(2, weight=1)

    #fonts and font sizes
    title_font = tkFont.Font(family= "Courier bold", size = 40)
    puzzle_title_bar_font = tkFont.Font(family="Courier", size = 30)
    puzzle_font = tkFont.Font(family= "Courier", size = 40)
    solution_title_font = tkFont.Font(family="Courier", size = 20)
    solution_font = tkFont.Font(family="Courier", size = 28)
    puzzle_list_title_font = tkFont.Font(family="Courier", size = 28)
    puzzle_list_category_font = tkFont.Font(family="Courier bold", size = 22)
    puzzle_list_font = tkFont.Font(family= "Courier", size = 18)
    sub_font = tkFont.Font(family= "Courier", size = 20)

    #main set of function calls for GUI
    create_title()
    create_puzzle_title_bar(0)
    create_menu()
    create_puzzle()

    gui.mainloop()
