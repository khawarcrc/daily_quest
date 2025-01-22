# Problem Statement:
# Write a function to generate the powerset of a given array.
# A powerset is the set of all subsets, including the empty set and the array itself.
# For example, the powerset of [1, 2] is [[], [1], [2], [1, 2]].

# Code Explanation:
# The function works by starting with an empty subset and iteratively adding elements from the input array
# to existing subsets to form new subsets. The result is a list containing all subsets of the input array.


# Execution Theory:
# 1. Start with `subsets = [[]]`, which represents the empty subset.
# 2. For each element in the input array:
#    - Iterate over all subsets already in `subsets`.
#    - For each subset, create a new subset that includes the current element.
#    - Add the new subset to `subsets`.
# 3. The loop ensures that every subset of the input array is considered,
#    both with and without the current element.
# 4. By the end of the process, `subsets` contains all possible subsets of the array.
#
# Complexity Analysis:
# - Time Complexity: O(n * 2^n), where n is the length of the input array.
#   This is because there are 2^n subsets, and we process each one as we add elements.
# - Space Complexity: O(n * 2^n), as the resulting powerset list contains 2^n subsets,
#   and each subset can have up to n elements.

def powerset(array):
    # Initialize the powerset with the empty subset
    subsets = [[]]
    
    # Iterate over each element in the input array
    for element in array:
        # Iterate over the subsets collected so far
        for i in range(len(subsets)):
            # Get the current subset
            currentSubset = subsets[i]
            # Create a new subset by adding the current element to the current subset
            subsets.append(currentSubset + [element])
    
    # Return the final list of subsets (powerset)
    return subsets

# Dummy data for testing the function
input_array = [1, 2, 3]

# Call the function and print the powerset of the input array
print(powerset(input_array))


