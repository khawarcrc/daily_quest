function kadanesAlgorithm(array) {
    // Initialize maxCurrent and maxGlobal with the first element
    let maxCurrent = array[0];
    let maxGlobal = array[0];
    
    console.log("Initial maxCurrent:", maxCurrent);
    console.log("Initial maxGlobal:", maxGlobal);

    // Iterate through the array starting from the second element
    for (let i = 1; i < array.length; i++) {
        const num = array[i];
        
        // Update maxCurrent to be the maximum of the current element
        // or the sum of maxCurrent and the current element
        maxCurrent = Math.max(num, maxCurrent + num);
        
        console.log(`Element at index ${i}:`, num);
        console.log("Updated maxCurrent:", maxCurrent);

        // Update maxGlobal if maxCurrent is greater
        if (maxCurrent > maxGlobal) {
            maxGlobal = maxCurrent;
            console.log("Updated maxGlobal:", maxGlobal);
        }
    }

    return maxGlobal;
}

// Example usage with dummy data
const array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]; // Example array
console.log("Maximum Sum of Contiguous Subarray:", kadanesAlgorithm(array));
