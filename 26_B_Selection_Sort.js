function selectionSort(array) {
    // Initialize current index to start at the first element
    let currentIndex = 0;

    // Continue until we reach the second-to-last element
    while (currentIndex < array.length - 1) {
        // Assume the current index contains the smallest element in the unsorted portion
        let smallestIndex = currentIndex;

        // Iterate over the unsorted portion of the array (from currentIndex + 1 to the end)
        for (let i = currentIndex + 1; i < array.length; i++) {
            // If we find an element smaller than the current smallest, update smallestIndex
            if (array[smallestIndex] > array[i]) {
                smallestIndex = i;
            }
        }

        // Swap the current element with the smallest found in the unsorted portion
        swap(currentIndex, smallestIndex, array);

        // Move to the next element, increasing the size of the sorted portion
        currentIndex++;
    }

    // Return the sorted array
    return array;
}

function swap(i, j, array) {
    // Swap the elements at indices i and j
    [array[i], array[j]] = [array[j], array[i]];
}

// Example usage with dummy data
const data = [64, 25, 12, 22, 11];
const sortedData = selectionSort(data);
console.log(`Sorted array: ${sortedData}`);
