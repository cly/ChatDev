'''
This is the main file of the tic tac toe game.
'''
from game import Game
from gui import GUI
def main():
    # Create an instance of the game
    game = Game()
    # Create an instance of the GUI
    gui = GUI(game)
    # Start the game loop
    gui.run()
if __name__ == "__main__":
    main()