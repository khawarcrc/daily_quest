function bubbleSort(array) {
    // Initialize the flag to check if the array is sorted
    let isSorted = false;
    // Initialize counter to keep track of the number of passes
    let counter = 0;

    // Continue looping until no more swaps are needed
    while (!isSorted) {
        // Assume the array is sorted at the beginning of this pass
        isSorted = true;

        // Iterate through the array, ignoring the last 'counter' elements
        for (let i = 0; i < array.length - 1 - counter; i++) {
            // Compare adjacent elements
            if (array[i] > array[i + 1]) {
                // Swap if the current element is greater than the next element
                swap(i, i + 1, array);
                // Set the flag to false because a swap occurred
                isSorted = false;
            }
        }

        // Increment counter to reduce the range of the next pass
        counter++;
    }

    // Return the sorted array
    return array;
}

function swap(i, j, array) {
    // Swap the elements at indices i and j in the array
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

// Dummy data for testing
let dummy_data = [64, 34, 25, 12, 22, 11, 90];

// Execute bubbleSort on the dummy data
let sorted_data = bubbleSort(dummy_data);

// Print the sorted data
console.log("Sorted Array:", sorted_data);
