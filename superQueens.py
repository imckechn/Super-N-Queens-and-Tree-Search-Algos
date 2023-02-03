# SuperQueens
# By Ian McKechnie
# Sunday, January 29, 2023

def createBoard(n):
    board = []
    for i in range(n):
        board.append([])
        for j in range(n):
            if i == j:
                board[i].append("Q")
            else:
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


def countCollisions(board):
    hits = 0
    n = len(board)

    queenCount = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q":
                queenCount += 1

    if queenCount != n:
        return n

    printBoard(board)
    print("QueenCount = ", queenCount)

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

#Moves queen down to the next open row, in the same column as before
def moveQueenDown(board, column):

    oldPos = []
    queenFound = False
    for i in range(len(board)):
        if board[i][column] == "Q":
            oldPos = [i, column]
            queenFound = True
            continue

        if queenFound:
            isRowClear = True
            for j in range(len(board)):
                if board[i][j] == "Q":
                    isRowClear = False
                    break

            if isRowClear:
                board[oldPos[0]][oldPos[1]] = "."
                board[i][column] = "Q"
                return True

    return None


    for i in range(len(board)):
        if board[i][column] == "Q":
            if i + 1 < len(board):
                board[i][column] = "."
                board[i + 1][column] = "Q"
                return board, True

    return board, False

#Pops the queen off the board given the Column
def popQueen(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            board[i][column] = "."
            return board

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
            return board

    return board


def isQueen(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            return True
        return False


# Checks if the queen in the given column can move down
# Board is the current board
# Column is the exact column where the queen is located
# Returns 0 if it can move down
# Returns 1 if it can't move down due to a Queen on the right
# Returns -1 if it can't move down due to a Queen on the left
def canMoveDown(board, column):
    #Need to check if there is open rows on the board when only looking to the right side of the current Queen
    queenFound = False
    canMoveRight = True
    for i in range(len(board)):
        if board[i][column] == "Q":
            queenFound = True
            continue

        if queenFound:
            queenInRow = False
            for j in range(column + 1, len(board)):
                if board[i][j] == "Q":
                    queenInRow = True
                    break

            if queenInRow:
                canMoveRight = False
                break


    # Need to check if there is open rows on the board when only looking to the left side of the current Queen
    queenFound = False
    canMoveLeft = True
    for i in range(len(board)):
        if board[i][column] == "Q":
            queenFound = True
            continue

        if queenFound:
            queenInRow = False
            for j in range(0, column):
                if board[i][j] == "Q":
                    queenInRow = True
                    break

            if queenInRow:
                canMoveLeft = False
                break

    if canMoveLeft and canMoveRight:
        return 0

    if not canMoveRight:
        return 1

    if not canMoveLeft:
        return -1



def superQueens(cur_board, best_board, size, conflicts, column):
    # print("LOOPS")
    # print("Size: ", size)
    # print("Conflicts: ", conflicts)
    # print("column: ", column)
    # print("Current board: ")
    # printBoard(cur_board)
    # print("Best board: ")
    # printBoard(best_board)


    if column == -1:
        if size == 1:
            return best_board, 0
        if size == 0:
            return best_board, 0

        return best_board, conflicts


    if isQueenAtBottom(cur_board,column) == True:
        popQueen(cur_board, column)
        best_board, conflicts = superQueens(cur_board, best_board, size, conflicts, column - 1)

    # Can't move down
    else:

        #Check if it's able to move down right now
        ans = canMoveDown(cur_board, column)

        if ans == 0: # It's able to move down
            moveQueenDown(cur_board, column)

            for i in range(column + 1, len(cur_board)):
                placeQueen(cur_board, i)

            collisions = countCollisions(cur_board)
            if collisions < conflicts:
                conflicts = collisions
                best_board = cur_board

            best_board, conflicts = superQueens(cur_board, best_board, size, conflicts, column + 1)
            return best_board, conflicts
            for i in range(column, len(cur_board)):
                popQueen(cur_board, i)

            best_board, conflicts = superQueens(cur_board, best_board, size, conflicts, column - 1)

        elif ans == 1: # It's not able to due to queens on the right
            for i in range(column + 1, size):
                popQueen(cur_board, i)

            moveQueenDown(cur_board, column)

            for i in range(column + 1, size):
                placeQueen(cur_board, i)

            collisions = countCollisions(cur_board)
            if collisions < conflicts:
                conflicts = collisions
                best_board = cur_board

            best_board, conflicts = superQueens(cur_board, best_board, size, conflicts, column + 1)


        elif ans == -1: # It's not able to due to queens on the left
            for i in range(column, len(board)):
                popQueen(cur_board, i)

            best_board, conflicts = superQueens(cur_board, best_board, size, conflicts, column - 1)

    return best_board, conflicts

while True:
    try:
        n = int(input("Enter the size of the board (NxN board): "))
    except:
        print("Invalid input, please enter a number")
        continue

    break

board = createBoard(n)
best_board = createBoard(n)

# board = [
#     ["Q", ".", "."],
#     [".", "Q", "."],
#     [".", ".", "Q"]
# ]
# best_board = [
#     ["Q", ".", "."],
#     [".", "Q", "."],
#     [".", ".", "Q"]
# ]
# n = 3


# printBoard(board)
# print("n = ", n)


best_board, conflicts = superQueens(board, best_board, n, n, n - 1)
print("Best Board: ")
printBoard(best_board)

print("Conflicts: ", conflicts)
