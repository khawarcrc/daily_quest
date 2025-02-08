#  What is Minesweeper?
# Minesweeper is a classic puzzle game played on a grid (a board with rows and columns).
# Every cell on the board is either:
# - A mine (), or
# - An empty cell (which could be surrounded by 0 to 8 mines)
#
# The goal of the game is to click on the cells and avoid the mines.

#  What Happens When You Click a Cell?
# Imagine this:
# You're playing on a grid, and every square is hidden (we represent that with "H").
# When you click on one, two things can happen:

# 1. You click a mine :
#    - Uh-oh! BOOM! 
#    - The game marks that mine with an "X" to show it exploded.

# 2. You click a safe spot:
#    - Now we need to figure out: how many mines are around that spot?
#    - Look at the 8 squares around the one you clicked (up, down, left, right, and diagonals).
#
#    a. If there are mines around:
#       - You just show the number of mines near you (like “1”, “2”, ..., “8”).
#
#    b. If there are no mines around:
#       - You show a "0", and then (this is the cool part)...
#       - You automatically reveal all the nearby hidden cells, because they are safe too!
#       - This revealing continues recursively (like a ripple effect) until it hits spots that are next to mines.

# How the Code Helps Solve It

# 1. The board:
# [
#     ["H", "H", "H", "H"],
#     ["H", "M", "H", "H"],
#     ["H", "H", "H", "H"],
#     ["M", "H", "H", "H"],
# ]
# - "H" → hidden cell
# - "M" → mine
# - "X" → clicked mine (BOOM!)
# - "0" → revealed safe cell with 0 mines around
# - "1", "2", etc. → number of mines near that cell

# 2. The click:
# When you call:
#     revealMinesweeper(test_board, 0, 0)
# You're saying:
#     "Click on row 0, column 0. What do we reveal?"

# 3. What the function does:
# - Checks if it's a mine? If yes → mark it with "X" and stop.
# - If not, look at the 8 neighboring cells.
# - Count how many of them are mines ("M").
# - If it finds any → show that number on the cell.
# - If it finds zero mines nearby:
#     → mark the cell as "0"
#     → then repeat this process for all neighboring hidden cells (recursive ripple effect)

#  Why Use Recursion?
# Because if the clicked cell is safe ("0"), we want to automatically reveal all nearby safe areas too —
# without clicking each one manually. Recursion helps the computer do that:
#     “Hey, this spot is safe — go check all my neighbors too,
#     and if they are safe, check their neighbors!”

#  Real-life Analogy
# Imagine you're clearing snow off your driveway.
# - If you start and find clear pavement, you keep clearing around you.
# - But if you hit a rock (a mine), you stop.
# - And if the cleared area is surrounded by other safe zones?
#   You keep going until you're done.

#  Final Goal of This Problem
# Write a function that:
# - Reveals what happens when you click a cell.
# - If it's a mine → show "X".
# - If it's safe → show the number of nearby mines.
# - If it's safe and has no nearby mines → reveal it and its safe neighbors,
#   and their neighbors, and so on...



def revealMinesweeper(board, row, column):
    print(f"\nClicked cell: ({row}, {column}) -> {board[row][column]}")

    # If the clicked cell is a mine, return the board with the cell marked 'X'
    if board[row][column] == "M":
        print(">>> Mine found! Game Over.")
        board[row][column] = "X"
        return board

    # Get list of valid neighbor cell coordinates
    neighbors = getNeighbors(board, row, column)
    print(f"Valid neighbors of ({row}, {column}): {neighbors}")

    # Initialize mine count to zero
    adjacentMinesCount = 0

    # Count how many neighboring cells contain mines
    for neighborRow, neighborColumn in neighbors:
        if board[neighborRow][neighborColumn] == "M":
            adjacentMinesCount += 1

    print(f"Adjacent mines to ({row}, {column}): {adjacentMinesCount}")

    # If there are one or more adjacent mines, update the cell with the count
    if adjacentMinesCount > 0:
        board[row][column] = str(adjacentMinesCount)
        print(f"Updated cell ({row}, {column}) to count: {board[row][column]}")
    else:
        # If no adjacent mines, mark the cell as '0'
        board[row][column] = "0"
        print(f"No adjacent mines. Updated cell ({row}, {column}) to '0'")

        # Recursively reveal all hidden ('H') neighboring cells
        for neighborRow, neighborColumn in neighbors:
            if board[neighborRow][neighborColumn] == "H":
                print(f"Revealing neighbor cell: ({neighborRow}, {neighborColumn})")
                revealMinesweeper(board, neighborRow, neighborColumn)

    # Return the updated board
    return board


def getNeighbors(board, row, column):
    # 8 directions: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    neighbors = []

    # Loop through each direction
    for directionRow, directionColumn in directions:
        newRow = row + directionRow
        newColumn = column + directionColumn

        if 0 <= newRow < len(board) and 0 <= newColumn < len(board[0]):
            neighbors.append((newRow, newColumn))

    return neighbors


# ---------------------- Dummy Test Data ----------------------

test_board = [
    ["H", "H", "H", "H"],
    ["H", "M", "H", "H"],
    ["H", "H", "H", "H"],
    ["M", "H", "H", "H"],
]

# Example click on cell (0, 0)
updated_board = revealMinesweeper(test_board, 0, 0)

# Print the result
print("\nFinal Board:")
for row in updated_board:
    print(row)
