


"""
Notes on the game:

1. 'O' play first always and 'X' next. Does not matter who begins playing

"""

from Game import *

if __name__ == "__main__":

    correct = 0
    square = 3

    print("----- TIC-TAC-TOE -----")
    print("Right now the game is only available on a 3x3 board and user plays first. To be improved...")

    print("Before we begin, I will tell you how to make a move. During your turn, you will have to indicate the square where you want to place a piece. ")
    print("The top-left corner is number 0, the top-rigth corner is", square-1, "and below square 0 is square number", square, "and so on \n")
    print("Once said, good luck! Your loss will be quick though ;) \n")

    game = Game(3)
    game.printBoard3()
    game.playGame()
