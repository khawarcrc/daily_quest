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
