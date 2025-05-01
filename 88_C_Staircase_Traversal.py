# --------------------- Problem Statement ---------------------
# Given a staircase of 'height' steps and a maxSteps value, compute the number of
# distinct ways to reach the top by climbing 1 to maxSteps steps at a time.

# --------------------- Explanation ---------------------
# For every step, the number of ways to reach it is the sum of the number of ways
# to reach the previous 'maxSteps' steps. This version uses a **sliding window** approach.
# we maintain a running sum using a window (O(1) update) — improving performance.

# --------------------- Code Execution Theory ---------------------
# We initialize an array `waysToTop` where each index i represents the number of ways to reach step i.
# - waysToTop[0] = 1 (1 way to stay at ground)
# For each height from 1 to 'height':
#   - Calculate a sliding window from (currentHeight - maxSteps) to (currentHeight - 1)
#   - Use cumulative sum technique: currentWays = prefixSum[end] - prefixSum[start - 1]
#   - Append the number of ways to reach the current step into the waysToTop array.
# Time Complexity: O(n)
# Space Complexity: O(n)

# --------------------- Corrected Code Starts Here ---------------------

def staircaseTraversal(height, maxSteps): 
    # Number of ways to reach step 0 (ground level) is 1
    waysToTop = [1]  
    
    # Running sum of the last 'maxSteps' entries
    currentNumberOfWays = 0  
    
    # Start calculating from step 1 to height
    for currentHeight in range(1, height + 1): 
        # Define window for sliding sum
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1
        
        # Subtract out-of-window value if valid
        if startOfWindow >= 0: 
            currentNumberOfWays -= waysToTop[startOfWindow]
        
        # Add current end of window to the running total
        if endOfWindow >= 0:
            currentNumberOfWays += waysToTop[endOfWindow]
        
        # Append total ways to reach currentHeight
        waysToTop.append(currentNumberOfWays)
    
    # Final answer: ways to reach top (height)
    return waysToTop[height]

# --------------------- Dummy Test Case ---------------------

# Example: height = 4, maxSteps = 2
# Ways: [1,1,1,1], [1,2,1], [2,2], [2,1,1], [1,1,2]
# Output: 5

height = 4
maxSteps = 2

print("Number of ways to climb the staircase:", staircaseTraversal(height, maxSteps))
