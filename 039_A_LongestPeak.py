# Problem Statement:
# We are given an array of integers, and we need to find the length of the longest peak.
# A peak is defined as an element that is greater than both its left and right neighbors.
# The peak length includes the peak itself, plus the elements on the left forming the increasing slope,
# and the elements on the right forming the decreasing slope.
# Our task is to return the length of the longest peak in the array.

# Steps to Solve:
# 1. Initialize a variable to store the longest peak length (set to 0 initially).
# 2. Iterate through the array, starting from the second element and stopping at the second-last element.
#    - This is because a peak needs both left and right neighbors.
# 3. For each element, check if it is a peak by comparing it with its left and right neighbors.
#    - If the element is not a peak, continue to the next element.
# 4. If a peak is found, expand leftwards to find how far the increasing slope goes.
# 5. Expand rightwards to find how far the decreasing slope goes.
# 6. Calculate the length of the current peak by measuring the distance between the left and right boundaries.
# 7. Update the longest peak length if the current peak is longer than the previously recorded peaks.
# 8. Move the index to the end of the current peak (i.e., skip over the peak) to avoid re-checking it.
# 9. After the loop completes, return the longest peak length found.


def longestPeak(array):
    # Initialize variable to store the length of the longest peak found
    longestPeakLength = 0
    # Start loop from the second element (1) to ensure we can check for peaks
    i = 1

    # Traverse the array until the second last element
    while i < len(array) - 1:
        # Check if the current element is a peak
        # array[0] < array[1] > array[2] => 1 < 3 > 2 -> True, it is a peak
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]

        # Expand left to find how far the increasing slope goes
        # leftIndex starts at i - 2 = 1 - 2 = -1 (out of bounds, stop immediately)
        leftIndex = i - 2

        # Expand right to find how far the decreasing slope goes
        # rightIndex starts at i + 2 = 1 + 2 = 3, 
        # array[3] = 5, array[2] = 2 -> stop, as 5 > 2
        rightIndex = i + 2

        # Calculate the current peak length (rightIndex - leftIndex - 1)
        # rightIndex = 3, leftIndex = -1 -> peak length = 3 - (-1) - 1 = 3
        currentPeakLength = rightIndex - leftIndex - 1

        # Update longest peak length if the current one is longer
        # longestPeakLength = max(0, 3) -> 3
        longestPeakLength = max(longestPeakLength, currentPeakLength)

        # Skip over the processed peak and move to the next potential peak
        # i = rightIndex = 3
        i = rightIndex

    # Check next element starting from i = 3
    # array[2] < array[3] > array[4] => 2 < 5 > 4 -> True, it is a peak
    # Expand left -> leftIndex starts at i - 2 = 1
    # Continue expanding left until leftIndex = -1 (array[1] < array[2])
    # Expand right -> rightIndex starts at 5 -> stop at 7 (array[5] > array[6])
    # peak length = 7 - (-1) - 1 = 7

    # longestPeakLength = max(3, 7) -> 7

    # Skip over the processed peak i = rightIndex = 7

    # Continue until no more peaks, longestPeakLength = 7

    return longestPeakLength


# Dummy data to test the function
array = [1, 3, 2, 5, 4, 10, 6, 2, 1, 9, 8, 7]
print(longestPeak(array))  # Output: 6 (for the peak 1-3-2-5-4-10-6)
