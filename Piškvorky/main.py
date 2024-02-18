board = ["_", "_", "_",
        "_", "_", "_",
       "_", "_", "_"]
currentplayer = "x"
winner = None
Gamerun = True
# playing the bord game
def printboard (board):
    print("  " + "1 " + "  " + "2 " + "  " + "3")
    print("1 " + board[0] + " | " + board[1] + " | " + board[2]+"  position:" + " 1 / 2 / 3")
    print("2 " + board[3] + " | " + board[4] + " | " + board[5]+"  position:" + " 4 / 5 / 6")
    print("3 " + board[6] + " | " + board[7] + " | " + board[8]+"  position:" + " 7 / 8 / 9")

# take input
def playerInput (board):
    print(f"Look at the position of your turn {currentplayer} !")
    player_choice = (int(input("Enter a number 1-9:"))-1)
    if player_choice >= 0 and player_choice <= 8 and board[player_choice] == "_":
        board[player_choice] = currentplayer
    else:
        print("Place is already use")

# check for win
# check rows for the same symbols
def checkHorizontale(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[2] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "_":
        winner = board[6]
        return True

# check columns for the same symbols
def checkVertical (board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[3] != "_":
        winner = board[2]
        return True
# check angle for the same symbols
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

def checkDraw (board):
    global Gamerun
    if "_" not in board:
        printboard(board)
        print("The match ended in a draw")
        Gamerun = False

def checkWin (board):
    global Gamerun
    if checkDiagonal(board) or checkHorizontale(board) or checkVertical(board):
        print(f"The winner is {winner}")
        Gamerun = False

# switch player
def switchPlayer():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "0"
    else:
        currentplayer = "x"

# check for win or draw again
while Gamerun:
    printboard(board)
    playerInput(board)
    checkWin(board)
    checkDraw(board)
    switchPlayer()