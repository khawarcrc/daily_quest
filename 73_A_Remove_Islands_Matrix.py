# Problem Statement:
# Given a binary matrix (2D list) where cells with a value of 1 represent land and cells with a value of 0 represent water,
# remove all "islands" of 1's that are not connected to the border of the matrix. A cell is considered part of an island 
# if it is surrounded by 0's (water) on all sides, and is not connected to any 1's that touch the matrix border. Any 1's 
# that connect directly or indirectly to the matrix's border should remain unchanged. The goal is to replace all internal 
# islands of 1's with 0's, leaving only the border-connected 1's intact.

# Explanation of the Problem:
# - The matrix consists of rows and columns where each cell has a value of either 1 (land) or 0 (water).
# - A "border-connected land" is any cell containing a 1 that is directly or indirectly connected to a border cell with a 1.
# - An "island" is a group of 1's completely surrounded by 0's and disconnected from the matrix border.
# - To solve the problem, we need to:
#   1. Identify all 1's that are directly or indirectly connected to any border cell containing a 1.
#   2. Mark these cells as connected to the border, meaning they shouldn't be removed.
#   3. Replace all remaining internal 1's (islands) with 0's.

# Code Execution Theory:
# 1. Initialize a boolean matrix `onesConnectedToBorder` with the same dimensions as the input matrix, 
#    where each cell is set to `False`. This matrix is used to mark which cells contain 1's connected to the border.
# 2. Traverse the matrix borders:
#    - For each cell on the border, if it contains a 1, call a helper function to mark all 1's connected to it.
#    - This is done using depth-first search (DFS) to explore all adjacent cells with a 1.
# 3. In the DFS function `findOnesConnectedToBorder`:
#    - Use a stack to explore each cell containing a 1 that is reachable from a border 1.
#    - Mark each visited cell in `onesConnectedToBorder` as `True`.
#    - For each cell visited, check its neighbors in four directions (up, down, left, right).
#    - Add each neighboring cell with a 1 to the stack, so that all connected 1's are visited and marked.
# 4. After all border-connected 1's are marked, traverse the inner matrix cells (excluding the borders):
#    - For each cell, if it contains a 1 but is not marked as connected to the border in `onesConnectedToBorder`,
#      change it to 0, effectively removing the island.
# 5. Return the modified matrix, where all internal islands of 1's are replaced with 0's, while border-connected 1's remain.


def removeIslands(matrix):
    # Create a matrix of the same size to mark 1's connected to the border
    onesConnectedToBorder = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Traverse the border cells to find all 1's connected to the border
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Check if the cell is on the border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue

            # If it's a border cell with a 1, start marking connected 1's
            if matrix[row][col] == 1:
                findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    # Convert internal 1's (not connected to the border) to 0's (removing islands)
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if not onesConnectedToBorder[row][col]:
                matrix[row][col] = 0

    return matrix


def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    # Stack for depth-first search to mark connected 1's
    stack = [(startRow, startCol)]

    while stack:
        currentRow, currentCol = stack.pop()

        # Skip if we've already visited this cell
        if onesConnectedToBorder[currentRow][currentCol]:
            continue

        # Mark this cell as connected to the border
        onesConnectedToBorder[currentRow][currentCol] = True

        # Get all valid neighboring cells
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighborRow, neighborCol in neighbors:
            if matrix[neighborRow][neighborCol] == 1:
                stack.append((neighborRow, neighborCol))


def getNeighbors(matrix, row, col):
    neighbors = []
    numRows = len(matrix)
    numCols = len(matrix[0])

    # Check each direction and add valid neighbors
    if row - 1 >= 0:  # Up
        neighbors.append((row - 1, col))
    if row + 1 < numRows:  # Down
        neighbors.append((row + 1, col))
    if col - 1 >= 0:  # Left
        neighbors.append((row, col - 1))
    if col + 1 < numCols:  # Right
        neighbors.append((row, col + 1))

    return neighbors


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

# Print the result
for row in result:
    print(row)
