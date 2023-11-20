# Import all the essential modules - tkinter for window and graphics, random for some chaos
from tkinter import *
from random import randint


# The window of the game is described as a class, because inside the class it's easier to store and
# use global variables
# The game is a sequence of inputs and responding functions for them - that's why it's easier to do it as class
class GameWindow(Tk):
    # Some global starting constants for the class
    window_width = 500
    window_height = 500
    canvas_width = 400
    canvas_height = 400
    board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]  # This is the array which will store all the turns

    # Initialising function - it will create the window, the canvas to draw on and set some default values
    def __init__(self):
        # Initialising the window and setting for it
        Tk.__init__(self)
        self.wm_title('Tic-Tac-Toe')
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.minsize(width=self.window_width, height=self.window_height)
        self.maxsize(width=self.window_width, height=self.window_height)
        # Creating the button for a new game, add it to the window and configure the reaction, if it's pressed
        btn1 = Button(self, text="Start a new game")
        btn1.pack()
        btn1.bind('<Button-1>', self.new_game)
        # Creating the label for showing some info for gamers
        self.lbl = Label(self, text='')
        self.lbl.pack()
        # Creating the canvas to draw on it, configuring it and add the reaction for left mouse click on the canvas
        self.canvas = Canvas(self, bg="white", width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(anchor=CENTER, expand=1)
        self.canvas.bind('<Button-1>', self.click)
        self.turn = 'Cross'
        self.start = False  # THis variable shows whether the game was started, or canvas is still blank

    # This function is called when the start button is pressed, it's preparing canvas for the new game and
    # set default values for some variables
    def new_game(self, event):
        # Cleaning the canvas and draw the playing field with cell borders
        self.canvas.delete('all')
        self.canvas.create_line(self.canvas_width // 3 + 5, 0, self.canvas_width // 3 + 5, self.canvas_height, width=10)
        self.canvas.create_line(self.canvas_width // 3 * 2 + 5, 0, self.canvas_width // 3 * 2 + 5, self.canvas_height,
                                width=10)
        self.canvas.create_line(0, self.canvas_height // 3 + 5, self.canvas_width, self.canvas_height // 3 + 5,
                                width=10)
        self.canvas.create_line(0, self.canvas_height // 3 * 2 + 5, self.canvas_width, self.canvas_height // 3 * 2 + 5,
                                width=10)
        self.turn = 'Cross'  # Crosses always have first turn
        self.lbl.configure(text=f"It's {self.turn} turn", fg='black')
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Updating matrix for new game
        self.start = True  # Now the game is started

    # This function draw cross in the cell which match given coordinates
    def cross(self, x, y):
        # The following block match the coordinates with the index in the game matrix
        if x <= self.canvas_width // 3:
            i = 0
        elif x >= self.canvas_width // 3 * 2 + 15:
            i = 2
        else:
            i = 1
        if y <= self.canvas_height // 3:
            j = 0
        elif y >= self.canvas_height // 3 * 2 + 15:
            j = 2
        else:
            j = 1
        if not self.board[i][j]:  # If the cell is empty
            self.board[i][j] = 1
            # Drawing two crossed lines: their beginnings, ends and width are randomly different to make them look
            # like drawn by human
            self.canvas.create_line(self.canvas_width // 3 * i + randint(8, 17),
                                    self.canvas_height // 3 * j + randint(8, 17),
                                    self.canvas_width // 3 * (i + 1) - randint(3, 12),
                                    self.canvas_height // 3 * (j + 1) - randint(3, 12),
                                    width=randint(7, 10), fill='red')
            self.canvas.create_line(self.canvas_width // 3 * (i + 1) - randint(8, 17),
                                    self.canvas_height // 3 * j + randint(8, 17),
                                    self.canvas_width // 3 * i + randint(3, 12),
                                    self.canvas_height // 3 * (j + 1) - randint(3, 12),
                                    width=randint(7, 9), fill='red')
            self.turn = 'Nought'  # After Crosses goes Noughts turn
            self.lbl.configure(text=f"It's {self.turn} turn", fg='black')

    # This function draw nought in the cell which match given coordinates - does the same thing,
    # as the previous, but with circles
    def noughts(self, x, y):
        if x <= self.canvas_width // 3:
            i = 0
        elif x >= self.canvas_width // 3 * 2 + 15:
            i = 2
        else:
            i = 1
        if y <= self.canvas_height // 3:
            j = 0
        elif y >= self.canvas_height // 3 * 2 + 15:
            j = 2
        else:
            j = 1
        if not self.board[i][j]:
            self.board[i][j] = -1
            self.canvas.create_oval(self.canvas_width // 3 * i + randint(8, 17),
                                    self.canvas_height // 3 * j + randint(8, 17),
                                    self.canvas_width // 3 * (i + 1) - randint(3, 12),
                                    self.canvas_height // 3 * (j + 1) - randint(3, 12),
                                    width=randint(6, 8), outline='green')
            self.turn = 'Cross'
            self.lbl.configure(text=f"It's {self.turn} turn", fg='black')

    # The function truing to find three same figures straight
    def check(self, flag):
        for i in range(len(self.board)):  # Searching in the columns (with the same x coordinate)
            if sum(self.board[i]) == 3 * flag:
                self.canvas.create_line(self.canvas_width / 3 * i + self.canvas_width / 6, 0,
                                        self.canvas_width / 3 * i + self.canvas_width / 6, self.canvas_height,
                                        width=randint(8, 11), fill='blue')  # Drawing a "winning line"
                self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]  # Filling the matrix to show, that the game is over
                return True
        for i in range(3):  # Searching in the rows (with the same y coordinate)
            if self.board[0][i] + self.board[1][i] + self.board[2][i] == 3 * flag:
                self.canvas.create_line(0, self.canvas_height / 3 * i + self.canvas_height / 6,
                                        self.canvas_width, self.canvas_height / 3 * i + self.canvas_height / 6,
                                        width=randint(8, 11), fill='blue')
                self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                return True
        # Two following ifs check the diagonals
        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 3 * flag:
            self.canvas.create_line(0, 0,
                                    self.canvas_width, self.canvas_height,
                                    width=randint(8, 11), fill='blue')
            self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            return True
        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 3 * flag:
            self.canvas.create_line(self.canvas_width, 0,
                                    0, self.canvas_height,
                                    width=randint(8, 11), fill='blue')
            self.board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
            return True
        return False

    # This function is activated when the user click in the canvas
    def click(self, event):
        x = event.x  # Get the x coordinate of the user's click
        y = event.y  # Get the y coordinate of the user's click
        # Next block check whether click was inside a cell, not on borders
        if self.canvas_width // 3 < x < self.canvas_width // 3 + 15 or self.canvas_width // 3 * 2 < x < \
                self.canvas_width // 3 * 2 + 15:
            pass
        elif self.canvas_height // 3 < y < self.canvas_height // 3 + 15 or self.canvas_height // 3 * 2 < y < \
                self.canvas_height // 3 * 2 + 15:
            pass
        else:
            # If the coordinates are accepted It draw either Cross or Nought
            if self.turn == 'Cross':
                self.cross(x, y)  # This function get the coordinates and draw a cross in right cell
                if self.check(1):  # This function check if crosses has won by now
                    self.lbl.configure(text=f"Crosses Win!", fg='red')
                    self.start = False
                else:
                    # Check is it a draw if noone win this turn
                    s = 1
                    for i in self.board:
                        for j in i:
                            s *= j
                    # If there is at least one empty cell, s will be equal 0
                    if s and self.start:  # If s is true, != 0, then all the cells are used
                        self.lbl.configure(text=f"Draw", fg='blue')
            else:
                # The same jobs but for noughts
                self.noughts(x, y)
                if self.check(-1):
                    self.lbl.configure(text=f"Noughts Win!", fg='green')
                    self.start = False
                else:
                    s = 1
                    for i in self.board:
                        for j in i:
                            s *= j
                    if s and self.start:
                        self.lbl.configure(text=f"Draw", fg='blue')


# Running the program until the window is closed
if __name__ == "__main__":
    app = GameWindow()
    app.mainloop()
