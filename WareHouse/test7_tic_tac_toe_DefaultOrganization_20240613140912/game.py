'''
This file contains the Game class which represents the tic tac toe game logic.
'''
class Game:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False
    def check_winner(self):
        if not self.is_board_empty():
            for i in range(3):
                if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                    return True
                if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                    return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
                return True
        return False
    def is_board_empty(self):
        for row in self.board:
            if any(row):
                return False
        return True
    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"