def removeIslands(matrix):
    # Create a matrix of the same size as `matrix` to track which 1's are connected to the border
    onesConnectedToBorder = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    print("Initial onesConnectedToBorder matrix:")
    for row in onesConnectedToBorder:
        print(row)

    # Traverse each cell along the border to find all 1's connected to the border
    for row in range(len(matrix)):  # Loop through each row
        for col in range(len(matrix[row])):  # Loop through each column in the row
            # Determine if the current cell is on the border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder  # Cell is a border cell if it's in the first or last row/column
            if not isBorder:  # Skip non-border cells
                continue

            # If this border cell contains a 1, initiate a search to mark connected 1's
            if matrix[row][col] == 1:
                print(f"\nStarting search for border-connected 1's from cell ({row}, {col})")
                findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    # Traverse all non-border cells and remove (convert to 0) any 1's not connected to the border
    print("\nMarking non-border-connected 1's as 0 in the matrix:")
    for row in range(1, len(matrix) - 1):  # Loop through rows, excluding the first and last rows
        for col in range(1, len(matrix[row]) - 1):  # Loop through columns, excluding first and last columns
            # If the cell is not marked as connected to the border, it's an "island" 1, so set it to 0
            if not onesConnectedToBorder[row][col]:
                print(f"Setting cell ({row}, {col}) from 1 to 0")
                matrix[row][col] = 0

    print("\nFinal matrix after removing islands:")
    for row in matrix:
        print(row)
    return matrix  # Return the modified matrix


def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    # Initialize a stack for depth-first search (DFS) to mark all 1's connected to the border
    stack = [(startRow, startCol)]
    print(f"  Initialized DFS stack with starting cell ({startRow}, {startCol})")

    # Loop until all reachable connected 1's have been processed
    while stack:
        currentRow, currentCol = stack.pop()  # Pop the last added position from the stack
        print(f"  Visiting cell ({currentRow}, {currentCol})")

        # Check if the cell has already been marked as visited
        if onesConnectedToBorder[currentRow][currentCol]:
            print(f"  Cell ({currentRow}, {currentCol}) already visited. Skipping.")
            continue  # Skip this cell if it has already been visited

        # Mark the cell as connected to the border
        onesConnectedToBorder[currentRow][currentCol] = True
        print(f"  Marked cell ({currentRow}, {currentCol}) as connected to border")

        # Retrieve all valid neighbors of the current cell
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighborRow, neighborCol in neighbors:  # Loop through each neighboring cell
            # If the neighboring cell contains a 1, add it to the stack for further exploration
            if matrix[neighborRow][neighborCol] == 1:
                print(f"  Adding neighboring cell ({neighborRow}, {neighborCol}) to stack")
                stack.append((neighborRow, neighborCol))


def getNeighbors(matrix, row, col):
    # Initialize an empty list to store valid neighboring positions
    neighbors = []
    numRows = len(matrix)  # Total number of rows in the matrix
    numCols = len(matrix[0])  # Total number of columns in the matrix

    # Check if the upward neighbor is within bounds and add it to neighbors
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
        print(f"    Found neighbor at ({row - 1}, {col})")

    # Check if the downward neighbor is within bounds and add it to neighbors
    if row + 1 < numRows:
        neighbors.append((row + 1, col))
        print(f"    Found neighbor at ({row + 1}, {col})")

    # Check if the left neighbor is within bounds and add it to neighbors
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
        print(f"    Found neighbor at ({row}, {col - 1})")

    # Check if the right neighbor is within bounds and add it to neighbors
    if col + 1 < numCols:
        neighbors.append((row, col + 1))
        print(f"    Found neighbor at ({row}, {col + 1})")

    return neighbors  # Return the list of valid neighboring positions


# Dummy data: 1's represent land, 0's represent water
matrix = [
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1]
]

# Call the function with the dummy data
result = removeIslands(matrix)

# Print the resulting matrix
print("\nResulting matrix after removing islands:")
for row in result:
    print(row)
