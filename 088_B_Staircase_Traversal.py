# --------------------- Problem Statement ---------------------
# Given a staircase of a certain height, and the maximum number of steps you can take at once (maxSteps),
# find the total number of distinct ways you can reach the top from the ground level (step 0).
# You can climb 1 to maxSteps steps at a time.

# --------------------- Explanation ---------------------
# The person can take variable steps (from 1 to maxSteps) at a time.
# We are to compute how many distinct sequences of such steps can sum up to exactly 'height'.

# --------------------- Code Execution Theory ---------------------
# This uses a bottom-up dynamic programming approach.
# We maintain an array waysToTop[] where waysToTop[i] means number of ways to reach step 'i'.
# waysToTop[0] = 1 → only one way to stand at the base.
# Then for each step i from 2 to height:
#   We initialize step = 1
#   While step <= maxSteps and step <= currentHeight:
#       We add the ways from (i - step) to current height’s ways.
# This accumulates all possible step sequences that lead to step i.
# Time Complexity: O(n * k), where n = height, k = maxSteps
# Space Complexity: O(n)

# --------------------- Corrected Code Using `while` ---------------------

def staircaseTraversal(height, maxSteps):
    # Initialize DP array to store number of ways to reach each height
    waysToTop = [0 for _ in range(height + 1)]
    
    # Base cases
    waysToTop[0] = 1  # One way to stay at the bottom
    if height >= 1:
        waysToTop[1] = 1  # One way to reach step 1
    
    # Iterate from step 2 up to the final height
    for currentHeight in range(2, height + 1):
        step = 1
        # Accumulate number of ways using steps from 1 to maxSteps
        while step <= maxSteps and step <= currentHeight:
            # Add ways from previous steps to reach currentHeight
            waysToTop[currentHeight] += waysToTop[currentHeight - step]
            step += 1
    
    return waysToTop[height]  # Total ways to reach the top step

# --------------------- Dummy Test Case ---------------------

# Example: Staircase height = 4, maxSteps = 2
# Valid paths: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]
# Expected output: 5

height = 4
maxSteps = 2

print("Number of ways to climb the staircase:", staircaseTraversal(height, maxSteps))
