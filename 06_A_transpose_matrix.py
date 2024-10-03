# Problem Statement:
# Given a matrix (a list of lists), the goal is to transpose the matrix.
# Transposing a matrix means converting its rows into columns and vice versa.

# Steps to Solve the Problem:
# 1. Initialize an empty list to store the transposed matrix.
# 2. Iterate over each column index in the original matrix:
#    - The outer loop will run for the number of columns in the original matrix.
# 3. For each column, initialize a new row for the transposed matrix.
# 4. Iterate over each row index in the original matrix:
#    - The inner loop will run for the number of rows in the original matrix.
# 5. Append the element from the current row and the current column
#    of the original matrix to the new row being formed for the transposed matrix.
# 6. After completing the inner loop, append the new row to the transposed matrix.
# 7. Return the transposed matrix after completing the outer loop.


def transposeMatrix(matrix):
    # Initialize an empty list to store the transposed matrix
    transposeMatrix = []

    # Iterate over each column index in the matrix
    for col in range(len(matrix[0])):
        # Initialize a new row for the transposed matrix
        newRow = []

        # Iterate over each row index in the matrix
        for row in range(len(matrix)):
            # Append the element at the current row and column to the new row
            newRow.append(matrix[row][col])

        # Append the newly formed row to the transposed matrix
        transposeMatrix.append(newRow)

    # Return the transposed matrix
    return transposeMatrix


# Define a sample matrix to transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Execute the transposeMatrix function and store the result
transposed = transposeMatrix(matrix)

# Print the transposed matrix
for row in transposed:
    print(row)


# def transposeMatrix(matrix):
#     # Initialize an empty list to store the transposed matrix
#     transposeMatrix = []

#     # Iterate over each column index in the matrix
#     for col in range(len(matrix[0])):
#         # Initialize a new row for the transposed matrix
#         newRow = []
#         print(f"\nProcessing column {col + 1}:")

#         # Iterate over each row index in the matrix
#         for row in range(len(matrix)):
#             # Append the element at the current row and column to the new row
#             print(f"  Taking element from row {row + 1}, column {col + 1}: {matrix[row][col]}")
#             newRow.append(matrix[row][col])

#         # Append the newly formed row to the transposed matrix
#         print(f"  Formed new row: {newRow}")
#         transposeMatrix.append(newRow)

#     # Return the transposed matrix
#     return transposeMatrix

# # Define a sample matrix to transpose
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Print the original matrix
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Execute the transposeMatrix function and store the result
# transposed = transposeMatrix(matrix)

# # Print the transposed matrix
# print("\nTransposed Matrix:")
# for row in transposed:
#     print(row)
