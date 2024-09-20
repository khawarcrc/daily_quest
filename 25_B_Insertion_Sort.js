function insertionSort(array) {
    // Traverse the array starting from the second element (index 1)
    for (let i = 1; i < array.length; i++) {
        let j = i;  // Initialize j with the current index i

        // The inner loop checks two conditions:
        // j > 0: Ensures that the current element is not at the first position.
        // array[j] < array[j - 1]: Compares the current element with the previous one to see if they are in the wrong order.
        // If both conditions are true, the elements are swapped to move the current element to its correct position in the sorted portion.
        while (j > 0 && array[j] < array[j - 1]) {
            swap(j, j - 1, array);  // Swap elements if they are in the wrong order
            j--;  // After swapping, j is decremented to continue comparing the newly swapped element with previous elements,
                  // ensuring that the correct position in the sorted portion is found.
        }
    }
    return array;  // Return the sorted array
}

function swap(i, j, array) {
    // Function to swap two elements in the array
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

// Example usage with dummy data
let array = [5, 2, 9, 1, 5, 6];  // Unsorted array
let sortedArray = insertionSort(array);  // Perform insertion sort
console.log(sortedArray);  // Expected output: [1, 2, 5, 5, 6, 9]
