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


                # print("Checking " + str(row) + " " + str(column) + " = " + board[row][column])
                print("Hits b4, ", hits)
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
        #Need to check if this move is vali -> cannot be in the same row or column as another queen

        newBoard = board.copy()

        newBoard[pos[0]][pos[1]] = "."
        newBoard[newPos[0]][newPos[1]] = "Q"
        colisions = countColisions(newBoard, n)

        if colisions < conflicts:
            bestBoad = newBoard.copy()
            conflicts = colisions
        return moveQueen(n, newBoard, level, conflicts, newPos, bestBoad)

    else:
        board[pos[0]][pos[1]] = "."
        board[newPos[0]][newPos[1]] = "Q"

        moveQueen(n, board, level - 1, conflicts, [pos[0] - 1, pos[1] - 1], bestBoad)



def superQueens(board, size):
    conflicts = size
    board, conflicts = moveQueen(n, board, size, conflicts, [size - 1, size - 1])


#n = input("Enter the size of the board (NxN board): ")
n = 4
n = int(n)

board = createBoard(n)
#board, conflicts = superQueens(board, n)

board = [
    [".", ".", ".", "Q"],
    [".", ".", "Q", "."],
    [".", "Q", ".", "."],
    ["Q", ".", ".", "."]
]


print(countColisions(board, n))
#print("Number of conflicts: ", str(conflicts))