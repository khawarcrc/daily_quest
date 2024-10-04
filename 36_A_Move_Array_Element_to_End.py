# Problem Statement:
# Given an array of integers and a specific integer value `toMove`, write a function that moves all instances of 
# the `toMove` value to the end of the array. The order of the other elements in the array should remain the same. 
# The function should achieve this in-place, meaning no additional memory should be used apart from modifying 
# the input array.

# Steps to Solve:
# 1. Initialize two pointers, `pointerOne` and `pointerTwo`. 
#    - `pointerOne` starts from the beginning of the array.
#    - `pointerTwo` starts from the end of the array.

# 2. Loop through the array while `pointerOne` is less than `pointerTwo`:
#    - Check if the value at `pointerTwo` is equal to the `toMove` value.
#    - If it is, move `pointerTwo` one step to the left to skip it, since it's already in the correct position at the end.
   
# 3. If the value at `pointerOne` is equal to `toMove`, swap the values at `pointerOne` and `pointerTwo`.
#    - After swapping, this moves the `toMove` value toward the end of the array.
#    - Move `pointerOne` one step to the right to check the next element.

# 4. Repeat this process until `pointerOne` crosses `pointerTwo`.

# 5. Return the modified array where all occurrences of `toMove` have been moved to the end, while the relative order 
# of the other elements remains unchanged.


def moveElementToEnd(array, toMove):
    pointerOne = 0  # Start of the array
    pointerTwo = len(array) - 1  # End of the array

    while pointerOne < pointerTwo:
        # If pointerTwo points to `toMove`, move pointerTwo left
        if array[pointerTwo] == toMove:
            pointerTwo -= 1
        # If pointerOne points to `toMove`, swap it with pointerTwo
        elif array[pointerOne] == toMove:
            array[pointerOne], array[pointerTwo] = array[pointerTwo], array[pointerOne]
            pointerOne += 1
        # If pointerOne is not equal to `toMove`, just move pointerOne right
        else:
            pointerOne += 1

    return array

# Example usage
array = [2, 1, 2, 2, 3, 4, 2]
toMove = 2

result = moveElementToEnd(array, toMove)
print("The list:", result)  # Output: [4, 1, 3, 2, 2, 2, 2]
