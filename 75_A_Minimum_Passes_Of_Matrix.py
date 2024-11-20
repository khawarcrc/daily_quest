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

# Execution Theory:
# - `minimumPassesOfMatrix`: Controls the flow of the program. It checks if negative values remain 
#   after completing the passes and calculates the total passes.
# - `convertNegatives`: Executes the BFS, converting adjacent negative cells in each pass and counting passes.
# - `getAllPositivePositions`: Identifies the initial positive cells in the matrix.
# - `getAdjacentPositions`: Determines the valid neighboring cells for a given cell.
# - `containsNegative`: Checks if any negative values remain in the matrix after processing.

# Example Matrix:
# Input:
# [
#   [0, -1, -3, 2, 0],
#   [1, -2, -5, -1, -3],
#   [3, 0, 0, -4, -1]
# ]
# Expected Output: The minimum number of passes required to convert all negative cells, or -1 if not possible.
# The code tracks each transformation step and calculates the total passes required.

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
