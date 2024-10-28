# Problem Statement:
# Given an array of integers, write a function `maxSubSetSumNoAdjacent` to find the maximum sum of non-adjacent elements.
# This means that no two selected elements in the sum can be next to each other in the array.
# The function should return 0 if the array is empty, and handle cases where there is only one element.
# This problem is commonly solved using dynamic programming techniques.

# Code Execution Theory:
# - If the array is empty, we return 0.
# - If the array has one element, we return that element because it's the only possible sum.
# - For arrays with two or more elements, we define:
#     * `second` as the value of the first element.
#     * `first` as the maximum of the first and second elements, which sets an initial maximum.
# - We then loop through the array from the third element onward.
#     * For each element, calculate `current` as the maximum value by choosing between:
#         - the previous `first` (i.e., max sum so far)
#         - `second + current element` (adding non-adjacent element sum).
#     * Update `second` to the previous `first`, and `first` to `current` to keep track of new max sums.
# - The result stored in `first` at the end of the loop gives the maximum non-adjacent sum.


 # Reasoning for this approach:
    # - **Dynamic Programming**: This method utilizes dynamic programming to efficiently compute the maximum sum by reusing
    # previously calculated results, avoiding the need for redundant calculations.
    # - **Two Trackers**: We use two variables (`second` and `first`) to keep track of the maximum sums up to the last two
    # non-adjacent elements, allowing us to maintain constant space complexity while iterating through the array.
    # - **Iterative Calculation**: At each step, we decide whether to include the current element based on the maximum sum of
    # previous selections, ensuring that no two adjacent elements are selected in the sum.

def maxSubSetSumNoAdjacent(array):
    # If the array is empty, return 0 as there are no elements to sum.
    if not len(array):
        return 0
    # If the array has only one element, return that element as the max sum.
    elif len(array) == 1:
        return array[0]

    # Initialize `second` as the first element, `first` as the max of first two elements.
    second = array[0]
    first = max(array[0], array[1])

    # Loop through the rest of the array starting from the third element.
    for i in range(2, len(array)):
        # Calculate the current max sum by comparing:
        # - the previous max sum (`first`)
        # - the sum of `second` + current element
        current = max(first, second + array[i])

        # Move `first` and `second` up to the next positions for the next iteration.
        second = first
        first = current

    # The `first` variable holds the maximum sum with no adjacent elements.
    return first

# Dummy data to test the function
array = [3, 7, 4, 6, 5]
print(maxSubSetSumNoAdjacent(array))  # Expected output: 13 (7 + 6)
