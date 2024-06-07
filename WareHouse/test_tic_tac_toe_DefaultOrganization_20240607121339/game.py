'''
Game class
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from board import Board
class Game:
    def __init__(self, root):
        self.root = root
        self.board = Board(root)
        self.current_player = "X"
        self.board.canvas.bind("<Button-1>", self.handle_click)
    def handle_click(self, event):
        if self.board.is_game_over():
            messagebox.showinfo("Game Over", "The game is already over!")
            return
        x, y = event.x, event.y
        row, col = self.board.get_clicked_cell(x, y)
        if row is not None and col is not None:
            if self.board.is_cell_empty(row, col):
                self.board.set_cell(row, col, self.current_player)
                if self.board.is_winner(self.current_player):
                    messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                    self.board.reset()
                elif self.board.is_board_full():
                    messagebox.showinfo("Draw", "It's a draw!")
                    self.board.reset()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
class Board:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()
        self.cells = [["" for _ in range(3)] for _ in range(3)]
        self.draw_board()
    def draw_board(self):
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100)
            self.canvas.create_line(i * 100, 0, i * 100, 300)
    def get_clicked_cell(self, x, y):
        row = y // 100
        col = x // 100
        return row, col
    def is_cell_empty(self, row, col):
        return self.cells[row][col] == ""
    def set_cell(self, row, col, player):
        self.cells[row][col] = player
        x = col * 100 + 50
        y = row * 100 + 50
        self.canvas.create_text(x, y, text=player, font=("Arial", 40))
    def is_winner(self, player):
        for i in range(3):
            if self.cells[i][0] == self.cells[i][1] == self.cells[i][2] == player:
                return True
            if self.cells[0][i] == self.cells[1][i] == self.cells[2][i] == player:
                return True
        if self.cells[0][0] == self.cells[1][1] == self.cells[2][2] == player:
            return True
        if self.cells[0][2] == self.cells[1][1] == self.cells[2][0] == player:
            return True
        return False
    def is_board_full(self):
        for row in self.cells:
            if "" in row:
                return False
        return True
    def is_game_over(self):
        return self.is_winner("X") or self.is_winner("O") or self.is_board_full()
    def reset(self):
        self.canvas.delete("all")
        self.cells = [["" for _ in range(3)] for _ in range(3)]
        self.draw_board()