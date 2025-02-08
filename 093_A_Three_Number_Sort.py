# ----------------------------- Problem Statement -----------------------------
# You are given an array of integers and an array of three distinct integers called 'order'.
# The input array contains only these three integers in any order and any frequency.
# Your task is to sort the array **in-place** so that its elements are ordered
# according to the sequence specified in the 'order' array.

# For example, if the input array is:
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# and the order = [0, 1, -1]
# Then the output should be:
# [0, 0, 0, 1, 1, 1, -1, -1]

# The goal is to solve this in linear time and constant space (in-place sorting).

# ----------------------------- Explanation -----------------------------
# The algorithm follows a three-pointer technique similar to the Dutch National Flag problem:
# - firstValue: the element that should appear first in the sorted array
# - secondValue: the element that should appear second
# - The third element is implied (remaining element in 'order')

# We use three pointers:
# - firstIdx: where to place the next firstValue
# - secondIdx: current index being examined
# - thirdIdx: where to place the next thirdValue (i.e., the one not equal to firstValue or secondValue)



# ----------------------------- Code Execution Theory -----------------------------
def threeNumberSort(array, oreder):  # Function to sort the array based on a custom three-element order
    firstValue = oreder[0]  # The first value in the desired order
    secondValue = oreder[1]  # The second value in the desired order

    # Initialize three pointers:
    # firstIdx - where the next firstValue will be placed
    # secondIdx - the current index being scanned
    # thirdIdx - where the next third (last) value will be placed
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

    # Loop until the scanning index crosses the boundary for the third section
    while secondIdx <= thirdIdx:
        value = array[secondIdx]  # Get the current value at secondIdx

        if value == firstValue:
            # If the value is the firstValue, swap it to the front (firstIdx)
            array[secondIdx], array[firstIdx] = array[firstIdx], array[secondIdx]
            firstIdx += 1  # Move the firstIdx forward to the next open position
            secondIdx += 1  # Move the scan pointer forward
        elif value == secondValue:
            # If the value is the secondValue, it’s already in the correct middle section
            secondIdx += 1  # Just move the scan pointer forward
        else:
            # Otherwise, it must be the thirdValue (the one not explicitly named)
            # Swap it to the end (thirdIdx)
            array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
            thirdIdx -= 1  # Move the thirdIdx backward to the next open position
            # Do not increment secondIdx here because the swapped value may be firstValue or secondValue
            # and needs to be evaluated in the next iteration

    return array  # Return the sorted array


# ----------------------------- Dummy Data -----------------------------
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

# ----------------------------- Function Call -----------------------------
sorted_array = threeNumberSort(array, order)

# ----------------------------- Output -----------------------------
print(sorted_array)  # Output: [0, 0, 0, 1, 1, 1, -1, -1]
