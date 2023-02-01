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

# Moves the queen down one row, if at the bottom, returns None
def moveQueenDown(board, column):
    print("Type of board: ", type(board))
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

    print("ERROR, NO QUEEN FOUND")
    print(board)


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
    print("LOOPS")
    print("Current board: ", cur_board)
    print("Best board: ", best_board)
    print("Size: ", size)
    print("Conflicts: ", conflicts)
    print("Row: ", row)

    if row <= -1:
        return cur_board, conflicts

    #If you cannot move the queen down a slot in a legal move, ie. it's at the bottom
    if moveQueenDown(cur_board, row) is None:
        print("row being passed = ", row)
        cur_board = popQueen(cur_board, row) #Pop the queen off the board
        print("Calling loop on row: ", row - 1)
        return superQueens(cur_board, best_board, size, conflicts, row - 1) #Move to the next queen

    else:
        for i in range(row, size - 1):
            cur_board = placeQueen(cur_board, i)

        print("row = ", row)
        print("size -1 = ", size - 1)
        print("cur_board: ", cur_board)

        colisions = countColisions(cur_board, size)
        if colisions < conflicts:
            best_board = cur_board.copy()
            conflicts = colisions

        for i in range(row, size - 1):
            cur_board = popQueen(cur_board, i)

        print("Calling loop on row: ", row + 1)
        print("calling from here------------------")
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
