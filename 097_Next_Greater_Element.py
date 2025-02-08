# ------------------------------------------------------------
# PROBLEM STATEMENT:
# ------------------------------------------------------------
# Given a circular array of integers, for each element in the array, 
# find the "next greater element" (NGE).
# The "next greater element" of a number is the first number that 
# appears to the right of it (considering circular rotation of the array) 
# which is strictly greater than it. 
# If no such element exists, assign -1 for that position.
#
# ------------------------------------------------------------
# EXPLANATION OF THE PROBLEM:
# ------------------------------------------------------------
# Let's break it down:
# - We have an array, for example: [2, 5, -3, -4, 6, 7, 2].
# - For each element, we want to look forward (to its right) and 
#   find the next number that is larger than it.
# - If we reach the end of the array and still haven't found 
#   a greater number, we "wrap around" because it's circular.
# - If we still don’t find anything, we assign -1.
#
# Example:
# Array = [2, 5, -3, -4, 6, 7, 2]
# Next Greater Elements = [5, 6, 6, 6, 7, -1, 5]
# Why?
# - For 2 → Next greater is 5
# - For 5 → Next greater is 6
# - For -3 → Next greater is 6
# - For -4 → Next greater is 6
# - For 6 → Next greater is 7
# - For 7 → No greater element, so -1
# - For 2 → Next greater is 5 (wrap around)
#
# ------------------------------------------------------------
# CODE EXECUTION THEORY:
# ------------------------------------------------------------
# We'll use a **monotonic decreasing stack** to efficiently solve this.
# Here's the thought process:
# - We need results for each index → initialize result[] with -1.
# - We will loop through the array *twice* (to simulate circular behavior).
# - At each step, we check if the current element is greater 
#   than the element at the index stored on top of the stack.
#   - If yes → we found the next greater element for that index.
# - Push the current index to the stack for later comparison.
# - At the end → result[] contains all answers.
#
# Time Complexity = O(n), because each element is pushed and popped once.
#
# ------------------------------------------------------------
# CODE IMPLEMENTATION WITH COMMENTS:
# ------------------------------------------------------------

def nextGreaterElement(array):
    # Step 1: Initialize result array with -1 (default: assume no greater element)
    result = [-1] * len(array)
    
    # Step 2: Use a stack to store indices of elements
    stack = []
    
    # Step 3: Loop through the array twice (to handle circular behavior)
    for idx in range(2 * len(array)):
        # Step 3a: Calculate the circular index (wrap around using modulo)
        circularIdx = idx % len(array)
        
        # Step 3b: While stack is not empty AND current element is greater 
        # than the element at the index stored at top of the stack
        while stack and array[stack[-1]] < array[circularIdx]:
            # Step 3c: Pop index from stack, assign next greater element
            top = stack.pop()
            result[top] = array[circularIdx]
        
        # Step 3d: Push index into stack (only in the first pass)
        if idx < len(array):  
            stack.append(circularIdx)
    
    return result


# ------------------------------------------------------------
# TEST WITH DUMMY DATA
# ------------------------------------------------------------
data = [2, 5, -3, -4, 6, 7, 2]
print("Input Array: ", data)
print("Next Greater Elements: ", nextGreaterElement(data))

# Output:
# Input Array:  [2, 5, -3, -4, 6, 7, 2]
# Next Greater Elements:  [5, 6, 6, 6, 7, -1, 5]


# ------------------------------------------------------------
# INDUSTRY EQUIVALENT REAL-TIME APPLICATION SCENARIO:
# ------------------------------------------------------------
# This "Next Greater Element" concept is widely useful in:
#
# 1. Stock Market Analysis:
#    - Array elements = daily stock prices.
#    - Next greater element = the next day when stock price goes higher.
#    - Helps in predicting "next rise" days.
#
# 2. Weather Forecasting:
#    - Array elements = daily temperatures.
#    - Next greater element = the next warmer day.
#    - This is a classic LeetCode problem: "Daily Temperatures".
#
# 3. Manufacturing/Processing:
#    - Array elements = machine load or usage levels.
#    - Next greater element = the next time the machine runs at a higher load.
#
# 4. Circular Buffers in Networking:
#    - Circular arrays are common in ring buffers for streaming data.
#    - We can use this to find the next packet size greater than the current one.
