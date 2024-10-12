# Problem Statement:
# Given an array of size 'n', find the majority element. The majority element is the element that appears more than
# 'n // 2' times (where 'n' is the size of the array). You are guaranteed that a majority element always exists 
# in the given array.

# Steps to solve the problem:
# 1. Initialize a 'count' variable to 0, which will track the balance between the current candidate for the majority
#    element and other elements.
# 2. Initialize an 'answer' variable to None, which will store the current potential majority element.
# 3. Loop through each element in the array:
#    a. If 'count' is 0, set the current value as the potential majority element ('answer').
#    b. If the current value equals 'answer', increase 'count' by 1 (indicating support for this element).
#    c. Otherwise, decrease 'count' by 1 (indicating opposition to the current candidate).
# 4. Once the loop completes, return 'answer', which will be the majority element.
#    The algorithm guarantees that the element stored in 'answer' will be the majority element.

# Theory:
# The problem uses the **Boyer-Moore Voting Algorithm**. This algorithm works by maintaining a candidate for the 
# majority element and a counter to track how many times that candidate has been supported or opposed. 
# 
# Here's the intuition:
# - If the array contains a majority element, it means that its frequency is greater than half the size of the array.
# - As we iterate through the array, every time we see the majority element, we increase its count.
# - If we encounter a different element, we decrease the count (representing a "vote" against the current candidate).
# - When the count reaches zero, we discard the current candidate and start considering the new element as the majority.
# - By the end of the loop, the remaining candidate will be the majority element because it has dominated the array.
# 
# **Time Complexity**: O(n), where 'n' is the number of elements in the array. The array is traversed once.
# **Space Complexity**: O(1), constant space, as we only use a few variables (count and answer) regardless of the array size.

# Test Cases and Code:

def majorityElement(array):
    # Initialize count to 0 and answer to None
    count = 0
    answer = None

    # Loop through each element in the array
    for value in array:
        # If count is 0, set the current value as the potential majority element
        if count == 0:
            answer = value
        
        # If the current value is the same as the potential majority element, increase count
        if value == answer:
            count += 1
        else:
            # Otherwise, decrease count as this element is different
            count -= 1
    
    # Return the majority element (appears more than n//2 times in the array)
    return answer

# Dummy data to test the function
# Test case 1: The majority element is 3, as it appears 3 times in the array of 5 elements
array1 = [3, 3, 4, 2, 3]
print(majorityElement(array1))  # Output: 3

# Test case 2: The majority element is 5, as it appears 4 times in the array of 6 elements
array2 = [5, 5, 5, 6, 5, 6]
print(majorityElement(array2))  # Output: 5

# Test case 3: The majority element is 2, as it appears 5 times in the array of 9 elements
array3 = [2, 2, 1, 1, 2, 2, 1, 2, 2]
print(majorityElement(array3))  # Output: 2
