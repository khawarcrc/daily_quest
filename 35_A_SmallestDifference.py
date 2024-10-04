# Problem Statement:
# Given two non-empty arrays of integers, write a function that finds the pair of numbers
# (one from each array) whose absolute difference is closest to zero. Return the pair with
# the smallest difference.

# Steps to solve the problem:

# 1. Sort both arrays in ascending order.
# 2. Initialize two pointers, one for each array, starting at index 0.
# 3. Initialize variables to track the smallest difference found so far and the current difference.
# 4. Use a while loop to traverse both arrays until one of the pointers reaches the end of its array.
# 5. Compare the current numbers from both arrays:
#    a. If the number from the first array is smaller, increase the pointer of the first array.
#    b. If the number from the second array is smaller, increase the pointer of the second array.
#    c. If both numbers are equal, return the pair immediately (since their difference is zero).
# 6. Update the smallest difference and the corresponding pair if the current difference is smaller.
# 7. After the loop ends, return the pair with the smallest difference found.


def smallestDifference(arrayOne, arrayTwo):
    # Sort both arrays to facilitate comparison
    arrayOne.sort()
    arrayTwo.sort()

    # Initialize pointers for both arrays
    indexOne = 0
    indexTwo = 0

    # Variables to store the smallest difference and the current difference
    smallest = float("inf")  # Smallest difference found so far
    current = float("inf")  # Current difference between numbers being compared

    # Variable to store the pair with the smallest difference
    smallestPair = []

    # Iterate over both arrays as long as there are elements in both
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        firstNumber = arrayOne[indexOne]  # Current number from the first array
        secondNumber = arrayTwo[indexTwo]  # Current number from the second array

        # Calculate the difference between the two numbers
        if firstNumber < secondNumber:
            current = secondNumber - firstNumber
            indexOne += 1  # Move pointer for the first array
        elif secondNumber < firstNumber:
            current = firstNumber - secondNumber
            indexTwo += 1  # Move pointer for the second array
        else:
            # If both numbers are equal, the difference is 0, which is the smallest possible
            return [firstNumber, secondNumber]

        # Update the smallest difference and the corresponding pair
        if smallest > current:
            smallest = current
            smallestPair = [firstNumber, secondNumber]

    # Return the pair with the smallest difference
    return smallestPair


# Dummy data to test the function
arrayOne = [10, 20, 14, 16, 18]
arrayTwo = [30, 23, 54, 33, 10]

# Call the function and print the result
result = smallestDifference(arrayOne, arrayTwo)
print("The pair with the smallest difference is:", result)
