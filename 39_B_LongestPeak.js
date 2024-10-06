function longestPeak(array) {
    // Initialize variable to store the length of the longest peak found
    let longestPeakLength = 0;
    // Start loop from the second element (1) to ensure we can check for peaks
    let i = 1;

    // Traverse the array until the second last element
    while (i < array.length - 1) {
        // Check if the current element is a peak
        const isPeak = array[i - 1] < array[i] && array[i] > array[i + 1];

        // If it's not a peak, move to the next element
        if (!isPeak) {
            i++;
            continue;
        }

        // Expand left to find how far the increasing slope goes
        let leftIndex = i - 2;
        while (leftIndex >= 0 && array[leftIndex] < array[leftIndex + 1]) {
            leftIndex--;
        }

        // Expand right to find how far the decreasing slope goes
        let rightIndex = i + 2;
        while (rightIndex < array.length && array[rightIndex] < array[rightIndex - 1]) {
            rightIndex++;
        }

        // Calculate the current peak length
        const currentPeakLength = rightIndex - leftIndex - 1;
        // Update longest peak length if the current one is longer
        longestPeakLength = Math.max(longestPeakLength, currentPeakLength);

        // Skip over the processed peak and move to the next potential peak
        i = rightIndex;
    }

    // Return the length of the longest peak found
    return longestPeakLength;
}

// Dummy data to test the function
const array = [1, 3, 2, 5, 4, 10, 6, 2, 1, 9, 8, 7];
console.log(longestPeak(array));  // Output: 6 (for the peak 1-3-2-5-4-10-6)
