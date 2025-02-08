# Problem Statement (Selection Sort):
# Given an array of unsorted integers, sort the array in ascending order using the selection sort algorithm.
# The goal is to repeatedly find the smallest element in the unsorted part of the array and place it at the correct position in the sorted part.
# The algorithm divides the array into two parts: a sorted part (left side) and an unsorted part (right side).
# For each pass through the unsorted part, the smallest element is placed in its correct position in the sorted part.

# Steps to Solve the Problem (Selection Sort):

# 1. Initialization:
#    - Start with an empty sorted part of the array.
#    - Consider the entire array as unsorted initially.

# 2. Loop through the array:
#    - Begin with the first element and mark it as the current index (currentIndex).

# 3. Find the smallest element:
#    - Iterate through the unsorted part of the array (starting from currentIndex + 1).
#    - Compare each element with the current smallest element.
#    - Update the index of the smallest element found (smallestIndex).

# 4. Swap the elements:
#    - Swap the element at currentIndex with the element at smallestIndex (placing the smallest element in the correct position in the sorted part).

# 5. Move to the next unsorted element:
#    - Increment currentIndex by 1 to move to the next element in the unsorted part of the array.

# 6. Repeat steps 3 to 5:


def selectionSort(array):
    # Initialize current index to start at the first element
    currentIndex = 0

    # Continue until we reach the second-to-last element
    while currentIndex < len(array) - 1:
        # Assume the current index contains the smallest element in the unsorted portion
        smallestIndex = currentIndex

        # Iterate over the unsorted portion of the array (from currentIndex + 1 to the end)
        for i in range(currentIndex + 1, len(array)):
            # If we find an element smaller than the current smallest, update smallestIndex
            if array[smallestIndex] > array[i]:
                smallestIndex = i

        # Swap the current element with the smallest found in the unsorted portion
        swap(currentIndex, smallestIndex, array)

        # Move to the next element, increasing the size of the sorted portion
        currentIndex += 1

    # Return the sorted array
    return array


def swap(i, j, array):
    # Swap the elements at indices i and j
    array[i], array[j] = array[j], array[i]


# Example usage with dummy data
data = [64, 25, 12, 22, 11]
sorted_data = selectionSort(data)
print(f"Sorted array: {sorted_data}")
