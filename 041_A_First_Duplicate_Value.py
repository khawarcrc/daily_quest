# Problem Statement:
# Given an array of integers, the task is to find the first duplicate value 
# that occurs in the array. A duplicate value is defined as an integer that 
# appears more than once in the array. If a duplicate exists, the function 
# should return the value of the first duplicate that occurs. If no duplicates 
# are found, the function should return -1.
#
# The challenge is not only to find duplicates but to identify the one that 
# appears first, i.e., the one that occurs with the minimum second index in 
# the array. If there are no duplicate values, the function should return -1.

# Theory:
# The idea behind this solution is to loop through the array and compare 
# each element with the elements that come after it. If a duplicate is found, 
# the index of the second occurrence is stored. By the end of the loop, 
# the function will know the first duplicate by identifying the element with 
# the smallest second occurrence index.

# To achieve this:
# - We initialize a variable `minimumSecondIndex` to the length of the array, 
#   which serves as a placeholder to track the index of the second occurrence 
#   of a duplicate value.
# - We loop over the array starting from the first element, and for each element, 
#   we compare it with the rest of the elements in the array (using a nested loop).
# - If a duplicate is found (i.e., two elements are the same), we compare the 
#   current second occurrence index (`j`) with the existing `minimumSecondIndex` 
#   and update it if the current index is smaller.
# - After the loop, if `minimumSecondIndex` has not been updated (i.e., no 
#   duplicates were found), we return -1. Otherwise, we return the value at 
#   `minimumSecondIndex`.

# This solution uses a brute-force approach, meaning that it will compare 
# every element with every other element in the array, resulting in a time 
# complexity of O(n^2), where n is the length of the array. This is not the 
# most efficient solution but is easy to understand and implement.

# The overall algorithm involves:
# - Two nested loops: The outer loop iterates through each element of the array, 
#   and the inner loop checks for any duplicates by comparing the element at 
#   the outer loop index with the subsequent elements in the array.
# - If a duplicate is found, the second occurrence index is compared with the 
#   minimum index found so far to ensure that the first duplicate (with the 
#   smallest second index) is returned.

# Alternative efficient solutions could use a set or dictionary (hashmap) 
# to track the first occurrence of each element, allowing for a linear time 
# complexity O(n) solution.



# Solution Implementation:



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
