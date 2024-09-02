# 1. Initialize Transposed Matrix:
# An empty list `transposeMatrix` is initialized to store the transposed version of the input matrix.

# 2. Iterate Over Columns:
# The outer loop iterates over each column index (`col`) of the original matrix.

# 3. Initialize New Row:
# For each column, a new row (`newRow`) is initialized to collect elements that will form the corresponding row in the transposed matrix.

# 4. Iterate Over Rows:
# The inner loop iterates over each row index (`row`) of the original matrix.

# 5. Element Collection:
# Inside the inner loop, the element at the current `[row][col]` position is taken from the original matrix and appended to `newRow`.

# 6. Form and Append New Row:
# After collecting all elements for the current column, `newRow` (which is now a complete row for the transposed matrix) is appended to `transposeMatrix`.

# 7. Return Transposed Matrix:
# Once all columns are processed, the fully constructed `transposeMatrix` is returned.

# 8. Print the Original and Transposed Matrix:
# The original matrix is printed.
# The `transposeMatrix` function is executed, and the resulting transposed matrix is printed.


def transposeMatrix(matrix):
    # Initialize an empty list to store the transposed matrix
    transposeMatrix = []
    
    # Iterate over each column index in the matrix
    for col in range(len(matrix[0])): 
        # Initialize a new row for the transposed matrix
        newRow = []
        print(f"\nProcessing column {col + 1}:")

        # Iterate over each row index in the matrix
        for row in range(len(matrix)): 
            # Append the element at the current row and column to the new row
            print(f"  Taking element from row {row + 1}, column {col + 1}: {matrix[row][col]}")
            newRow.append(matrix[row][col])
        
        # Append the newly formed row to the transposed matrix
        print(f"  Formed new row: {newRow}")
        transposeMatrix.append(newRow)
    
    # Return the transposed matrix
    return transposeMatrix

# Define a sample matrix to transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Execute the transposeMatrix function and store the result
transposed = transposeMatrix(matrix)

# Print the transposed matrix
print("\nTransposed Matrix:")
for row in transposed:
    print(row)
