import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window

Window.size = (300, 400)

# Generate a Sudoku puzzle and solution
from copy import deepcopy

class SudokuGenerator:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]
        self.fill_board()
        self.solution = deepcopy(self.board)
        self.remove_cells()

    def fill_board(self):
        def is_safe(board, row, col, num):
            for x in range(9):
                if board[row][x] == num or board[x][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        nums = list(range(1, 10))
                        random.shuffle(nums)
                        for num in nums:
                            if is_safe(board, row, col, num):
                                board[row][col] = num
                                if solve(board):
                                    return True
                                board[row][col] = 0
                        return False
            return True

        solve(self.board)

    def remove_cells(self):
        count = 40  # Number of cells to remove
        while count:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1

class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def get_hint(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            return (row, col, num)
        return None

class SudokuGrid(GridLayout):
    def __init__(self, puzzle, solution, **kwargs):
        super(SudokuGrid, self).__init__(**kwargs)
        self.cols = 9
        self.inputs = []
        self.solution = solution

        for row in range(9):
            for col in range(9):
                val = puzzle[row][col]
                if val != 0:
                    ti = TextInput(text=str(val), readonly=True, halign='center',
                                   font_size=24, background_color=(0.6, 1, 0.6, 1))
                else:
                    ti = TextInput(multiline=False, input_filter='int', halign='center', font_size=24)
                    ti.bind(focus=self.on_focus_validate(row, col, ti))
                self.inputs.append(ti)
                self.add_widget(ti)

    def on_focus_validate(self, row, col, ti):
        def callback(instance, focused):
            if not focused:
                value = ti.text
                if value.isdigit() and 1 <= int(value) <= 9:
                    correct = self.solution[row][col]
                    if int(value) == correct:
                        ti.background_color = (0.6, 1, 0.6, 1)  # Green = Correct
                    else:
                        ti.background_color = (1, 0.4, 0.4, 1)  # Red = Incorrect
                else:
                    ti.background_color = (1, 1, 1, 1)  # White = Reset
        return callback


    def get_board(self):
        board = []
        for i in range(0, 81, 9):
            row = []
            for j in range(9):
                val = self.inputs[i + j].text
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_hint(self, row, col, num):
        index = row * 9 + col
        cell = self.inputs[index]
        if not cell.readonly:
            cell.text = str(num)
            cell.background_color = (0.2, 0.9, 1, 1)

class SudokuApp(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=5, padding=5)
        generator = SudokuGenerator()
        self.solution = generator.solution
        self.grid = SudokuGrid(generator.board, generator.solution, size_hint_y=0.85)

        hint_button = Button(text='Get Hint', size_hint_y=0.075)
        hint_button.bind(on_press=self.show_hint)
        self.label = Label(size_hint_y=0.075)

        layout.add_widget(self.grid)
        layout.add_widget(hint_button)
        layout.add_widget(self.label)
        return layout

    def show_hint(self, instance):
        board = self.grid.get_board()
        solver = SudokuSolver(board)
        hint = solver.get_hint()
        if hint:
            row, col, num = hint
            self.grid.set_hint(row, col, num)
            self.label.text = f"Hint: Place {num} at row {row+1}, column {col+1}"
        else:
            self.label.text = "No hints available or puzzle is complete!"

if __name__ == "__main__":
    SudokuApp().run()