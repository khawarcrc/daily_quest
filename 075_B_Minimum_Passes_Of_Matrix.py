# """
# Problem Statement:
# You are given a 2D matrix where each cell contains either a positive, negative, or zero value.
# - Positive values can "convert" adjacent negative values (top, bottom, left, right) into positive values in a single pass.
# - The goal is to determine the minimum number of passes required to convert all negative values to positive values. 
# If it is not possible to convert all negative values, return -1.

# Example:
# Matrix:
# [
#     [0, -1, -3, 2, 0],
#     [1, -2, -5, -1, -3],
#     [3, 0, 0, -4, -1]
# ]
# Output: 4
# Explanation:
# - In each pass, all adjacent negatives are converted to positives by their neighboring positives. This process repeats until no negatives remain.
# """



def minimumPassesOfMatrix(matrix):
    """
    Controls the process and returns the final number of passes required.
    - If negative values remain after processing, returns -1.
    """
    passes = convertNegatives(matrix)  # Transform negative values into positives
    # Check if any negative value remains. If yes, return -1; else, return the passes count.
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    """
    Performs a BFS to convert negative values into positive values.
    Uses a single queue to track cells to be processed.
    """
    queue = getAllPositivePositions(matrix)  # Initialize queue with all positive positions
    passes = 0  # Initialize pass count

    # Continue processing until no more cells to process
    while len(queue) > 0:
        currentSize = len(queue)  # Number of cells to process in the current pass
        madeProgress = False  # Track if any changes are made during this pass

        while currentSize > 0:
            currentRow, currentCol = queue.pop(0)  # Dequeue the next cell
            # Get all valid adjacent positions
            adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix)
            for position in adjacentPositions:
                row, col = position
                value = matrix[row][col]
                if value < 0:
                    # Convert negative to positive and enqueue the position
                    matrix[row][col] *= -1
                    queue.append([row, col])
                    madeProgress = True
            currentSize -= 1  # Decrement the count of cells to process in this pass

        if madeProgress:
            passes += 1  # Increment the pass count if changes occurred

    return passes

def getAllPositivePositions(matrix):
    """
    Identifies all initial positive cell positions in the matrix.
    Returns a list of coordinates of positive cells.
    """
    positivePositions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:  # Add position to the list if value is positive
                positivePositions.append([row, col])
    return positivePositions

def getAdjacentPositions(row, col, matrix):
    """
    Returns a list of valid adjacent cell positions for the given cell.
    """
    adjacentPositions = []
    if row > 0:
        adjacentPositions.append([row - 1, col])  # Top neighbor
    if row < len(matrix) - 1:
        adjacentPositions.append([row + 1, col])  # Bottom neighbor
    if col > 0:
        adjacentPositions.append([row, col - 1])  # Left neighbor
    if col < len(matrix[0]) - 1:
        adjacentPositions.append([row, col + 1])  # Right neighbor
    return adjacentPositions

def containsNegative(matrix):
    """
    Checks if the matrix still contains any negative values.
    Returns True if any negative value exists, otherwise False.
    """
    for row in matrix:
        for value in row:
            if value < 0:  # Found a negative value
                return True
    return False

# Dummy Data for Testing
matrix = [
    [0, -1, -3, 2, 0],  # Example matrix with positives, negatives, and zeros
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

# Test the function with the dummy matrix
result = minimumPassesOfMatrix(matrix)
print(f"Minimum passes required: {result}")  # Expected Output: 4
