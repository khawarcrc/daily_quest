# Problem Statement:
# You are given a 2D matrix of integers where each integer represents the value of a cell.
# Positive integers represent "positive cells," negative integers represent "negative cells," 
# and zeroes are neutral cells. 
# In one "pass," all negative cells adjacent (vertically or horizontally) to positive cells 
# are converted into positive cells.
# The goal is to determine the minimum number of passes required to convert all negative cells 
# into positive cells. If it is not possible to convert all cells to positive, return -1.

# Code Explanation:
# 1. The program works by simulating "passes" through the matrix. Each pass looks for all negative cells 
#    adjacent to positive cells and converts them into positive cells.
# 2. It uses a breadth-first search (BFS) approach where the positions of all current positive cells are tracked 
#    and their adjacent negative cells are processed.
# 3. The process continues until there are no more negative cells that can be converted or all passes are completed.
# 4. Finally, if any negative cell remains in the matrix, it indicates the transformation is impossible.

# Execution Theory (Detailed):
# 
# 1. `minimumPassesOfMatrix`:
#    - **Purpose**: Acts as the main controller function. It orchestrates the entire process 
#      of determining how many passes are required to convert all negative cells to positive.
#    - **Key Steps**:
#      - Calls `convertNegatives` to perform the BFS passes, returning the total number of passes.
#      - Checks if any negative value remains in the matrix after all passes using `containsNegative`.
#      - If negative values remain, returns -1 (impossible to convert all cells). 
#        Otherwise, returns the total number of passes minus 1, as the last pass may not make a change.
#    - **How It Works**:
#      - It receives the matrix as input, calculates the result based on other functions, 
#        and provides the final output.

# 2. `convertNegatives`:
#    - **Purpose**: Implements the BFS to simulate each "pass" of converting adjacent negative cells.
#    - **Key Steps**:
#      - Calls `getAllPositivePositions` to find all positive cells' coordinates in the matrix initially.
#      - While the `nextPassQueue` (cells to process in the next pass) is not empty:
#          - Copies the `nextPassQueue` to `currentPassQueue` for processing.
#          - Resets `nextPassQueue` to store new positive cells for the next pass.
#          - For each cell in `currentPassQueue`, calls `getAdjacentPositions` to find valid neighboring cells.
#          - Checks if an adjacent cell is negative:
#              - Converts it to positive by multiplying the value by -1.
#              - Adds the newly converted cell to `nextPassQueue`.
#          - Continues until no new cells can be processed.
#      - Returns the total number of passes.
#    - **How It Works**:
#      - The BFS ensures that all adjacent negative cells are processed in the same "pass."
#      - By repeatedly processing the `nextPassQueue`, it simulates spreading positivity step-by-step.

# 3. `getAllPositivePositions`:
#    - **Purpose**: Finds and returns a list of coordinates (row, col) of all positive cells in the matrix.
#    - **Key Steps**:
#      - Loops through each cell in the matrix using nested loops:
#          - Outer loop iterates through rows, inner loop iterates through columns.
#          - Checks if the cell value is positive (value > 0).
#          - If positive, appends its [row, col] coordinates to the list `positivePositions`.
#      - Returns the list of all positive cells.
#    - **How It Works**:
#      - Scans the entire matrix to identify positive cells at the beginning of the process.
#      - These positions are used as the starting points for the BFS in `convertNegatives`.

# 4. `getAdjacentPositions`:
#    - **Purpose**: Returns a list of valid adjacent cell coordinates for a given cell in the matrix.
#    - **Key Steps**:
#      - Checks the four possible directions (up, down, left, right) from the current cell:
#          - Ensures the adjacent positions do not go out of matrix bounds.
#          - Adds the valid positions to the list `adjacentPositions`.
#      - Returns the list of valid positions.
#    - **How It Works**:
#      - For each cell, this function determines its neighbors, enabling BFS to spread positivity correctly.
#      - Ensures no invalid indices are accessed, preventing errors.

# 5. `containsNegative`:
#    - **Purpose**: Determines if any negative value remains in the matrix.
#    - **Key Steps**:
#      - Loops through each row in the matrix:
#          - For each row, loops through each value.
#          - Checks if the value is negative (value < 0).
#          - If a negative value is found, immediately returns `True`.
#      - If no negatives are found, returns `False`.
#    - **How It Works**:
#      - Acts as a final verification step to check if the process was successful.
#      - Prevents unnecessary passes or incorrect results.

# **How the Queue System Works in BFS**:
# - The `nextPassQueue` keeps track of cells to process in the next pass. It ensures that the BFS processes 
#   cells level by level (or pass by pass).
# - Initially, `nextPassQueue` is populated with all positive cells.
# - During each pass:
#     - The current cells to process are stored in `currentPassQueue`.
#     - As their neighbors are processed and converted, new cells are added to `nextPassQueue`.
# - This cycle continues until no more cells are left to process.

# **Summary of Matrix Transformation**:
# - The matrix transformation starts with all initial positive cells.
# - In each pass, positive cells spread to their adjacent negative cells.
# - Each pass reduces the total number of negative cells until none remain (or it's impossible to convert all).

# **Dummy Example Walkthrough**:
# Matrix before any passes:
# [
#   [0, -1, -3, 2, 0],
#   [1, -2, -5, -1, -3],
#   [3,  0,  0, -4, -1]
# ]
# Pass 1:
# - Initial positives: [(0, 3), (1, 0), (2, 0)]
# - Converted negatives: [(0, 2), (1, 1)]
# Matrix after Pass 1:
# [
#   [0, -1,  3,  2,  0],
#   [1,  2, -5, -1, -3],
#   [3,  0,  0, -4, -1]
# ]
# ...
# Process continues until all negatives are converted or no further conversion is possible.


def minimumPassesOfMatrix(matrix):
    # Function to control the process and return the final number of passes
    passes = convertNegatives(matrix)
    # If negative values remain, return -1; otherwise, return the passes count
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    # BFS to transform negative cells into positive cells
    nextPassQueue = getAllPositivePositions(matrix)  # Initial positive cells
    passes = 0

    while len(nextPassQueue) > 0:
        # Process cells for the current pass
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        while len(currentPassQueue) > 0:
            currentRow, currentCol = currentPassQueue.pop(0)

            # Get valid adjacent positions
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position

                value = matrix[row][col]
                if value < 0:
                    # Convert negative to positive and add to the queue for the next pass
                    matrix[row][col] *= -1
                    nextPassQueue.append([row, col])

        passes += 1  # Increment pass count
    return passes

def getAllPositivePositions(matrix):
    # Identify initial positive cell positions
    positivePositions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row, col])
    return positivePositions

def getAdjacentPositions(row, col, matrix):
    # Get valid adjacent positions for a given cell
    adjacentPositions = []

    if row > 0:
        adjacentPositions.append([row - 1, col])
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])

    if col > 0:
        adjacentPositions.append([row, col - 1])
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])

    return adjacentPositions

def containsNegative(matrix):
    # Check if any negative values remain in the matrix
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False

# Dummy Data for Testing
matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

# Test the function with the dummy matrix
result = minimumPassesOfMatrix(matrix)
print(f"Minimum passes required: {result}")
