# Sort the array in ascending order to enable a two-pointer approach.
# Initialize two pointers: 'left' at the start and 'right' at the end of the array.
# Iterate while 'left' pointer is less than 'right' pointer to find a pair that sums to the target.
# Calculate the sum of the values at the 'left' and 'right' pointers.
# If the current sum equals the target sum, return the pair of numbers.
# If the current sum is less than the target sum, move the 'left' pointer to the right to increase the sum.
# If the current sum is greater than the target sum, move the 'right' pointer to the left to decrease the sum.
# If no such pair is found after the loop ends, return an empty list.

def twoNumberSum(array, targetSum):
    # Step 1: Sort the input array in ascending order.
    array.sort()
    
    # Step 2: Initialize two pointers. 
    # 'left' starts at the beginning of the array.
    # 'right' starts at the end of the array.
    left = 0
    right = len(array) - 1
    
    # Step 3: Loop while 'left' pointer is less than 'right' pointer.
    while left < right:
        # Calculate the current sum of the values at the two pointers.
        currentSum = array[left] + array[right]
        
        # Step 4: Check if the current sum is equal to the target sum.
        if currentSum == targetSum:
            # If it is, return the pair of numbers.
            return [array[left], array[right]]
        # Step 5: If the current sum is less than the target sum,
        # move the 'left' pointer to the right to increase the sum.
        elif currentSum < targetSum:
            left += 1
        # Step 6: If the current sum is greater than the target sum,
        # move the 'right' pointer to the left to decrease the sum.
        elif currentSum > targetSum:
            right -= 1
    
    # Step 7: If no pair is found that sums to the target sum,
    # return an empty list.
    return []

# Example of calling the function with input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

# Calling the function and printing the result
result = twoNumberSum(array, targetSum)
print(result)  # Output should be [11, -1] or [-1, 11] (order doesn't matter)
