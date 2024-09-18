function binarySearch(array, target) {
    // Start the binary search by calling the helper function
    return binarySearchHelper(array, target, 0, array.length - 1);
}

function binarySearchHelper(array, target, left, right) {
    // Loop continues as long as the search space is valid (left <= right)
    while (left <= right) {
        // Calculate the middle index
        const middle = Math.floor((left + right) / 2);
        
        // Get the value at the middle index
        const potentialMatch = array[middle];
        
        // Check if the middle element is the target
        if (target === potentialMatch) {
            // If yes, return the middle index (target found)
            return middle;
        }
        // If the target is smaller than the middle element, discard the right half
        else if (target < potentialMatch) {
            right = middle - 1;
        }
        // If the target is greater than the middle element, discard the left half
        else {
            left = middle + 1;
        }
    }
    
    // If target is not found, return -1
    return "target not found";
}

// Dummy data for testing
// Example sorted array: [1, 3, 5, 7, 9, 11, 13, 15]
// Target to find: 9
console.log(binarySearch([1, 3, 5, 7, 9, 11, 13, 15], 9));  // Expected output: 4

// Example where the target is not found
// Target to find: 4
console.log(binarySearch([1, 3, 5, 7, 9, 11, 13, 15], 4));  // Expected output: -1
