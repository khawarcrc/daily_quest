# Problem Statement:
# The problem is to generate all possible subsets (the power set) of a given array.
# A subset can be empty, contain one element, or any combination of elements from the array.
# For example, the powerset of [1, 2] is [[], [1], [2], [1, 2]].

# Code Execution Theory:
# - This problem uses recursion to calculate subsets for progressively smaller arrays.
# - At each recursive step, subsets are created for the current element by adding it to existing subsets.
# - The base case returns an empty subset when the index is less than zero.
# - This process ensures that all possible subsets of the input array are generated.


def powerset(array, idx=None):

    # If idx is not provided (initial call), set it to the last index of the array
    if idx is None:
        idx = len(array) - 1

    # Base case: If idx is less than 0, return a list containing the empty subset
    elif idx < 0:
        return [[]]

    # Retrieve the current element at idx
    currentElemenet = array[idx]

    # Recursively compute the powerset for the array excluding the current element
    subsets = powerset(array, idx - 1)

    # Add the current element to each subset in the list of subsets
    for i in range(len(subsets)):
        # Create a new subset by appending the current element to the existing subset
        currentSubset = subsets[i]
        subsets.append(currentSubset + [currentElemenet])

    # Return the complete list of subsets
    return subsets


# Dummy Data:
array = [1, 2, 3]  # Input array for which powerset needs to be calculated
result = powerset(array)  # Generate the powerset
print(result) 

# Execution:
# Input: [1, 2, 3]
# Recursive calls:
# 1. powerset([1, 2, 3], idx=2) -> Process subsets with and without 3
# 2. powerset([1, 2, 3], idx=1) -> Process subsets with and without 2
# 3. powerset([1, 2, 3], idx=0) -> Process subsets with and without 1
# 4. powerset([1, 2, 3], idx=-1) -> Base case returns [[]]
# Final output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
