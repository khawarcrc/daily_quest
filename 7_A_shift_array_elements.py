# Overall Process Explained in Points:

# 1. Check for Empty Array:
#    - The function first checks if the input array is empty. 
#    - If it is, the function immediately returns the empty array.

# 2. Initialize a New Array:
#    - A new array (shiftedArray) is created with the same length as the input array.
#    - The new array is initially filled with zeros and will store the elements after they have been shifted to the right.

# 3. Move the Last Element to the First Position:
#    - The last element of the input array is placed in the first position of the shiftedArray.
#    - This is because shifting elements to the right causes the last element to wrap around to the beginning of the array.

# 4. Shift Remaining Elements to the Right:
#    - The function iterates through the input array, moving each element one position to the right in the shiftedArray.
#    - This is done for all elements except the last one, which has already been moved to the first position.

# 5. Return the Shifted Array:
#    - After all elements have been shifted, the function returns the shiftedArray as the result.




def shiftRight(array):
    # Check if the array is empty
    if len(array) == 0:
        return array
    
    # Initialize a list to store the shifted elements
    shiftedArray = [0 for _ in array]
    print(f"Initialized shiftedArray with zeros: {shiftedArray}")

    # Set the last element of the input array as the first element of shiftedArray
    shiftedArray[0] = array[-1]
    print(f"Moved last element {array[-1]} to the first position: {shiftedArray}")

    # Iterate through each element of the input array except the last one
    for idx in range(len(array) - 1):
        # Shift elements to the right by one position
        shiftedArray[idx + 1] = array[idx]
        print(f"Shifted element {array[idx]} from index {idx} to index {idx + 1}: {shiftedArray}")

    # Return the shifted array
    return shiftedArray


# Test the function with an example array
array = [1, 2, 3, 4, 5]
result = shiftRight(array)
print(f"Final shifted array: {result}")
