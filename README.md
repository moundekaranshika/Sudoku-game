# 🤩 Sudoku Solver – Python Project

Automatically solve any 9x9 Sudoku puzzle using the backtracking algorithm. Includes both a **console-based** solver and a **Tkinter GUI interface** for interactive play.

![sudoku\_banner](https://www.google.com/imgres?q=sudoku&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2Fe%2Fe0%2FSudoku_Puzzle_by_L2G-20050714_standardized_layout.svg%2F250px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSudoku&docid=2PH68oM51aR1nM&tbnid=uc7Uo45UJQ3HNM&vet=12ahUKEwj4ov7Tq9WNAxXvT2wGHV_NKqkQM3oECBoQAA..i&w=250&h=250&hcb=2&ved=2ahUKEwj4ov7Tq9WNAxXvT2wGHV_NKqkQM3oECBoQAA)

---

## 📌 Features

✅ Solve any 9x9 Sudoku puzzle
✅ Backtracking algorithm
✅ Input validation
✅ Simple and responsive GUI using `tkinter`
✅ Clear, Reset, and Solve buttons
✅ Console and GUI versions included

---

## 🚀 Demo

> **CLI Version**

```bash
python sudoku_solver.py
```

> **GUI Version**

```bash
python sudoku_gui.py
```

---

## 🧠 Algorithm

This project uses the **backtracking** algorithm to try all possibilities in a recursive depth-first manner until the puzzle is solved.

```python
def solve(board):
    row, col = find_empty(board)
    if row is None:
        return True

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack

    return False
```

---

## 🖥️ GUI Preview

The `tkinter` GUI allows you to enter your own puzzle, clear the board, or solve it instantly:

* **Solve**: Triggers the backtracking algorithm.
* **Clear**: Resets the board to blank.
* **Quit**: Closes the window.

---

## 📁 Project Structure

```
sudoku-solver/
├── sudoku_solver.py        # Console-based solver
├── sudoku_gui.py           # GUI interface with tkinter
├── README.md               # Project documentation
└── requirements.txt        # Dependencies (optional)
```

---

## 🧪 Example Puzzle

```python
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
```

---

## 📦 Requirements

* Python 3.x
* `tkinter` (comes pre-installed with Python)

```bash
# To install dependencies (if separated)
pip install -r requirements.txt
```

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Made by [Anshika Moundekar](https://github.com/moundekaranshika)
