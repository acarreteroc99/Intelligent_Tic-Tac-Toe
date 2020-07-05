


import random
from Algorithms import *

class Game:
    def __init__(self, squares):
        self.board = []
        self.squares = int(squares)
        self.dimension = self.squares * self.squares
        self.__init__board()
        self.player1 = []
        self.player2 = []

    def __init__board(self):
        for i in range(0, self.dimension):
            self.board.append(" ")

    def printBoard3(self):
        print("-----------------")
        for i in range(-1, self.dimension-1):
            j = i+1
            print(self.board[j], " | ", end=" ")
            #print(self.board[i], " | ", self.board[i+1], " | " , self.board[i+2])
            if(i % self.squares == 1):
                print("\n", "-----------------")

    def playerMoves(self):
        print("You move: ")
        playerMove = int(input())
        playerMove = checkPlayerMove(playerMove, self.dimension, self.board)

        return playerMove


    def checkMove(self, caller):
        if self.squares == 3:
            defeat = self.check3InLine(caller)

        return defeat

    def check3InLine(self, caller):
        endOfGame = 0

        if caller == 'O':
            if self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
                endOfGame = 1
            elif self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
                endOfGame = 1
            elif self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
                endOfGame = 1
            elif self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
                endOfGame = 1
            elif self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
                endOfGame = 1
            elif self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
                endOfGame = 1
            elif self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
                endOfGame = 1
            elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
                endOfGame = 1

        elif caller == 'X':
            if self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
                endOfGame = 1
            elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
                endOfGame = 1
            elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
                endOfGame = 1
            elif self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
                endOfGame = 1
            elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
                endOfGame = 1
            elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
                endOfGame = 1
            elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
                endOfGame = 1
            elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
                endOfGame = 1

        return endOfGame

    def playGame(self):
        defeat = 0
        full = 0
        while defeat == 0 and full == 0:
            if " " not in self.board:
                full = 1

            pMove = self.playerMoves()
            self.board[pMove] = 'O'
            defeat = self.checkMove('O')
            self.printBoard3()

            if defeat == 1:
                print('Player, you win :( ')
            else:
                print("AI moves: \n")
                self.board = (minimax(self.board, 'X', 2, self.dimension))[1]
                self.printBoard3()
                defeat = self.checkMove('X')

                if defeat == 1:
                    print("I win B)")

        if full == 1:
            print("That's a draw")

def checkPlayerMove(pMove, d, board):
    correct = 0

    # Checks if the square entered by the user is in the range
        # Checks if the selected square is empty or not
    while correct == 0:
        if 0 <= pMove and pMove < d:
            if board[pMove] == " ":
                board[pMove] = 'O'
                correct = 1
            else:
                print("This square is not empty. Intro square: ")
                pMove = int(input())
        else:
            print("Introduce a square between 0 and ", d)
            pMove = int(input())

    return pMove
