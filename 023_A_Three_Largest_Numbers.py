
# Problem Statement:
# Given an array of integers, find the three largest distinct numbers and return them in ascending order. 
# The goal is to identify the top three largest values from the array without sorting it directly.

# Steps to Solve the Problem:

# 1. Initialize a list with three placeholders (None values), which will eventually hold the three largest numbers.
#    - This array will be updated as we iterate through the input array.

# 2. Iterate through each number in the input array:
#    - For each number, check if it should be placed among the top three largest numbers.

# 3. Use a helper function to determine if the current number is larger than any of the existing three largest numbers.
#    - Compare the number against the largest (third position), second largest (second position), and third largest (first position).

# 4. If the number is larger than the largest or second largest or third largest:
#    - Shift the smaller numbers to the left to make space for the new larger number.
#    - Update the list of three largest numbers accordingly.

# 5. Continue the process until all numbers in the input array have been evaluated.

# 6. Finally, return the list of the three largest numbers in ascending order.

def findThreeLargestNumbers(array):
    # Initialize an array to hold the three largest numbers
    # This starts with all None values: [None, None, None]
    threeLargest = [None, None, None]

    # Iterate through each number in the input array
    for num in array:
        # Update the three largest numbers as needed
        updateLargest(threeLargest, num)

    # Return the final three largest numbers in ascending order
    return threeLargest


def updateLargest(threeLargest, num):
    # Check if the current number is larger than the largest (third) value in the array
    if threeLargest[2] is None or num > threeLargest[2]:
        # If so, shift the array and place the number in the largest (third) position
        shiftandUpdate(threeLargest, num, 2)
    # Otherwise, check if it's larger than the second largest number
    elif threeLargest[1] is None or num > threeLargest[1]:
        # If so, shift the array and place the number in the second position
        shiftandUpdate(threeLargest, num, 1)
    # Otherwise, check if it's larger than the third largest number
    elif threeLargest[0] is None or num > threeLargest[0]:
        # If so, shift the array and place the number in the first position
        shiftandUpdate(threeLargest, num, 0)


def shiftandUpdate(array, num, index):
    # This loop shifts the array elements to the left to make room for the new number
    # For example, if we want to insert at index 2 (largest), we shift elements to the left
    for i in range(index + 1):
        # When we reach the index, place the new number there
        if i == index:
            array[i] = num
        # Otherwise, shift the number to the left by copying the next element
        else:
            array[i] = array[i + 1]


# Dummy data for testing:
# Example array: [10, 5, 9, 12, 8, 20, 2]
# Expected result: [10, 12, 20]
print(findThreeLargestNumbers([10, 5, 9, 12, 8, 20, 2]))  # Output: [10, 12, 20]

# Another test case: [1, 5, 9, 3, 7]
# Expected result: [5, 7, 9]
print(findThreeLargestNumbers([1, 5, 9, 3, 7]))  # Output: [5, 7, 9]
