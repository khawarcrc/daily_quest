# Problem Statement:
# We are given an unsorted array of numbers, and the task is to sort this array in ascending order
# using the Insertion Sort algorithm. The algorithm works by iteratively taking each element from the 
# unsorted portion and inserting it into its correct position in the sorted portion of the array.

# Steps to Solve the Problem:

# 1. Initialize the sorting process:
#    - Start from the second element of the array (index 1), since the first element is already considered "sorted."

# 2. Outer loop (Iterate through the unsorted array):
#    - Loop through each element in the array from index 1 to the end.
#    - For each element, set a variable 'j' equal to the current index 'i' to track the current position.

# 3. Inner loop (Insert the current element into the sorted portion):
#    - Compare the element at position 'j' with the one before it (i.e., 'j-1').
#    - Continue this comparison as long as:
#        a) The current index 'j' is greater than 0 (to ensure you are still within the array bounds).
#        b) The element at position 'j' is smaller than the element before it (i.e., array[j] < array[j-1]).

# 4. Swap elements if they are out of order:
#    - If the current element is smaller than the previous one, swap the two elements.
#    - After swapping, decrement 'j' by 1 to continue checking and swapping the element with the sorted portion to the left.

# 5. Continue moving the element backward:
#    - Continue the inner loop until the current element is in the correct position in the sorted portion of the array.

# 6. Repeat for all elements:
#    - The process will continue until all elements are sorted, and the array will be in ascending order.

# 7. Return the sorted array:
#    - Once all elements are sorted, the function will return the modified array.

def insertionSort(array):  
    # Traverse the array starting from the second element (index 1)
    for i in range(1, len(array)):
        j = i  # Initialize j with the current index i

        # while j > 0 and array[j] < array[j - 1]:
        # The inner loop checks two conditions:
        # j > 0: Ensures that the current element is not at the first position.
        # array[j] < array[j - 1]: Compares the current element with the previous one to see if they are in the wrong order.
        # If both conditions are true, the elements are swapped to move the current element to its correct position in the sorted portion.
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)  # Swap elements if they are in the wrong order
            j -= 1  #  After swapping, j is decremented to continue comparing the newly swapped element with previous elements,
                    #  ensuring that the correct position in the sorted portion is found.

    return array  # Return the sorted array


def swap(i, j, array):  # Function to swap two elements in the array
    array[i], array[j] = array[j], array[i]  # Swap the elements at index i and j


# Example usage with dummy data
array = [5, 2, 9, 1, 5, 6]  # Unsorted array
sorted_array = insertionSort(array)  # Perform insertion sort
print(sorted_array)  # Expected output: [1, 2, 5, 5, 6, 9]
