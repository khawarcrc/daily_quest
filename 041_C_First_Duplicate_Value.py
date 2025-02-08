def firstDuplicateValue(array):
    # Loop through each value in the array
    for value in array:
        # Get the absolute value of the current element
        absValue = abs(value)
        
        # Check if the element at the index corresponding to absValue is already negative
        # This indicates that we've seen this value before (it's a duplicate)
        if array[absValue - 1] < 0:
            return absValue  # Return the first duplicate value
        
        # Mark the value as seen by multiplying the element at the index by -1
        # This changes the sign to negative
        array[absValue - 1] *= -1
    
    # If no duplicates are found, return -1
    return -1


# Dummy data for testing
test_array = [5, 3, 4, 5, 2, 2, 3, 1]
print(firstDuplicateValue(test_array))  # Output will be 5, as it's the first duplicate value found.
