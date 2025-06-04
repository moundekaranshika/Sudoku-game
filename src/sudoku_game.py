import tkinter as tk
from tkinter import messagebox
import copy

class SudokuGame:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Game")

        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.cells = {}
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.master)
        frame.pack()

        for row in range(9):
            for col in range(9):
                e = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
                e.grid(row=row, column=col, padx=1, pady=1)

                # Thicker 3x3 box borders
                if col % 3 == 0:
                    e.grid(padx=(3,1))
                if row % 3 == 0:
                    e.grid(pady=(3,1))

                val = self.board[row][col]
                if val != 0:
                    e.insert(0, str(val))
                    e.config(state='readonly', readonlybackground='#eee')
                self.cells[(row, col)] = e

    def create_buttons(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=10)

        solve_button = tk.Button(frame, text="Solve", command=self.solve)
        solve_button.pack(side=tk.LEFT, padx=10)

        hint_button = tk.Button(frame, text="Hint", command=self.give_hint)
        hint_button.pack(side=tk.LEFT, padx=10)

        clear_button = tk.Button(frame, text="Clear", command=self.clear)
        clear_button.pack(side=tk.LEFT, padx=10)

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                entry = self.cells[(row, col)]
                val = entry.get()
                if val == '':
                    current_row.append(0)
                elif val.isdigit() and 1 <= int(val) <= 9:
                    current_row.append(int(val))
                else:
                    messagebox.showerror("Invalid input", f"Invalid value at row {row+1} column {col+1}")
                    return None
            board.append(current_row)
        return board

    def is_valid(self, board, num, pos):
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def solve_board(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        row, col = find
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.solve_board(board):
                    return True
                board[row][col] = 0
        return False

    def solve(self):
        board = self.get_board()
        if board is None:
            return
        if self.solve_board(board):
            for i in range(9):
                for j in range(9):
                    entry = self.cells[(i, j)]
                    if entry.cget('state') == 'normal':
                        entry.delete(0, tk.END)
                        entry.insert(0, str(board[i][j]))
                        entry.config(fg='black')
        else:
            messagebox.showinfo("No Solution", "This board has no solution.")

    def give_hint(self):
        board = self.get_board()
        if board is None:
            return
        solved = copy.deepcopy(board)
        if not self.solve_board(solved):
            messagebox.showinfo("No Solution", "Cannot give hint: no solution exists.")
            return

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    self.cells[(i, j)].insert(0, str(solved[i][j]))
                    self.cells[(i, j)].config(fg='blue')
                    return
        messagebox.showinfo("Hint", "No hint available — puzzle may be solved.")

    def clear(self):
        for (i, j), entry in self.cells.items():
            if self.board[i][j] == 0:
                entry.config(state='normal')
                entry.delete(0, tk.END)
                entry.config(fg='black')

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
