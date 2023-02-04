# SuperQueens
# By Ian McKechnie
# Sunday, January 29, 2023


best_brd = []
best_collisions = 0

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
        return n + 1

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
                        break

                # Check diagonally up and to the left
                row = i
                column = j
                while (row - 1 >= 0 and column - 1 >= 0 ):
                    row -= 1
                    column -= 1
                    if board[row][column] == "Q":
                        hits += 1
                        break

                # Check diagonally down and to the left
                row = i
                column = j
                while (row + 1 < n and column - 1 >= 0 ):
                    row += 1
                    column -= 1
                    if board[row][column] == "Q":
                        hits += 1
                        break


                # Check diagonally down and to the right
                row = i
                column = j
                while (row + 1 < n and column + 1 < n ):
                    row += 1
                    column += 1
                    if board[row][column] == "Q":
                        hits += 1
                        break

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

    return hits / 2


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


#Pops the queen off the board given the Column
def popQueen(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            board[i][column] = "."
            return board


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


# def getQueensRow(board, column):
#     for i in range(len(board)):
#         if board[i][column] == "Q":
#             return i


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

            if queenInRow == False and canMoveRight == True:
                return 0

    if canMoveLeft and canMoveRight:
        #Check if it's already at the bottom
        if column == 0 and isQueenAtBottom(board, column):
            return 2
        else:
            return 0

    if not canMoveRight:
        return 1

    if not canMoveLeft:
        return -1


def isInEndState(board):
    reversedArr = []

    for i in range(len(board)): #Rows
        reverseRow = board[i][::-1]
        reversedArr.append(reverseRow)

    for i in range(len(board)):
        for j in range(len(board)):

            if i == j and reversedArr[i][j] != "Q":
                return False
    return True

def saveState(cur_board, collisions):
    global best_brd
    global best_collisions

    if collisions < best_collisions:
        best_brd = []

        for i in range(len(cur_board)):
            best_brd.append([])

            for j in range(len(cur_board)):
                if cur_board[i][j] == "Q":
                    best_brd[i].append("Q")
                else:
                    best_brd[i].append(".")

        best_collisions = collisions


def superQueens(cur_board, best_board, size, column):

    if isQueenAtBottom(cur_board,column) == True and board[len(board) - 1][0] != "Q":
        popQueen(cur_board, column)
        #best_board, conflicts = superQueens(cur_board, best_board, size, column - 1)
        return column - 1

    # Can't move down
    else:

        #Check if it's able to move down right now
        ans = canMoveDown(cur_board, column)

        if ans == 0: # It's able to move down
            moveQueenDown(cur_board, column)

            for i in range(column + 1, len(cur_board)):
                placeQueen(cur_board, i)

            collisions = countCollisions(cur_board)
            saveState(cur_board, collisions)

            #return superQueens(cur_board, best_board, size, column + 1)
            return column + 1

        elif ans == 1: # It's not able to due to queens on the right
            for i in range(column + 1, size):
                popQueen(cur_board, i)

            moveQueenDown(cur_board, column)

            for i in range(column + 1, size):
                placeQueen(cur_board, i)

            collisions = countCollisions(cur_board)
            saveState(cur_board, collisions)

            #best_board, conflicts = superQueens(cur_board, best_board, size, column + 1)
            return column + 1


        elif ans == -1: # It's not able to due to queens on the left
            for i in range(column, len(cur_board)):
                popQueen(cur_board, i)

            #best_board, conflicts = superQueens(cur_board, best_board, size, column - 1)
            return column -1

        elif ans == 2:
            for i in range(column + 1, size):
                placeQueen(cur_board, i)

            return column + 1

            #best_board, conflicts = superQueens(cur_board, best_board, size, column - 1)


    return column -1

while True:
    try:
        n = int(input("Enter the size of the board (NxN board): "))
    except:
        print("Invalid input, please enter a number")
        continue

    break


if n == 0:
    print("Best Board:")
    print("Conflicts: 0")
    exit()

if n == 1:
    print("Best Board:")
    print("Q")
    print("Conflicts: 0")
    exit()

board = createBoard(n)
best_board = createBoard(n)
best_collisions = n

ans = n - 1
while(isInEndState(board) == False):
    ans = superQueens(board, best_board, n, ans)


print("Best Board: ")
printBoard(best_brd)
# print("board")
# printBoard(board)
print("Conflicts: ", best_collisions)