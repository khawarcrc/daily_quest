# Problem Statement:
# Given an array of integers, write a function that shifts all elements of the array to the right by one position. 
# The last element of the array should wrap around to the first position. 
# If the array is empty, the function should return an empty array.

# Steps to Solve:
# 1. Check if the input array is empty.
#    - If it is empty, return the empty array.
#
# 2. Initialize a new list called `shiftedArray` with the same length as the input array, filled with zeros.
#
# 3. Set the first element of `shiftedArray` to the last element of the input array. 
#
# 4. Iterate through the input array from the first element to the second-to-last element:
#    - For each element, shift it to the right by assigning its value to the next position in `shiftedArray`.
#
# 5. After completing the iteration, return the `shiftedArray` containing the shifted elements.




def shiftRight(array):
    # Check if the array is empty
    if len(array) == 0:
        return array
    
    # Initialize a list to store the shifted elements
    shiftedArray = [0 for _ in array]

    # Set the last element of the input array as the first element of shiftedArray
    shiftedArray[0] = array[-1]

    # Iterate through each element of the input array except the last one
    for idx in range(len(array) - 1):
        # Shift elements to the right by one position
        shiftedArray[idx + 1] = array[idx]

    # Return the shifted array
    return shiftedArray


# Test the function with an example array
array = [1, 2, 3, 4, 5]
result = shiftRight(array)
print(f"Final shifted array: {result}")



# def shiftRight(array):
#     # Check if the array is empty
#     if len(array) == 0:
#         return array
    
#     # Initialize a list to store the shifted elements
#     shiftedArray = [0 for _ in array]
#     print(f"Initialized shiftedArray with zeros: {shiftedArray}")

#     # Set the last element of the input array as the first element of shiftedArray
#     shiftedArray[0] = array[-1]
#     print(f"Moved last element {array[-1]} to the first position: {shiftedArray}")

#     # Iterate through each element of the input array except the last one
#     for idx in range(len(array) - 1):
#         # Shift elements to the right by one position
#         shiftedArray[idx + 1] = array[idx]
#         print(f"Shifted element {array[idx]} from index {idx} to index {idx + 1}: {shiftedArray}")

#     # Return the shifted array
#     return shiftedArray


# # Test the function with an example array
# array = [1, 2, 3, 4, 5]
# result = shiftRight(array)
# print(f"Final shifted array: {result}")
