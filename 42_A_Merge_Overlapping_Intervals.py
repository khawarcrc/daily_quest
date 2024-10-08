# Problem Statement:
# Given a list of intervals, merge all overlapping intervals.
# An interval is defined as a list or tuple with two elements [start, end].
# The merged intervals should not overlap, and if they do, they should be combined into a single interval.

# Example:
# Input: [[3, 4], [1, 2], [2, 5], [7, 8], [5, 6]]
# Output: [[1, 5], [7, 8]]

# Steps to Solve the Problem:
# 1. Sort the list of intervals based on the starting point of each interval.
# 2. Initialize an empty list to hold the merged intervals.
# 3. Add the first interval from the sorted list to the merged intervals.
# 4. Iterate through the sorted intervals starting from the second interval:
#     a. For each interval, unpack the start and end values of the current and next intervals.
#     b. Check if the current interval overlaps with the next interval:
#         i. If they overlap (current interval's end >= next interval's start), merge them:
#             - Update the end of the current interval to the maximum of both ends.
#         ii. If they do not overlap, set the current interval to the next interval and add it to the merged intervals.
# 5. Return the list of merged intervals.


def mergeOverlappingIntervals(intervals):
    # Sort the intervals based on the starting point
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    # Initialize a list to hold the merged intervals
    mergedIntervals = []

    # Start with the first interval and add it to the merged list
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    # Iterate through the sorted intervals
    for nextInterval in sortedIntervals:
        # Unpack the current interval's end value
        _, currentIntervalEnd = currentInterval

        # Unpack the next interval's start and end values
        nextIntervalStart, nextIntervalEnd = nextInterval

        # Check if the current interval overlaps with the next interval
        if currentIntervalEnd >= nextIntervalStart:
            # Merge the two intervals by updating the end of the current interval
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            # No overlap, so add the next interval to the merged list
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals


# Dummy data: list of intervals
dummy_data = [[3, 4], [1, 2], [2, 5], [7, 8], [5, 6]]

# Call the function with dummy data and print the result
result = mergeOverlappingIntervals(dummy_data)
print("Merged Intervals:", result)
