function mergeOverlappingIntervals(intervals) {
    // Sort the intervals based on the starting point
    const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);

    // Initialize a list to hold the merged intervals
    const mergedIntervals = [];

    // Start with the first interval and add it to the merged list
    let currentInterval = sortedIntervals[0];
    mergedIntervals.push(currentInterval);

    // Iterate through the sorted intervals
    for (let i = 1; i < sortedIntervals.length; i++) {
        const nextInterval = sortedIntervals[i];
        
        // Unpack the current interval's end value
        const currentIntervalEnd = currentInterval[1];

        // Unpack the next interval's start and end values
        const nextIntervalStart = nextInterval[0];
        const nextIntervalEnd = nextInterval[1];

        // Check if the current interval overlaps with the next interval
        if (currentIntervalEnd >= nextIntervalStart) {
            // Merge the two intervals by updating the end of the current interval
            currentInterval[1] = Math.max(currentIntervalEnd, nextIntervalEnd);
        } else {
            // No overlap, so add the next interval to the merged list
            currentInterval = nextInterval;
            mergedIntervals.push(currentInterval);
        }
    }

    return mergedIntervals;
}

// Dummy data: list of intervals
const dummyData = [[3, 4], [1, 2], [2, 5], [7, 8], [5, 6]];

// Call the function with dummy data and log the result
const result = mergeOverlappingIntervals(dummyData);
console.log("Merged Intervals:", result);
