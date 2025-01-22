# """
# Problem Statement:
# The task is to generate all possible permutations of a given array of unique elements.
# A permutation is a unique arrangement of the elements of the array, where the order matters.
# For example, for the input array [1, 2, 3], the possible permutations are:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].

# Explanation of the Problem:
# 1. A permutation is a rearrangement of the elements of an array in every possible order.
# 2. The number of permutations of an array with 'n' elements is n! (factorial of n).
#    For example, an array with 3 elements will have 3! = 6 permutations.
# 3. The solution involves recursively selecting an element, adding it to the current
#    permutation being built, and repeating the process with the remaining elements.

# Code Execution Theory:
# 1. The main function `getPermutations` initializes an empty list to store the final permutations
#    and calls the recursive helper function `permutationsHelper`.

# 2. The recursive function `permutationsHelper` does the following:
#    - Checks if the input array is empty and if there is a valid `currentPermutation`.
#      If true, it appends the `currentPermutation` to the list of permutations.
#    - Otherwise, it iterates through each element in the array.
#      For each element:
#        a. The current element is removed from the array to form a smaller array (`newArray`).
#        b. The current element is added to the ongoing permutation (`currentPermutation`).
#        c. A recursive call is made with the `newArray`, updated `currentPermutation`,
#           and the list to store permutations.

# 3. The recursion continues until all elements have been used in a permutation.
#    Each recursive call reduces the size of the array and adds one element to the
#    `currentPermutation`.

# 4. When the recursion completes, the `permutations` list contains all unique
#    arrangements of the input array's elements.

# 5. Finally, the `getPermutations` function returns the list of permutations to the caller.

# Time Complexity Analysis:
# - The algorithm generates n! permutations, where n is the size of the input array.
# - For each permutation, the helper function processes the array, resulting in an
#   overall time complexity of O(n * n!).

# Space Complexity Analysis:
# - The space complexity is O(n!) for storing the permutations and O(n) for the recursion
#   stack depth.
# """


def getPermutations(array):
    # """
    # Generates all possible permutations of the given array.

    # Args:
    #     array (list): The input array for which permutations need to be generated.

    # Returns:
    #     list: A list containing all permutations of the input array.
    # """
    # List to store all the permutations
    permutations = []
    # Call the helper function to generate permutations
    permutationsHelper(array, [], permutations)
    return permutations


def permutationsHelper(array, currentPermutation, permutations):
    # """
    # Recursive helper function to generate permutations.

    # Args:
    #     array (list): Remaining elements to permute.
    #     currentPermutation (list): The current permutation being built.
    #     permutations (list): A list to store all the generated permutations.
    # """
    # Base case: If the array is empty and we have a current permutation
    if not len(array) and len(currentPermutation):
        # Add the current permutation to the list of permutations
        permutations.append(currentPermutation)
    else:
        # Iterate through each element in the array
        for i in range(len(array)):
            # Remove the current element and keep the rest in a new array
            newArray = array[:i] + array[i + 1 :]
            # Add the current element to the ongoing permutation
            newPermutation = currentPermutation + [array[i]]
            # Recursive call with the updated arrays
            permutationsHelper(newArray, newPermutation, permutations)


# Dummy data
input_array = [1, 2, 3]  # Example input
result = getPermutations(input_array)  # Get permutations
print("Permutations:", result)  # Display the permutations


#                     []
#                   / |  \
#                 1   2   3        (Choose each element)
#               /     |     \
#            [1]    [2]   [3]      (Remaining array shrinks)
#           /  \    /  \   /  \
#        [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
#        /      /      /     /      /     /
#   [1,2,3] [1,3,2] [2,1,3][2,3,1][3,1,2][3,2,1]
