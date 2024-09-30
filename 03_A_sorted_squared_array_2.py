# Problem Statement:
# Given a sorted array of integers, both negative and positive, write a function that returns a new array containing 
# the squares of each number from the original array, also sorted in non-decreasing order.
# The input array is sorted, but squaring the numbers can disrupt the order, especially with negative numbers.

# Steps to Solve:
# 1. Create an empty array (or list) to store the squared values, initialized with zeros and of the same length as the input array.
# 2. Use two pointers:
#    a. One pointer at the start of the array (for smaller values).
#    b. One pointer at the end of the array (for larger values).
# 3. Iterate through the array in reverse order (starting from the largest index) because the largest squared value will be placed at the highest index.
# 4. During each iteration, compare the absolute values of the elements at both pointers:
#    a. If the absolute value of the number at the start pointer is greater, square it and place it at the current index, then move the start pointer to the right.
#    b. If the absolute value of the number at the end pointer is greater, square it and place it at the current index, then move the end pointer to the left.
# 5. Repeat the comparison and placement until all elements have been squared and placed in the new array in sorted order.
# 6. Return the sorted array of squared values.



# 4. Return the result:
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
