import pandas as pd

def numberOfWaysToTraverseGraph(width, height):
    # Initialize a 2D array to store the number of ways to reach each cell
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    # Log initial state
    print("Initial matrix:")
    print(pd.DataFrame(numberOfWays))

    # Iterate through each cell in the grid
    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            # Base case: if we're in the first row or first column, only 1 way to reach each cell
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                # Calculate ways from left and above cells
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

            # Log the matrix state after updating each cell
            print(f"\nMatrix after updating cell ({heightIdx},{widthIdx}):")
            print(pd.DataFrame(numberOfWays))

    # Return the number of ways to reach the bottom-right corner of the grid
    return numberOfWays[height][width]

# Dummy data for testing: width and height of a 3x3 grid
width = 3
height = 3
print("\nTotal ways to traverse the grid:", numberOfWaysToTraverseGraph(width, height))
