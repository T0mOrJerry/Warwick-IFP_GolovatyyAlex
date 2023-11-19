from tkinter import *
from random import randint


class GameWindow(Tk):
    window_width = 500
    window_height = 500
    canvas_width = 400
    canvas_height = 400
    board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

    def __init__(self):
        Tk.__init__(self)
        self.wm_title('Tic-Tac-Toe')
        self.geometry(f'{self.window_width}x{self.window_height}')
        self.minsize(width=self.window_width, height=self.window_height)
        self.maxsize(width=self.window_width, height=self.window_height)
        btn1 = Button(self, text="Start a new game")
        btn1.pack()
        self.lbl = Label(self, text='')
        self.lbl.pack()
        btn1.bind('<Button-1>', self.new_game)
        self.canvas = Canvas(self, bg="white", width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(anchor=CENTER, expand=1)
        self.canvas.bind('<Button-1>', self.click)
        self.turn = 'Cross'

    def new_game(self, event):
        self.canvas.delete('all')
        self.canvas.create_line(self.canvas_width // 3 + 5, 0, self.canvas_width // 3 + 5, self.canvas_height, width=10)
        self.canvas.create_line(self.canvas_width // 3 * 2 + 5, 0, self.canvas_width // 3 * 2 + 5, self.canvas_height,
                                width=10)
        self.canvas.create_line(0, self.canvas_height // 3 + 5, self.canvas_width, self.canvas_height // 3 + 5,
                                width=10)
        self.canvas.create_line(0, self.canvas_height // 3 * 2 + 5, self.canvas_width, self.canvas_height // 3 * 2 + 5,
                                width=10)
        self.lbl.configure(text=f"It's {self.turn} turn")
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def cross(self, x, y):
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
            self.board[i][j] = 1
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
            self.turn = 'Nought'

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

    def check(self, flag):
        pass

    def click(self, event):
        x = event.x
        y = event.y
        if self.canvas_width // 3 < x < self.canvas_width // 3 + 15 or self.canvas_width // 3 * 2 < x < \
                self.canvas_width // 3 * 2 + 15:
            pass
        elif self.canvas_height // 3 < y < self.canvas_height // 3 + 15 or self.canvas_height // 3 * 2 < y < \
                self.canvas_height // 3 * 2 + 15:
            pass
        else:
            if self.turn == 'Cross':
                self.cross(x, y)
                self.check(1)
            else:
                self.noughts(x, y)
                self.check(-1)
            self.lbl.configure(text=f"It's {self.turn} turn")


if __name__ == "__main__":
    app = GameWindow()
    app.mainloop()
