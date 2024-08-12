
def sortedSquaredArray(array): 
    # Initialize a list of zeros with the same length as the input array
    sortedSquares = [0 for _ in array]
    print(sortedSquares)

    # Iterate through each element in the input array
    for idx in range(len(array)): 
        # Get the value at the current index
        value = array[idx] 
        # Square the value and store it in the corresponding index of sortedSquares
        sortedSquares[idx] = value * value 
    
    # Sort the array of squared values
    sortedSquares.sort()

    # Return the sorted array of squared values
    return sortedSquares

# # Test the function with an example array
array = [-4, -1, 0, 3, 10]
# sortedSquaredArray(array)
result = sortedSquaredArray(array)
print(result)  


# Overall Process :
# 1. Input: An array of integers is provided.
# 2. Initialization: A new list of zeros is created to store the squared values.
# 3. Square Values: Each value in the input array is squared and stored in the corresponding index of the new list.
# 4. Sorting: The list of squared values is sorted in ascending order.
# 5 .Return: The sorted list of squared values is returned as the output.