## This program simulates a simple 3x3 game of Tic-Tac-Toe
# @author Jordan Phommachack
def main():
    NUM_ROWS = NUM_COLS = 3
    MAX_TURNS = NUM_ROWS * NUM_COLS
    turnsTaken = 0
    isWinner = False
    board = CreateBoard()
    player = "O"
    
    while (not isWinner and turnsTaken < MAX_TURNS) :
        # Switch players 
        # (If player variable contained an O assign an "X", else assign an "O")
        if player == "O":
            player = "X"
        else:
            player = "O"
        # Show the board (Call the showBoard function)   
        ShowBoard(board)
        
        # Prompt for and retrieve the row and column for the player
        # (Be sure to match the output)
        print("Player %s Turn" % player)
        row = int(input("Row: "))
        col = int(input("Col: "))
        
        # Place the X or O on the board (Hint: use the value of player)
        board[row][col] = player
        # Increment # of turns and check for win (completed)
        turnsTaken = turnsTaken + 1
        isWinner = CheckWin(board, player)
    
    # Game is now over, so show the final board (Call showBoard function)
    ShowBoard(board)
    # Display who won or if it was a cat/tie. (Match the output)
    if isWinner == True:
        print("%s wins!" % player)
    elif turnsTaken == MAX_TURNS and isWinner == False:
        print("Tie!")
        
# showBoard shows a tic tac toe board in a table format
# @param board The tic tac toe board
def ShowBoard(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end= " ")
        print()

# createBoard creates a 3x3 tic-tac-toe board 
# where each element is initialized to a dash
# REQUIREMENT: Rather then just returning [ ["-", "-", "-"], ...], make this
# function a little bit more complex by using a loop that iterates 3 times and
# uses the append method from the list to append a row in each iteration
# @return the created board
def CreateBoard():
    ROWS = 3
    COLS = 3
    
    board = []
    for row in range(ROWS):
        nextRow = ["-"] * COLS
        board.append(nextRow)
    return board

# checkWin determines if a win occurred in a row, column, or diagonal
# @param board The Tic-Tac-Toe board
# @param player Contains an "X" or "O" representing a player
# @return True or False depending if the game is won 
def CheckWin(board, player):
    win = False
    #horizontal win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True
        
    for col in range(len(board)):
        check = []
        
        for row in board:
            check.append(row[col])
            
        if check.count(check[0]) == len(check) and check[0] != '-':
                return True
        
    #diagonial win
    if board[0][0] == ('X') and board[1][1] == ('X') and board [2][2] == ('X'):
        return True
    if board[0][0] == ('O') and board[1][1] == ('O') and board [2][2] == ('O'):
        return True
    
    #second diagonial win
    if board[0][2] == ('X') and board[1][1] == ('X') and board [2][0] == ('X'):
        return True
    if board[0][2] == ('O') and board[1][1] == ('O') and board [2][0] == ('O'):
        return True
        
    return False         
main()