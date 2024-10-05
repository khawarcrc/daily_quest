# Problem Statement:
# Given a 2D array (matrix), write a function that returns a list of its elements in spiral order.
# Spiral order means starting at the top-left corner of the matrix and traversing it in a clockwise
# direction, layer by layer, until all elements are visited.

# Steps to Solve the Problem:

# 1. Initialize an empty list to store the result of the spiral traversal.
# 2. Define four variables to represent the boundaries of the current layer:
#    - `startRow`: The index of the top row of the current layer.
#    - `endRow`: The index of the bottom row of the current layer.
#    - `startCol`: The index of the leftmost column of the current layer.
#    - `endCol`: The index of the rightmost column of the current layer.
# 3. While the boundaries haven't crossed (i.e., `startRow <= endRow` and `startCol <= endCol`):
#    a. Traverse the top row from left to right (between `startCol` and `endCol`),
#       and append the elements to the result list.
#    b. Traverse the rightmost column from top to bottom (between `startRow+1` and `endRow`),
#       and append the elements to the result list.
#    c. If there are remaining rows (i.e., `startRow < endRow`), traverse the bottom row from right to left
#       (between `endCol-1` and `startCol`), and append the elements to the result list.
#    d. If there are remaining columns (i.e., `startCol < endCol`), traverse the leftmost column from bottom to top
#       (between `endRow-1` and `startRow+1`), and append the elements to the result list.
# 4. After traversing a full layer, move the boundaries inward:
#    a. Increment `startRow` by 1 to exclude the top row.
#    b. Decrement `endRow` by 1 to exclude the bottom row.
#    c. Increment `startCol` by 1 to exclude the leftmost column.
#    d. Decrement `endCol` by 1 to exclude the rightmost column.
# 5. Repeat the process until all elements in the matrix have been traversed.
# 6. Return the list containing the elements in spiral order.


def spiralTraverse(array):
    # Initialize an empty list to store the result
    result = []

    # Define the starting and ending boundaries for rows and columns
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1

    # Continue looping as long as the boundaries have not crossed
    while startRow <= endRow and startCol <= endCol:
        # Traverse the top row from left to right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # Traverse the right column from top to bottom
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # Traverse the bottom row from right to left (if there are remaining rows)
        if startRow < endRow:
            for col in reversed(range(startCol, endCol)):
                result.append(array[endRow][col])

        # Traverse the left column from bottom to top (if there are remaining columns)
        if startCol < endCol:
            for row in reversed(range(startRow + 1, endRow)):
                result.append(array[row][startCol])

        # Move the boundaries inward for the next layer
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


# Dummy data (4x4 matrix)
array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Call the function with the dummy data
print(
    spiralTraverse(array)
)  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


# Current boundaries: startRow = 0, endRow = 3, startCol = 0, endCol = 3
# Traversing top row from col 0 to 3 at row 0
# Appending 1 from array[0][0]
# Appending 2 from array[0][1]
# Appending 3 from array[0][2]
# Appending 4 from array[0][3]
# Traversing right column from row 1 to 3 at col 3
# Appending 8 from array[1][3]
# Appending 12 from array[2][3]
# Appending 16 from array[3][3]
# Traversing bottom row from col 2 to 0 at row 3
# Appending 15 from array[3][2]
# Appending 14 from array[3][1]
# Appending 13 from array[3][0]
# Traversing left column from row 2 to 1 at col 0
# Appending 9 from array[2][0]
# Appending 5 from array[1][0]
# Moving boundaries inward
# Updated boundaries: startRow = 1, endRow = 2, startCol = 1, endCol = 2
# Current result: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5]
# --------------------------------------------------
# Current boundaries: startRow = 1, endRow = 2, startCol = 1, endCol = 2
# Traversing top row from col 1 to 2 at row 1
# Appending 6 from array[1][1]
# Appending 7 from array[1][2]
# Traversing right column from row 2 to 2 at col 2
# Appending 11 from array[2][2]
# Traversing bottom row from col 1 to 1 at row 2
# Appending 10 from array[2][1]
# Traversing left column from row 1 to 2 at col 1
# Moving boundaries inward
# Updated boundaries: startRow = 2, endRow = 1, startCol = 2, endCol = 1
# Current result: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
# --------------------------------------------------
# Final spiral traversal result: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
