# Problem Statement:
# The task is to calculate the number of unique ways to traverse a grid from the top-left to the bottom-right corner,
# where movement is restricted to either going right or down. The grid dimensions are defined by 'width' and 'height'.
# Each cell represents a step in the path, and the top-left corner is the starting point.
# 
# Code Execution Theory:
# 1. A 2D list `numberOfWays` is created to store the number of ways to reach each cell in the grid, with dimensions
#    (height + 1) x (width + 1) to accommodate all cells.
# 2. For cells in the first row or first column, there is only one way to reach them, so they are set to 1.
# 3. For other cells, the number of ways to reach each cell is calculated by adding the values of the cell directly
#    above it (`waysUp`) and the cell to its immediate left (`waysLeft`), simulating movement down and right.
# 4. The final result, representing the number of ways to reach the bottom-right corner, is located at `numberOfWays[height][width]`.


def numberOfWaysToTraverseGraph(width, height):
    # Initialize a 2D array with dimensions (height + 1) x (width + 1) to store the number of ways to reach each cell
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    # Iterate through each cell in the grid
    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            # Set the base cases: if we're in the first row or the first column, there's only 1 way to reach each cell
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                # Calculate the number of ways by summing the ways from the left and the top cells
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

    # Return the number of ways to reach the bottom-right corner of the grid
    return numberOfWays[height][width]

# Dummy data for testing: width and height of a 3x3 grid
width = 3
height = 3
print(numberOfWaysToTraverseGraph(width, height))  # Expected output: 6



# Problem Execution Example:
# Let's consider a small grid with dimensions 2x2 to understand how the function calculates the number of ways to traverse it.
# Starting from the top-left corner (1,1), we can only move right or down to reach the bottom-right corner (2,2).

# The 2x2 grid layout looks like this:
# (1,1) --> (1,2)
#   |          |
#  (2,1) --> (2,2)

# Execution Steps:
# 1. Initialize a 3x3 array `numberOfWays` to accommodate all cells, including row 0 and column 0, which act as base indices.
#    Initially, the array looks like:
#    numberOfWays = [[0, 0, 0],
#                    [0, 0, 0],
#                    [0, 0, 0]]

# 2. For the first row and first column, there is only 1 way to reach each cell since the movement is either horizontal (right)
#    or vertical (down). After setting these base cases, the array updates to:
#    numberOfWays = [[0, 0, 0],
#                    [0, 1, 1],
#                    [0, 1, 0]]

# 3. Now, for the remaining cells (starting from cell (2,2)), calculate the number of ways to reach each cell by summing
#    the number of ways to reach the cell directly above it and the cell directly to its left:
#       - For cell (2,2): waysUp (1) + waysLeft (1) = 2
#    After this calculation, the array becomes:
#    numberOfWays = [[0, 0, 0],
#                    [0, 1, 1],
#                    [0, 1, 2]]

# 4. The final value at `numberOfWays[2][2]` (bottom-right corner) is 2, representing the number of unique ways to reach
#    this cell from the top-left corner.

# Conclusion:
# In a 2x2 grid, there are 2 unique paths from the top-left to the bottom-right:
#   - Right -> Down
#   - Down -> Right


