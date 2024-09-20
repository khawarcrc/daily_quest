# Problem Statement:
# You need to sort a list of integers in ascending order using the Bubble Sort algorithm.
# Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# The process continues until no swaps are needed, indicating that the list is sorted.

# Steps to Solve the Problem:
# 1. Initialize a flag `isSorted` to keep track of whether the list is sorted. Start with `isSorted` set to False.
# 2. Initialize a `counter` to keep track of the number of passes through the list. Start with `counter` set to 0.
# 3. Begin a while loop that runs as long as `isSorted` is False.
#     a. Assume the list is sorted at the beginning of this pass by setting `isSorted` to True.
#     b. Iterate through the list from the beginning to the last unsorted element, which is determined by `len(array) - 1 - counter`.
#         i. Compare each element with the next one.
#         ii. If the current element is greater than the next element, swap them and set `isSorted` to False.
#     c. Increment the `counter` to reduce the range of comparison in the next pass.
# 4. Continue looping until `isSorted` remains True, indicating the list is fully sorted.
# 5. Return the sorted list after the while loop completes.

# Scenario:
# Given a list of integers, such as [64, 34, 25, 12, 22, 11, 90], you need to sort this list in ascending order.
# The Bubble Sort algorithm will process the list by repeatedly swapping adjacent elements to move larger elements to the end.
# This process will be repeated until no more swaps are needed, resulting in the sorted list [11, 12, 22, 25, 34, 64, 90].


def bubbleSort(array):
    # Initialize the flag to check if the array is sorted
    isSorted = False
    # Initialize counter to keep track of the number of passes
    counter = 0

    # Continue looping until no more swaps are needed
    while not isSorted:
        # Assume the array is sorted at the beginning of this pass
        isSorted = True

        # Iterate through the array, ignoring the last 'counter' elements
        for i in range(len(array) - 1 - counter):
            # Compare adjacent elements
            if array[i] > array[i + 1]:
                # Swap if the current element is greater than the next element
                swap(i, i + 1, array)
                # Set the flag to False because a swap occurred
                isSorted = False

        # Increment counter to reduce the range of the next pass
        counter += 1

    # Return the sorted array
    return array


def swap(i, j, array):
    # Swap the elements at indices i and j in the array
    array[i], array[j] = array[j], array[i]


# Dummy data for testing
dummy_data = [64, 34, 25, 12, 22, 11, 90]

# Execute bubbleSort on the dummy data
sorted_data = bubbleSort(dummy_data)

# Print the sorted data
print("Sorted Array:", sorted_data)
