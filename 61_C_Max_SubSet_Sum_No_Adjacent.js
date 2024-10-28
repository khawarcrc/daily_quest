function maxSubSetSumNoAdjacent(array) {
    // If the array is empty, return 0 as there are no elements to sum.
    if (array.length === 0) {
        return 0;
    }
    // If the array has only one element, return that element as the max sum.
    else if (array.length === 1) {
        return array[0];
    }

    // Initialize `second` as the first element, `first` as the max of the first two elements.
    let second = array[0];
    let first = Math.max(array[0], array[1]);

    // Loop through the rest of the array starting from the third element.
    for (let i = 2; i < array.length; i++) {
        // Calculate the current max sum by comparing:
        // - the previous max sum (`first`)
        // - the sum of `second` + current element
        let current = Math.max(first, second + array[i]);

        // Move `first` and `second` up to the next positions for the next iteration.
        second = first;
        first = current;
    }

    // The `first` variable holds the maximum sum with no adjacent elements.
    return first;
}

// Dummy data to test the function
const array = [3, 7, 4, 6, 5];
console.log(maxSubSetSumNoAdjacent(array));  // Expected output: 13 (7 + 6)
