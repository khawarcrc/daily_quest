# --------------------- Problem Statement ---------------------
# Given a staircase with a certain number of steps (height), and a person who can climb
# up to 'maxSteps' steps at a time, compute the number of distinct ways the person can 
# reach the top of the staircase.

# --------------------- Explanation ---------------------
# Each step from 1 to maxSteps is a possible jump length the person can make.
# We need to calculate all possible combinations of such jumps that sum up to exactly the height.

# --------------------- Code Execution Theory ---------------------
# This is a dynamic programming problem, solved using memoization (top-down DP).
# The idea is to recursively reduce the problem: for each step from 1 to maxSteps,
# subtract that step from the current height and calculate the number of ways to reach
# the top from that new height.
# Memoization is used to store results for subproblems we've already solved to avoid recomputation.
# Base cases: 
# - height 0 means 1 way (already at the top)
# - height 1 means 1 way (only one step of 1)
# The recursion builds upward by combining results of smaller subproblems.
# Time Complexity: O(k * n), where n = height, k = maxSteps
# Space Complexity: O(n), for memoization dictionary

# --------------------- Code with Comments and Dummy Data ---------------------

def staircaseTraversal(height, maxSteps):
    """
    Calculates the number of ways to reach the top of the staircase.
    Starts from given height and uses a helper with memoization.
    """
    return numberOfWaysToTop(height, maxSteps, {0: 1, 1: 1})  # Base cases: height 0 or 1 have 1 way


def numberOfWaysToTop(height, maxSteps, memoize):
    """
    Recursive helper function that uses memoization to store previously computed results.
    """
    if height in memoize:  # If already calculated, return from memo
        return memoize[height]

    numberOfWays = 0  # Initialize number of ways for this height

    # Try every step size from 1 to maxSteps (or up to height)
    for step in range(1, min(maxSteps, height) + 1):
        # Recursively calculate ways for remaining height and add to total
        numberOfWays += numberOfWaysToTop(height - step, maxSteps, memoize)

    memoize[height] = numberOfWays  # Store result in memoization dictionary
    return numberOfWays  # Return total number of ways for this height


# --------------------- Dummy Test Case ---------------------

# Example: A staircase of height 4, with maxSteps of 2
# Possible combinations:
# 1-1-1-1
# 1-1-2
# 1-2-1
# 2-1-1
# 2-2
# So, expected output = 5

height = 4
maxSteps = 2

# Output: 5
print("Number of ways to climb the staircase:", staircaseTraversal(height, maxSteps))
