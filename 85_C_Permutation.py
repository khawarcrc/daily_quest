# Problem Statement:
# The task is to generate all possible permutations of a given array.
# A permutation is a specific arrangement of elements in a sequence where the order matters.
# For example, for an array [1, 2, 3], the possible permutations are:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

# Problem Explanation:
# The problem involves finding all unique orderings of the elements in the input array.
# This can be achieved using recursion and backtracking:
# 1. Fix one element at a time in the first position.
# 2. Recursively generate permutations for the remaining elements.
# 3. Swap elements back to their original positions after processing a branch to ensure the array
#    is restored for subsequent iterations (backtracking).

# Code Execution Theory:
# 1. The `getPermutations` function initializes an empty list to store permutations.
#    It then calls the helper function `permutationsHelper` with the initial index set to 0.
# 2. The `permutationsHelper` function:
#    - Checks if the current index `i` has reached the last index of the array.
#      If so, it appends a copy of the array to the list of permutations.
#    - Otherwise, it iterates through the array from the current index `i` to the end:
#      a. Swaps the element at `i` with the element at the current iteration index `j`.
#      b. Calls itself recursively with the next index (`i + 1`).
#      c. After returning from the recursion, swaps back the elements to restore the original array state.
# 3. The `swap` function exchanges two elements in the array at the specified indices.
#    It ensures that the elements are correctly rearranged during recursion and backtracking.

# Key Concepts:
# - **Recursion:** The helper function is called recursively to generate permutations by fixing one element
#   and permuting the remaining elements.
# - **Backtracking:** After processing a permutation branch, the elements are swapped back to their
#   original positions, ensuring the array remains unaltered for subsequent branches.
# - **Base Case:** The recursion stops when the current index is the last index, and the array is added
#   to the permutations list.
# - **Array Copy:** A copy of the array is appended to avoid mutations in the stored permutations.


# Time Complexity:
# - Generating permutations involves exploring all possible arrangements of the elements.
# - For an array of size `n`, there are `n!` permutations.
# - The time complexity is O(n * n!), where `n` comes from the array copy operation.

# Space Complexity:
# - Space is required to store the generated permutations and for the recursion stack.
# - Space complexity is O(n * n!) for storing permutations and O(n) for the recursion stack depth.


def getPermutations(array):
    """
    Function to generate all permutations of a given array.
    Args:
        array (list): The input array for which permutations are to be generated.
    Returns:
        list: A list of all possible permutations of the input array.
    """
    permutations = []  # Initialize an empty list to store permutations.
    permutationsHelper(0, array, permutations)  # Start the helper function from index 0.
    return permutations  # Return the list of generated permutations.


def permutationsHelper(i, array, permutations):
    """
    Helper function to recursively generate permutations.
    Args:
        i (int): The current index being fixed.
        array (list): The array being permuted.
        permutations (list): The list storing all permutations.
    """
    # Base case: If the current index is the last index of the array.
    if i == len(array) - 1:
        permutations.append(array[:])  # Append a copy of the current array to the permutations list.
    else:
        # Iterate through all elements from the current index to the end of the array.
        for j in range(i, len(array)):
            swap(array, i, j)  # Swap the current index with the iteration index.
            permutationsHelper(i + 1, array, permutations)  # Recursive call with the next index.
            swap(array, i, j)  # Swap back to restore the original state (backtracking).


def swap(array, i, j):
    """
    Function to swap two elements in an array.
    Args:
        array (list): The array where elements will be swapped.
        i (int): The index of the first element.
        j (int): The index of the second element.
    """
    array[i], array[j] = array[j], array[i]  # Swap the elements at index i and j.


# Dummy data to test the function
input_array = [1, 2, 3]  # Example array
result = getPermutations(input_array)  # Generate all permutations of the array

# Print the result
print("Permutations of the array:", result)



# Example Walkthrough:
# Input Array: [1, 2, 3]
# Step 1: Fix 1 -> Permute [2, 3] -> Results in [1, 2, 3] and [1, 3, 2]
# Step 2: Fix 2 -> Permute [1, 3] -> Results in [2, 1, 3] and [2, 3, 1]
# Step 3: Fix 3 -> Permute [1, 2] -> Results in [3, 1, 2] and [3, 2, 1]
# Output: All 6 permutations are generated and stored in the result list.
