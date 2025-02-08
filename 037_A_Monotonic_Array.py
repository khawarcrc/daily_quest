def isMonotonic(array):
    # Initialize two flags to track if the array is non-decreasing and non-increasing
    isNonDecreasing = True  # Assume the array is non-decreasing
    isNonIncreasing = True  # Assume the array is non-increasing

    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # Check if the current element is less than the previous element
        if array[i] < array[i - 1]:
            isNonDecreasing = False  # If so, the array cannot be non-decreasing
        elif array[i] > array[i - 1]:
            isNonIncreasing = False  # If so, the array cannot be non-increasing

    # Return True if the array is either non-decreasing or non-increasing
    return isNonDecreasing or isNonIncreasing


# Test cases to validate the function
test_array_1 = [1, 2, 2, 3]  # Non-decreasing
test_array_2 = [3, 2, 2, 1]  # Non-increasing
test_array_3 = [1, 3, 2]  # Not monotonic
test_array_4 = [1, 1, 1]  # Non-decreasing and non-increasing

# Function calls
print(isMonotonic(test_array_1))  # Output: True
print(isMonotonic(test_array_2))  # Output: True
print(isMonotonic(test_array_3))  # Output: False
print(isMonotonic(test_array_4))  # Output: True
