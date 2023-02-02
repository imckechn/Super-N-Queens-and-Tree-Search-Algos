# SuperQueens
# By Ian McKechnie
# Sunday, January 29, 2023

def createBoard(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(".")

    return board


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "Q":
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()


def countColisions(board, n):
    hits = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q":
                # Check diagonally up and to the right
                row = i
                column = j
                while (row - 1 >= 0 and column + 1 < n ):
                    row -= 1
                    column += 1
                    if board[row][column] == "Q":
                        hits += 1

                # Check diagonally up and to the left
                row = i
                column = j
                while (row - 1 >= 0 and column - 1 >= 0 ):
                    row -= 1
                    column -= 1
                    if board[row][column] == "Q":
                        hits += 1

                # Check diagonally down and to the left
                row = i
                column = j
                while (row + 1 < n and column - 1 >= 0 ):
                    row += 1
                    column -= 1
                    if board[row][column] == "Q":
                        hits += 1


                # Check diagonally down and to the right
                row = i
                column = j
                while (row + 1 < n and column + 1 < n ):
                    row += 1
                    column += 1
                    if board[row][column] == "Q":
                        hits += 1

                # Now check fo the knight moves
                #Checking to the right of the piece
                row = i
                column = j
                if row - 2 >= 0 and column + 1 < n:
                    if board[row-2][column+1] == "Q":
                        hits += 1

                if row + 2 < n and column + 1 < n:
                    if board[row+2][column+1] == "Q":
                        hits += 1

                if row + 1 < n and column + 2 < n:
                    if board[row+1][column+2] == "Q":
                        hits += 1

                if row - 1 >= 0 and column + 2 < n:
                    if board[row-1][column+2] == "Q":
                        hits += 1

                if row - 2 >= 0 and column - 1 >= 0:
                    if board[row-2][column-1] == "Q":
                        hits += 1

                if row + 2 < n and column - 1 >= 0:
                    if board[row+2][column-1] == "Q":
                        hits += 1

                if row + 1 < n and column - 2 >= 0:
                    if board[row+1][column-2] == "Q":
                        hits += 1

                if row - 1 >= 0 and column - 2 >= 0:
                    if board[row-1][column-2] == "Q":
                        hits += 1
    return hits/n


def isValid(board, pos):
    #Check if there is a queen in the same row
    for i in range(len(board)):
        if board[pos[0]][i] == "Q":
            return False

    #Check if there is a queen in the same column
    for i in range(len(board)):
        if board[i][pos[1]] == "Q":
            return False

    return True

def isQueenAtBottom(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            if i + 1 == len(board):
                return True

    return False

# Moves the queen down one row, if at the bottom, returns None
def moveQueenDown(board, column):
    print("Type of board: ", type(board))
    for i in range(len(board)):
        if board[i][column] == "Q":
            if i + 1 < len(board):
                board[i][column] = "."
                board[i + 1][column] = "Q"
                print("Moving queen down at: ", i, column)
                printBoard(board)
                return board, True
            

    print("Queen at bottom")
    printBoard(board)
    return board, False

#Pops the queen off the board given the Column
def popQueen(board, row):
    print("Poping queen at: ", row, "")
    printBoard(board)
    for i in range(len(board)):
        if board[row][i] == "Q":
            board[row][i] = "."
            print("Popping queen at: ", row, i)
            printBoard(board)
            return board

    print("ERROR, NO QUEEN FOUND")
    printBoard(board)


#Places the queen in the first open row in that queens column
def placeQueen(board, column):
    for i in range(len(board)): #Loop through each row
        hasQueen = False
        for j in range(column): #Loop through each column until you reach the column where the queen will be placed
            if board[i][j] == "Q":
                hasQueen = True
                break

        if not hasQueen:
            board[i][column] = "Q"

            print("Placing queen at: ", i, column)
            printBoard(board)
            return board

    print("---------Placing queen failed")
    return board


def isQueen(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            return True
        return False


def superQueens(cur_board, best_board, size, conflicts, row):
    print("LOOPS")
    print("Size: ", size)
    print("Conflicts: ", conflicts)
    print("Row: ", row)
    print("Current board: ")
    printBoard(cur_board)
    print("Best board: ")
    printBoard(best_board)

    if row == size - 1:
        popQueen(cur_board, row)
        return best_board, conflicts

    if row == size:
        return best_board, conflicts

    if isQueenAtBottom(cur_board, row) is False:
        cur_board, sucess  = moveQueenDown(cur_board, row)

        if sucess is False:
            superQueens(cur_board, best_board, size, conflicts, row + 1)
            moveQueenDown(cur_board, row)
            for i in range(row + 1, size):
                placeQueen(cur_board, i)

            conflicts = countColisions(cur_board, size)
            if conflicts < best_conflicts:
                best_board = cur_board
                best_conflicts = conflicts

            superQueens(cur_board, best_board, size, conflicts, row + 1)


    # if row == -1 or conflicts == 0:
    #     return best_board, conflicts

    # #Remove all the queens after the current row

    # while True:
    #     for i in range(row + 1, size):
    #         popQueen(cur_board, i)

    #     cur_board, bottomOfBoard = moveQueenDown(cur_board, row)

    #     for i in range(row + 1, size):
    #         placeQueen(cur_board, i)
    #     if bottomOfBoard == True:
    #         print("At bottom")
    #         break

    #     cur_conflicts = countColisions(cur_board, size)
    #     if cur_conflicts < conflicts:
    #         best_board = cur_board
    #         conflicts = cur_conflicts



    # return superQueens(cur_board, best_board, size, conflicts, row - 1)


#n = input("Enter the size of the board (NxN board): ")

n = 2
n = int(n)

#board = createBoard(n)
#board, conflicts = superQueens(board, n)

board = [
    ["Q", "."],
    [".", "Q"]
]

board, conflicts = superQueens(board, board, n, n - 1, 0)

print("Best Board: ")
printBoard(board)

print("Conflicts: ", conflicts)
