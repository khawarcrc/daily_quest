# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)


# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     potentialMatch = array[middle]
#     if target == potentialMatch:
#         return middle
#     elif target < potentialMatch:
#         return binarySearchHelper(array, target, left, middle - 1)
#     else:
#         return binarySearchHelper(array, target, middle + 1, right)

# Problem Statement:
# Implement a function `binarySearchHelper` that searches for a target value in a sorted array using the binary search algorithm.
# The function should return the index of the target if it is found, and return -1 if the target is not present in the array.
# Binary search is an efficient algorithm with a time complexity of O(log n), as it repeatedly halves the search space.

# Steps to solve:
# 1. Initialize two pointers, `left` and `right`, representing the current search boundaries within the array.
# 2. While `left` is less than or equal to `right`, perform the following steps:
#    a. Calculate the middle index using the formula: middle = (left + right) // 2.
#    b. Compare the value at the middle index (called `potentialMatch`) with the target.
# 3. If the target is equal to the value at the middle index, return the middle index (indicating the target is found).
# 4. If the target is smaller than the middle value, adjust the `right` pointer to `middle - 1` to search the left half of the array.
# 5. If the target is greater than the middle value, adjust the `left` pointer to `middle + 1` to search the right half of the array.
# 6. If the loop terminates and the target is not found (i.e., the `left` pointer exceeds the `right` pointer), return -1 to indicate the target is not present in the array.



def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    # Loop continues as long as the search space is valid (left <= right)
    while left <= right:
        # Calculate the middle index
        middle = (left + right) // 2
        
        # Get the value at the middle index
        potentialMatch = array[middle]
        
        # Check if the middle element is the target
        if target == potentialMatch:
            # If yes, return the middle index (target found)
            return middle
        # If the target is smaller than the middle element, discard the right half
        elif target < potentialMatch:
            right = middle - 1
        # If the target is greater than the middle element, discard the left half
        else:
            left = middle + 1
    
    # If target is not found, return -1
    return -1

# Dummy data for testing
# Example sorted array: [1, 3, 5, 7, 9, 11, 13, 15]
# Target to find: 9
# Binary search will check middle elements and adjust the range:
# 1st check: middle = 7 (index 3) -> target > 7, search right half
# 2nd check: middle = 11 (index 5) -> target < 11, search left half
# 3rd check: middle = 9 (index 4) -> target found, return index 4

# Call the function with the dummy data
print(binarySearchHelper([1, 3, 5, 7, 9, 11, 13, 15], 9, 0, 7))
# Expected output: 4 (because 9 is at index 4 in the array)

