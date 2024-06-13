# Tic Tac Toe Game User Manual

## Introduction

Welcome to the Tic Tac Toe Game! This game is a classic two-player game where players take turns marking spaces on a 3x3 grid. The goal is to get three of your marks in a row, either horizontally, vertically, or diagonally.

## Installation

To use the Tic Tac Toe Game, you need to have Python installed on your computer. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to set up the environment and install the necessary dependencies:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Create a virtual environment (optional but recommended): `python -m venv env`
4. Activate the virtual environment:
   - For Windows: `.\env\Scripts\activate`
   - For macOS/Linux: `source env/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To start playing the Tic Tac Toe Game, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have saved the game files.
3. Activate the virtual environment (if you created one).
4. Run the game: `python main.py`

Once the game starts, you will see a 3x3 grid displayed on the screen. Each cell in the grid represents a position where you can place your mark (either "X" or "O").

To make a move, you need to enter the row and column numbers of the position where you want to place your mark. The row and column numbers should be integers between 0 and 2, inclusive.

For example, to place your mark in the top-left corner, you would enter `0` for the row and `0` for the column.

After each move, the game will display the updated grid and indicate whose turn it is next.

The game will continue until one player wins or the board is full (a tie). If a player wins, a message will be displayed announcing the winner. If the board is full and there is no winner, a message will be displayed announcing a tie.

To play again, you can simply run the game again by executing the `python main.py` command.

## Conclusion

Congratulations! You now know how to install and play the Tic Tac Toe Game. Enjoy playing with your friends and have fun!