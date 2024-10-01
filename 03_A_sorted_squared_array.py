# Overall Process :
# 1. Input: An array of integers is provided.
# 2. Initialization: A new list of zeros is created to store the squared values.
# 3. Square Values: Each value in the input array is squared and stored in the corresponding index of the new list.
# 4. Sorting: The list of squared values is sorted in ascending order.
# 5 .Return: The sorted list of squared values is returned as the output.


def sortedSquaredArray(array):
    # Initialize a list of zeros with the same length as the input array
    sortedSquares = [0 for _ in array]

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



# def sortedSquaredArray(array):
#     # Initialize a list of zeros with the same length as the input array
#     sortedSquares = [0 for _ in array]
#     print(f"Initialized sortedSquares with zeros: {sortedSquares}")

#     # Iterate through each element in the input array
#     for idx in range(len(array)):
#         # Get the value at the current index
#         value = array[idx]
#         print(f"Current value at index {idx}: {value}")

#         # Square the value and store it in the corresponding index of sortedSquares
#         sortedSquares[idx] = value * value
#         print(f"Squared value: {sortedSquares[idx]}")

#     # Sort the array of squared values
#     print(f"Array before sorting: {sortedSquares}")
#     sortedSquares.sort()
#     print(f"Array after sorting: {sortedSquares}")

#     # Return the sorted array of squared values
#     return sortedSquares


# # Test the function with an example array
# array = [-4, -1, 0, 3, 10]
# result = sortedSquaredArray(array)
# print(f"Final sorted squared array: {result}")


