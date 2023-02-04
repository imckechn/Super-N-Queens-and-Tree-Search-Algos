# SuperQueens
# By Ian McKechnie
# February 3rd, 2023


best_board = []
best_collisions = 0


# This function creates a board of size NxN and returns it
# @Params
# n is the size of the board
# Returns a board of size NxN
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


# This function prints the board to the console
# @Params
# board is the board to be printed
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "Q":
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()


# This function counts the number of collisions on the board
# * I've assumed a queen cannot pass through another queen for another hit *
# @Params
# board is the board to be checked
# Returns the number of collisions
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

    #Divide by 2 because Queen A hits Queen B and Queen B hits Queen A (Same collision counted twice)
    return hits / 2


# This function checks if a queen is at the bottom of the board
# @Params
# board is the board to be checked
# column is the column being checked

def isQueenAtBottom(board, column):
    if board[ len(board) - 1 ][column] == "Q":
        return True
    return False


# Moves queen down to the next open row, has error checking to make sure it's a valid move
# @Params
# board is the board to be checked
# column is the column being checked
# Returns True if the queen was moved, None if it was not
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


# Pops the queen off the board given the Column
# @Params
# board is the board to be checked
# column is the column being checked
# Returns the board with the queen popped off, otherwise, does nothing
def popQueen(board, column):
    for i in range(len(board)):
        if board[i][column] == "Q":
            board[i][column] = "."
            return board


#Places the queen in the first open row in that queens column
# @Params
# board is the board to be checked
# column is the column being checked
# Returns the board with the queen placed
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


# Checks if the board is in the end state (Queens are in a diagonal from the bottom let to the top right)
# @Params
# board is the board to be checked
# Returns True if the board is in the end state, False otherwise
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


# Checks if the state of the board has a lower amount of collisons than the current best board
# @Params
# cur_board is the current board
# collisions is the amount of collisions in the current board
# Returns nothing
def saveState(cur_board, collisions):

    #Saves to global variables
    global best_board
    global best_collisions

    if collisions < best_collisions:
        best_board = []

        for i in range(len(cur_board)):
            best_board.append([])

            for j in range(len(cur_board)):
                if cur_board[i][j] == "Q":
                    best_board[i].append("Q")
                else:
                    best_board[i].append(".")

        best_collisions = collisions


# Main Algorithm that finds the optimal solution to the Super Queens problem
def superQueens(cur_board, size, column):

    # If the queen is at the bottom of the board, and the top right section of the board does not have a queen
    if isQueenAtBottom(cur_board,column) == True and board[len(board) - 1][0] != "Q":

        # Pop off the current queen then run the next iteration on the column to the left
        popQueen(cur_board, column)
        return column - 1

    # Can't move down
    else:

        #Check if it's able to move down right now
        ans = canMoveDown(cur_board, column)

        if ans == 0: # It's able to move down
            moveQueenDown(cur_board, column)

            #Place the queens on the right
            for i in range(column + 1, len(cur_board)):
                placeQueen(cur_board, i)

            #Check if the current board state has lowest collisions, if so, save it
            collisions = countCollisions(cur_board)
            saveState(cur_board, collisions)

            #Run next iteration on the column to the right
            return column + 1

        elif ans == 1: # It's not able to due to queens on the right

            #Remove queens to the right
            for i in range(column + 1, size):
                popQueen(cur_board, i)

            #Move the queen down
            moveQueenDown(cur_board, column)

            #Place the queens on the right
            for i in range(column + 1, size):
                placeQueen(cur_board, i)

            #Check if the current board state has lowest collisions, if so, save it
            collisions = countCollisions(cur_board)
            saveState(cur_board, collisions)

            #Run next iteration on the column to the right
            return column + 1


        elif ans == -1: # It's not able to due to queens on the left

            #Pop the queen in the current row and all queens to the right
            for i in range(column, len(cur_board)):
                popQueen(cur_board, i)

            # Run the next iteration on the column to the left
            return column - 1

        # If the left most queen is at the bottom
        elif ans == 2:

            #Fill in the right side of the board with queens
            for i in range(column + 1, size):
                placeQueen(cur_board, i)

            #Run next iteration on the column to the right
            return column + 1

    # Run the next iteration on the column to the left
    return column - 1



# ------ Main Program ------

#Get user input and do basic error checking
while True:
    try:
        n = int(input("Enter the size of the board (NxN board): "))
    except:
        print("Invalid input, please enter a number")
        continue

    break


# If the board is 0x0 or 1x1, print the solution
if n == 0:
    print("Best Board:")
    print("Conflicts: 0")
    exit()

if n == 1:
    print("Best Board:")
    print("Q")
    print("Conflicts: 0")
    exit()

# Create the board and set worst case collisions
board = createBoard(n)
best_collisions = n

ans = n - 1
#Continuously run the algorithm until the board is in the end state, starting from the right most column
while(isInEndState(board) == False):
    ans = superQueens(board, n, ans)


# Print the best board and the amount of collisions
print("Best Board: ")
printBoard(best_board)
print("Conflicts: ", best_collisions)