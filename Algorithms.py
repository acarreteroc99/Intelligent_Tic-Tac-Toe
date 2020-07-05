

"""
    NOTES:

        + 'O' --> max ; 'X' --> mini


"""
import copy

# ===================================   MINIMAX   ======================================

""" --- HEURISTIC --- 

    0   | -10 | -100
    ----|-----|-----
    10  |  0  |  0
    ----|-----|-----
    100 |  0  |  0


"""

heuristicList = [0, -10, -100, 10, 0, 0, 100, 0, 0]

def invert(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def calcMinimaxHeuristic(actualBoard, size):
    playerX = 0
    playerO = 0

    for i in range(0, size):

        if actualBoard[i] == 'X':
            playerX += heuristicList[i]
        elif actualBoard[i] == 'O':
            playerO += heuristicList[i]

    return (playerO - playerX)

def expandMinimax(board, player, size):

    auxTree = []

    for i in range(0, size):
        if board[i] == " ":
            board[i] = player
            auxTree.append(copy.deepcopy(board))
            board[i] = " "

    return auxTree

def minimum(list):

    min = list[0][0]
    iScenario = 0

    for i in range(1, len(list)):
        if min > list[i][0]:
            min = list[i][0]
            iScenario = i

    return list[iScenario]

def maximum(list):
    max = list[0][0]
    iScenario = 0

    for i in range(1, len(list)):
        if max < list[i][0]:
            max = list[i][0]
            iScenario = i

    return list[iScenario]


# actualBoard: list of 'size' positions
# player: 'O' or 'X'
# profmax: a number defining de maximum depth
# size: number of squares in the board (square * square)

def minimax(actualBoard, player, profmax, size):
    min = 'X'
    max = 'O'

    if profmax == 0:
        return ([calcMinimaxHeuristic(actualBoard, size),actualBoard])
    else:
        tree = expandMinimax(actualBoard, player, size)
        L = []
        for scenario in tree:
            profmax -= 1
            V = minimax(scenario, invert(player), profmax, size)
            #L.append([V[0], actualBoard])
            L.append([V[0], scenario])
            #L.append([V[0], V[1]])
            profmax += 1

        if player == min:
           #actualBoard = minimum(L)
           return minimum(L)
        if player == max:
           #actualBoard = maximum(L)
           return maximum(L)


# =================================================================================