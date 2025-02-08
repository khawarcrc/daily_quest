# Problem Statement:
# Given an array of positive integers, where each integer represents the amount of money at each position,
# write a function that returns the maximum sum of non-adjacent elements.
# The goal is to maximize the sum without selecting two consecutive elements.

# Code Execution Theory:
# 1. We create a new array 'maxSums' that will store the maximum sum we can obtain up to each element
#    without choosing adjacent elements.
# 2. For the second element in the array, we initialize maxSums[1] as the maximum of the first two elements
#    to handle the first comparison in non-adjacency.
# 3. For each element starting from the third position, we calculate the maximum possible sum at that
#    position by choosing between:
#    - The previous max sum (maxSums[i - 1], not including the current element),
#    - The sum of the current element and the best sum up to two positions before (maxSums[i - 2] + array[i]).
# 4. The last element of the maxSums array will contain the maximum sum achievable by selecting non-adjacent elements.
# 5. This approach ensures we avoid adjacent element selection and obtain the optimal sum.



def maxSubSetSumNoAdjacent(array):
    # Edge case: if the array is empty, the max sum is 0
    if not len(array):
        return 0
    # If the array has only one element, that element is the max sum
    elif len(array) == 1:
        return array[0]

    # Initialize maxSums array with the same values as the original array
    maxSums = array[:]
    # Set the second element as the max of the first two elements
    # This line sets maxSums[1] to the greater value between array[0] and array[1].
    # This way, maxSums[1] will hold the highest possible sum we can obtain by considering only the first two elements,
    # without picking two consecutive values.
    maxSums[1] = max(array[0], array[1])

    # Iterate over the array starting from the third element
    for i in range(2, len(array)):
        # Update the maxSums array by taking the maximum of:
        # 1. The previous maximum sum (not including current element)
        # 2. The sum of current element and max sum excluding previous element
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

    # The last element of maxSums contains the maximum sum we can obtain
    return maxSums[-1]

# Dummy data
array = [3, 2, 5, 10, 7]
print("Maximum sum with no adjacent elements:", maxSubSetSumNoAdjacent(array))



# Example execution for input array = [3, 2, 5, 10, 7]

# Step 1: Initialize maxSums array with a copy of the input array
# Initial maxSums = [3, 2, 5, 10, 7]

# Step 2: Set maxSums[1] to the maximum of the first two elements
# maxSums[1] = max(3, 2) = 3
# Updated maxSums = [3, 3, 5, 10, 7]

# Step 3: Iterate over the array starting from the third element

# When i = 2:
# maxSums[2] = max(maxSums[1], maxSums[0] + array[2])
#            = max(3, 3 + 5) = max(3, 8) = 8
# Updated maxSums = [3, 3, 8, 10, 7]

# When i = 3:
# maxSums[3] = max(maxSums[2], maxSums[1] + array[3])
#            = max(8, 3 + 10) = max(8, 13) = 13
# Updated maxSums = [3, 3, 8, 13, 7]

# When i = 4:
# maxSums[4] = max(maxSums[3], maxSums[2] + array[4])
#            = max(13, 8 + 7) = max(13, 15) = 15
# Final maxSums = [3, 3, 8, 13, 15]

# Result:
# The last element in maxSums, maxSums[-1] = 15, is the maximum sum we can obtain
# by choosing non-adjacent elements in the array.
