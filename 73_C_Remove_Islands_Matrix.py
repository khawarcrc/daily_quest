
# Outer loop explanation:
# The first loop in the `removeIslands` function scans through each cell on the border of the matrix.
# For any border cell containing a 1, it initiates a marking process to protect the connected 1's.
# This marking is done by changing 1's that are part of the border-connected regions to 2's.
# These marked 2's represent "safe" land cells that should not be removed, helping us to
# later distinguish between island cells (which need to be removed) and border-connected cells.

# Inner loop explanation:
# After marking the "safe" border-connected 1's, the second loop traverses all cells in the matrix.
# During this traversal, it checks each cell to identify and remove isolated 1's, also known as "islands."
# For each isolated 1 (a 1 not marked as connected to the border), it sets it to 0, effectively "removing" the island.
# The loop also reverts any 2's back to 1's, restoring the appearance of the matrix by keeping only the safe regions intact.

# Stack-based DFS explanation:
# The `changeOnesConnectedToBorderToTwos` function performs a depth-first search (DFS) to mark all 1's connected to a given border cell.
# Using a stack, this function iterates over each connected 1 and marks it as 2, ensuring that all neighboring land cells are explored.
# This approach ensures that all border-connected land cells are marked in a single traversal without revisiting any cell.

# Neighbor retrieval explanation:
# The `getNeighbors` function gathers all valid neighboring cells (up, down, left, and right) of a given cell.
# This is critical for the DFS traversal, as it ensures that only in-bound cells are processed.
# By providing a list of valid neighbors, it allows the DFS process to explore each connected cell efficiently.


def removeIslands(matrix):
    # Traverse the entire matrix, focusing on border cells to mark connected 1's
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Check if the current cell is on the border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder  # True if it's a border cell
            
            if not isBorder:  # Skip cells that are not on the border
                continue
            
            if matrix[row][col] != 1:  # Skip border cells that do not contain a 1
                continue
            
            # Convert connected border 1's to 2's to indicate they are safe
            changeOnesConnectedToBorderToTwos(matrix, row, col)
    
    # Traverse the entire matrix again to change isolated 1's to 0's and revert 2's to 1's
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            if color == 1:
                matrix[row][col] = 0  # Convert isolated 1's (islands) to 0's
            elif color == 2:
                matrix[row][col] = 1  # Revert 2's back to 1's to mark as safe land
    return matrix


def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    # Initialize a stack for depth-first search from the starting border cell
    stack = [(startRow, startCol)]

    while len(stack) > 0:
        currentPosition = stack.pop()  # Pop the last position added to the stack
        currentRow, currentCol = currentPosition

        # Mark the current cell as safe by changing it from 1 to 2
        matrix[currentRow][currentCol] = 2

        # Get all valid neighboring cells of the current cell
        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:  # Skip cells that are not 1's
                continue
            
            # Add connected 1's to the stack for further exploration
            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    # List to store valid neighboring cells
    neighbors = []

    numRows = len(matrix)  # Total rows in the matrix
    numCols = len(matrix[row])  # Total columns in the matrix

    # Add the cell above if within bounds
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    # Add the cell below if within bounds
    if row + 1 < numRows:
        neighbors.append((row + 1, col))
    # Add the cell to the left if within bounds
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    # Add the cell to the right if within bounds
    if col + 1 < numCols:
        neighbors.append((row, col + 1))

    return neighbors  # Return the list of valid neighboring cells


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




# Border-Connected Cells Marking:
# In the first implementation, the function `findOnesConnectedToBorder` 
# marks cells connected to the border by using an auxiliary matrix, 
# `onesConnectedToBorder`, to track which cells are connected to the border.
# In the second implementation, the `changeOnesConnectedToBorderToTwos` 
# function directly modifies the matrix itself, marking border-connected cells 
# with the number 2, eliminating the need for an additional matrix.

# Depth-First Search (DFS) Traversal:
# Both implementations use DFS to traverse connected cells, but they use 
# different helper functions:
# - The first implementation uses `findOnesConnectedToBorder` for recursive DFS traversal.
# - The second implementation uses a stack-based iterative approach within 
#   the `changeOnesConnectedToBorderToTwos` function.

# Final Conversion of Isolated 1's:
# - The first implementation’s inner loop checks the `onesConnectedToBorder` 
#   matrix to determine which 1's to remove (set to 0).
# - The second implementation iterates over the matrix itself, converting 
#   unconnected 1's to 0 and reverting the marked 2's back to 1.

# Efficiency:
# - The second implementation is more space-efficient as it avoids using an 
#   auxiliary matrix and instead performs the marking directly within the 
#   original matrix. This reduces memory usage, potentially improving speed for 
#   large matrices.
# - Both implementations have the same time complexity since they both 
#   iterate over the matrix and process cells using DFS.
