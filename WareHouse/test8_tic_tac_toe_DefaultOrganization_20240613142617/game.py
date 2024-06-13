'''
This file contains the Game class which represents the tic tac toe game logic.
'''
class Game:
    def __init__(self):
        # Initialize the game board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    def make_move(self, row, col):
        # Make a move on the game board
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        # Check if there is a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
    def is_board_full(self):
        # Check if the game board is full
        for row in self.board:
            if ' ' in row:
                return False
        return True