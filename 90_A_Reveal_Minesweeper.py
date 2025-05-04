 # ---------------------- Problem Statement & Execution Theory ----------------------
# '''
# Problem Statement:
# You are given a 2D board representing a Minesweeper game. Each cell can be:
# - 'H' (Hidden)
# - 'M' (Mine)
# - '0'–'8' (Revealed number indicating how many adjacent mines exist)

# You are given a starting point (row, coloumn) where the user clicks.
# If the cell is a mine ('M'), return the board as it is.
# If it's not a mine:
#   - Count adjacent mines.
#   - If at least one mine is adjacent, reveal the count.
#   - If no adjacent mines, reveal it as '0' and recursively reveal all hidden neighbors.

# Execution Theory:
# 1. Check if the clicked cell is a mine. If yes, return board unchanged.
# 2. Get all 8-directional neighbors using `getNeighbors`.
# 3. Count how many neighbors are mines.
# 4. If mines exist, set the current cell to the count.
# 5. If no mines, mark it '0' and recursively reveal all hidden neighbors.
# '''

# ---------------------- Function to Reveal Minesweeper Cells ----------------------

def revealMinesweeper(board, row, coloumn): 
    # If the clicked cell is a mine, return the board unchanged
    if board[row][coloumn] == 'M':
        return board
    
    # Get list of valid neighbor cell coordinates
    neighbors = getNeighbors(board, row, coloumn)
    
    # Initialize mine count to zero
    adjacentMinesCount = 0

    # Count how many neighboring cells contain mines
    for neighborRow, neighborColoumn in neighbors:
        if board[neighborRow][neighborColoumn] == 'M':
            adjacentMinesCount += 1

    # If there are one or more adjacent mines, update the cell with the count
    if adjacentMinesCount > 0: 
        board[row][coloumn] = str(adjacentMinesCount)
    else:
        # If no adjacent mines, mark the cell as '0'
        board[row][coloumn] = '0'
        # Recursively reveal all hidden ('H') neighboring cells
        for neighborRow, neighborColoumn in neighbors:
            if board[neighborRow][neighborColoumn] == 'H':
                revealMinesweeper(board, neighborRow, neighborColoumn)

    # Return the updated board
    return board


# ---------------------- Helper Function to Get Valid Neighbors ----------------------

def getNeighbors(board, row, coloumn):
    # 8 directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    neighbors = []

    # Loop through each direction
    for directionRow, directionColoumn in directions:
        # Calculate new row and column indices
        newRow = row + directionRow
        newColoumn = coloumn + directionColoumn

        # Check if new position is within board boundaries
        if 0 <= newRow < len(board) and 0 <= newColoumn < len(board[0]):
            neighbors.append((newRow, newColoumn))

    # Return list of valid neighbors
    return neighbors

# ---------------------- Dummy Test Data ----------------------

# 'H' = Hidden, 'M' = Mine
test_board = [
    ['H', 'H', 'H', 'H'],
    ['H', 'M', 'H', 'H'],
    ['H', 'H', 'H', 'H'],
    ['M', 'H', 'H', 'H']
]

# Example click on cell (0, 0)
updated_board = revealMinesweeper(test_board, 0, 0)

# Print the result
for row in updated_board:
    print(row)
