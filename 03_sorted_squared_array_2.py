def sortedSquaredArray(array):
    # Create a list of zeros with the same length as the input array
    sortedSquares = [0 for _ in array]
    
    # Initialize two pointers: one at the start (smallerValueIdx) and one at the end (largerValueIdx) of the array
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    
    # Iterate through the array in reverse order
    for idx in reversed(range(len(array))):
        # Get the current values at the pointers
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        
        # Compare the absolute values of the current elements
        if abs(smallerValue) > abs(largerValue):
            # If the smaller value has a larger absolute value, square it and place it at the current index
            sortedSquares[idx] = smallerValue * smallerValue
            # Move the smallerValueIdx pointer to the right
            smallerValueIdx += 1
        else:
            # If the larger value has a larger absolute value, square it and place it at the current index
            sortedSquares[idx] = largerValue * largerValue
            # Move the largerValueIdx pointer to the left
            largerValueIdx -= 1
    
    # Return the sorted array of squared values
    return sortedSquares

# Test the function with an example array
array = [-7, -3, 1, 9, 12]
result = sortedSquaredArray(array)
print(result)  # Output should be [1, 9, 49, 81, 144]




# Overall Process
# 1. Initialization:
#    a. Create a new list 'sortedSquares' to store the squared values.
#    b. Initialize two pointers (smallerValueIdx and largerValueIdx) at the start and end of the array.

# 2. Reverse Iteration:
#    a. Iterate through the array in reverse order, from the last index to the first.

# 3. Compare and Fill:
#    a. Compare the absolute values of the elements at the pointers.
#    b. Place the larger square value at the current index and move the corresponding pointer inward.

# 4. Return the result: