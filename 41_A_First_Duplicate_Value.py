# Problem Statement:
# Given an array of integers, the task is to find the first duplicate value 
# that occurs in the array. A duplicate value is defined as an integer that 
# appears more than once in the array. If a duplicate exists, the function 
# should return the value of the first duplicate that occurs. If no duplicates 
# are found, the function should return -1.

# Steps to Solve the Problem:
# 1. Initialize a variable `minimumSecondIndex` to the length of the array 
#    to keep track of the index of the second occurrence of any duplicate.
# 
# 2. Loop through the array with an index `i` from 0 to the length of the 
#    array:
#    - Retrieve the current value at index `i`.
#    
# 3. For each value at index `i`, create an inner loop with an index `j` 
#    that starts from `i + 1` to the end of the array:
#    - Retrieve the value at index `j`.
#    
# 4. Compare the current value (from index `i`) with the value from index `j`:
#    - If the values are equal (indicating a duplicate), update `minimumSecondIndex` 
#      with the minimum of the current `minimumSecondIndex` and the index `j`.
#
# 5. After both loops, check if `minimumSecondIndex` is still equal to the length of 
#    the array:
#    - If it is, return -1 (indicating no duplicates were found).
#    
# 6. If a duplicate was found, return the value at `minimumSecondIndex`.


def firstDuplicateValue(array):
    # Initialize minimum index for the second occurrence of a duplicate to the length of the array
    minimumSecondIndex = len(array)
    
    # Loop through the array from the start
    for i in range(len(array)):
        # Get the current value at index i
        value = array[i]
        
        # Inner loop to compare the current value with the rest of the elements in the array
        for j in range(i + 1, len(array)):
            # Get the value to compare with
            valueToCompare = array[j]
            
            # If a duplicate is found, update the minimum second index
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)
    
    # If no duplicate was found, return -1
    if minimumSecondIndex == len(array):
        return -1

    # Return the first duplicate value based on the minimum second index
    return array[minimumSecondIndex]


# Dummy data for testing
test_array = [5, 3, 4, 5, 2, 2, 3,1]
print(firstDuplicateValue(test_array))  # Output should be 5, as it's the first duplicate value found.
