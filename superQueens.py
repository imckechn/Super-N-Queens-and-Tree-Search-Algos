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

                print("Hits after, ", hits)
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


def moveQueen(n, board, level, conflicts, pos, bestBoad):
    if level == 0:
        return bestBoad, conflicts

    #If you can shift the piece left by 1 on it's original row, do it
    if pos[0] - 1 >= 0 and pos[1] == level - 1:
        newPos = [pos[0] - 1, pos[1]]

    #If you cannot shift it left anymore because it's at the left most position, return it and shift it upwards
    elif pos[0] == 0 and pos[1] == level - 1:
        newPos = pos[level - 1, pos[1] - 1]

    #If you've already shift it left, trying moving it up
    elif pos[1] - 1 >= 0 and pos[0] == level - 1:
        newPos = [pos[0], pos[1] - 1]

    #if you've tried going all the way left, and all the way right, reset it and go one level higher
    else:
        newPos = [level - 1, level - 1]

    if newPos != [level - 1, level - 1]:
        #Validate if the move is legal
        if isValid(board, newPos):
            newBoard = board.copy()

            newBoard[pos[0]][pos[1]] = "."
            newBoard[newPos[0]][newPos[1]] = "Q"
            colisions = countColisions(newBoard, n)

            if colisions < conflicts:
                bestBoad = newBoard.copy()
                conflicts = colisions

        return moveQueen(n, board, level, conflicts, newPos, bestBoad)

    else:
        board[pos[0]][pos[1]] = "."
        board[newPos[0]][newPos[1]] = "Q"

        return moveQueen(n, board, level - 1, conflicts, [pos[0] - 1, pos[1] - 1], bestBoad)

# Moves the queen down one row, if at the bottom, returns None
def moveQueenDown(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            if i + 1 < len(board):
                board[i][column] = "."
                board[i + 1][column] = "Q"
                return board
            else:
                return None

#Pops the queen off the board given the Column
def popQueen(board, row):
    for i in range(len(board)):
        if board[row][i] == "Q":
            board[row][i] = "."
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

    return None


def superQueens(cur_board, best_board, size, conflicts, row):
    if row == -1:
        return cur_board, conflicts

    if moveQueenDown(cur_board, row) is None: #If you cannot move the queen down a slot in a legal move
        cur_board = popQueen(cur_board, row) #Pop the queen off the board
        return superQueens(cur_board, best_board, size, conflicts, row - 1) #Move to the next queen

    else:
        for i in range(row, size - 1):
            cur_board = placeQueen(cur_board, i)

        best_board, conflicts = countColisions(cur_board, size)

        for i in range(row, size - 1):
            cur_board = popQueen(cur_board, i)

        return superQueens(cur_board, best_board, size, conflicts, row + 1)


#n = input("Enter the size of the board (NxN board): ")
n = 4
n = int(n)

board = createBoard(n)
#board, conflicts = superQueens(board, n)

board = [
    ["Q", ".", ".", "."],
    [".", "Q", ".", "."],
    [".", ".", "Q", "."],
    [".", ".", ".", "Q"]
]

board, conflicts = superQueens(board, board, n, n - 1, n - 1)

print("Board: ")
for i in range(len(board)):
    print(board[i])

print("Conflicts: ", conflicts)
