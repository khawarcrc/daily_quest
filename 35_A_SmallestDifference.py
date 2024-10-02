def smallestDifference(arrayOne, arrayTwo):
    # Sort both arrays to facilitate comparison
    arrayOne.sort()
    arrayTwo.sort()

    # Initialize pointers for both arrays
    indexOne = 0
    indexTwo = 0

    # Variables to store the smallest difference and the current difference
    smallest = float("inf")  # Smallest difference found so far
    current = float("inf")   # Current difference between numbers being compared

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
