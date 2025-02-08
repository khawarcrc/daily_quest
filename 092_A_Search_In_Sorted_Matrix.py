# ---------------------------------- Problem Statement ----------------------------------
# You are given a 2D matrix (n x m) where each row is sorted in ascending order from left to right,
# and each column is sorted in ascending order from top to bottom.
# Your task is to write a function that efficiently searches for a given target value in this matrix.
# If the target is found, return its coordinates [row, col]. Otherwise, return [-1, -1].

# ---------------------------------- Concept Explanation ----------------------------------
# Since both rows and columns are sorted, we can leverage the sorting to eliminate portions of the matrix.
# We start from the top-right corner of the matrix:
# - If the current number is greater than the target, we move left (column--).
# - If the current number is less than the target, we move down (row++).
# - If the current number equals the target, return the current coordinates.
# This ensures O(n + m) time complexity, where n is the number of rows and m is the number of columns.

# ---------------------------------- Function Definition ----------------------------------

def searchInSortedMatrix(matrix, target):
    # Start at the top-right corner of the matrix
    row = 0  # Initialize the row index to the first row
    col = len(matrix[0]) - 1  # Initialize the col index to the last column

    # Traverse the matrix while within the valid bounds
    while row < len(matrix) and col >= 0:
        # If the current element is greater than the target, move left
        if matrix[row][col] > target:
            col -= 1  # Move one column to the left
        # If the current element is less than the target, move down
        elif matrix[row][col] < target:
            row += 1  # Move one row down
        # If the current element is equal to the target, return its position
        else:
            return [row, col]  # Target found at this row and column

    # If the loop ends, the target is not in the matrix
    return [-1, -1]  # Target not found

# ---------------------------------- Dummy Data ----------------------------------

matrix = [
    [1,  4,  7, 11],     # Row 0
    [2,  5,  8, 12],     # Row 1
    [3,  6,  9, 16],     # Row 2
    [10,13,14,17]        # Row 3
]

target = 6  # The number we want to find in the matrix

# ---------------------------------- Function Call ----------------------------------

result = searchInSortedMatrix(matrix, target)  # Call the function and store the result

# ---------------------------------- Output ----------------------------------

# Print the coordinates of the target if found
print(f"Target {target} found at position: {result}")  # Expected output: [2, 1]
