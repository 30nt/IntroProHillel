import random
from tkinter import *


class My15:
    def __init__(self):
        self.my_15 = self._generate_15()
        self.row, self.col = self.get_space()

    def _generate_15(self):
        my_15 = []
        all_values = [str(i) for i in range(1, 16)] + [""]
        random.shuffle(all_values)
        for row_number in range(4):
            my_15.append(all_values[4 * row_number: 4 * (row_number + 1)])
        return my_15

    def print_15(self):
        for row in self.my_15:
            line = " ".join([f"{val:2}" for val in row])
            print(line)

    def get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self.my_15):
            if '' in row:
                row_ = i
                for j, col in enumerate(row):
                    if '' == col:
                        col_ = j
        return row_, col_

    def move_down(self):
        if self.row == 3:
            return
        self.my_15[self.row][self.col], self.my_15[self.row + 1][self.col] = self.my_15[self.row + 1][self.col], \
                                                                             self.my_15[self.row][self.col]
        self.row += 1

    def move_up(self):
        if self.row == 0:
            return
        self.my_15[self.row][self.col], self.my_15[self.row - 1][self.col] = self.my_15[self.row - 1][self.col], \
                                                                             self.my_15[self.row][self.col]
        self.row -= 1

    def move_right(self):
        if self.col == 3:
            return
        self.my_15[self.row][self.col], self.my_15[self.row][self.col + 1] = self.my_15[self.row][self.col + 1], \
                                                                             self.my_15[self.row][self.col]
        self.col += 1

    def move_left(self):
        if self.col == 0:
            return
        self.my_15[self.row][self.col], self.my_15[self.row][self.col - 1] = self.my_15[self.row][self.col - 1], \
                                                                             self.my_15[self.row][self.col]
        self.col -= 1


def draw_15_table(my_15):
    for row_index, row in enumerate(my_15.my_15):
        for col_index, col in enumerate(row):
            label = Entry(root, width=2, fg='white', bg='black', font=('Arial', 50, 'bold'), justify='center')
            label.config(highlightbackground="black")
            label.grid(row=row_index, column=col_index)
            label.insert(END, col)


def left(event):
    my_15.move_left()
    draw_15_table(my_15)


def right(event):
    my_15.move_right()
    draw_15_table(my_15)


def up(event):
    my_15.move_up()
    draw_15_table(my_15)


def down(event):
    my_15.move_down()
    draw_15_table(my_15)


my_15 = My15()
my_15.print_15()
root = Tk()
root.title("15")
root.geometry("275x280")
root.configure(background='black')
draw_15_table(my_15)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()
