# Problem statement:
# Kadane's Algorithm finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
# This algorithm efficiently solves the maximum subarray problem with a time complexity of O(n).
# Given an array of positive and negative integers, the goal is to find the subarray with the largest sum.
# Only the maximum sum of the subarray is returned, not the subarray itself.


# Execution theory:
# 1. The algorithm initializes two variables, `max_current` and `max_global`, to the first element of the array.
#    These variables track the maximum sum of a subarray ending at the current position (`max_current`) and
#    the global maximum sum encountered so far (`max_global`).
# 2. The algorithm iterates through the array, starting from the second element.
# 3. For each element:
#    - `max_current` is updated to be the maximum of either the current element itself or the sum of `max_current`
#      plus the current element, effectively deciding whether to start a new subarray or continue the existing one.
#    - `max_global` is updated to be the maximum of `max_global` and `max_current`, storing the highest value found.
# 4. The function returns `max_global`, which holds the maximum sum of any contiguous subarray found in the input.


def kadanesAlgorithm(array):
    # Initialize max_current and max_global with the first element
    max_current = max_global = array[0]

    # Iterate through the array starting from the second element
    for num in array[1:]:
        # Update max_current to be the maximum of the current element
        # or the sum of max_current and the current element
        max_current = max(num, max_current + num)

        # Update max_global if max_current is greater
        if max_current > max_global:
            max_global = max_current

    return max_global


# Example usage with dummy data
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Example array
print("Maximum Sum of Contiguous Subarray:", kadanesAlgorithm(array))
