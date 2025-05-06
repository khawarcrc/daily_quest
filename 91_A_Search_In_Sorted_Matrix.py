# ------------------ Problem Statement ------------------
# Given a 2D matrix where each row and each column is sorted in ascending order,
# write a function to search for a target value in the matrix.
# If the target is found, return its position as [row, column],
# otherwise return [-1, -1].

# ------------------ Explanation of the Problem ------------------
# - The matrix is sorted such that:
#     * Each row is sorted from left to right.
#     * Each column is sorted from top to bottom.
# - For example:
#     [
#       [1,  4,  7, 11],
#       [2,  5,  8, 12],
#       [3,  6,  9, 16],
#       [10,13,14,17]
#     ]
# - A naive approach would be to scan each element (O(m*n)),
#   but we can do better by using the sorted properties.

# ------------------ Code Execution Theory ------------------
# - We start from the **top-right** element of the matrix.
# - If the current element is **greater** than the target, move **left** (col -= 1)
# - If the current element is **less** than the target, move **down** (row += 1)
# - If the current element **equals** the target, return [row, col]
# - If we move out of bounds, return [-1, -1] (target not found)
# - Time complexity: O(m + n) where m = number of rows, n = number of columns


# ------------------ Function Definition ------------------
def searchInSortedmatrix(matrix, target):
    # Start from the top-right corner of the matrix
    row = 0
    col = len(matrix[0]) - 1  # Index of the last column

    # Traverse the matrix while staying within bounds
    while row < len(matrix) and col >= 0:
        # If current value is greater than target, move left
        if matrix[row][col] > target:
            col -= 1
        # If current value is less than target, move down
        elif matrix[row][col] < target:
            row += 1
        # If current value equals the target, return the position
        else:
            return [row, col]

    # Target was not found in the matrix
    return [-1, -1]


# ------------------ Dummy Data ------------------
matrix = [
    [1,  4,  7, 11],
    [2,  5,  8, 12],
    [3,  6,  9, 16],
    [10,13,14,17]
]
target = 6


# ------------------ Function Call ------------------
print(searchInSortedmatrix(matrix, target))  # Output: [2, 1]
