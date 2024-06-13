'''
This file contains the GUI class which represents the graphical user interface of the tic tac toe game.
'''
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=' ', width=10, height=5,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def run(self):
        self.window.mainloop()
    def make_move(self, row, col):
        self.game.make_move(row, col)
        self.update_board()
        winner = self.game.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.window.quit()
        elif self.game.is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.window.quit()
    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.game.board[i][j])