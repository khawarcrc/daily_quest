function zeroSumSubarray(nums) {
    // Initialize a set to keep track of the cumulative sums encountered so far, starting with 0
    const sums = new Set([0]);
    // Initialize the current cumulative sum
    let currentSum = 0;
    
    // Iterate through each number in the input list
    for (let num of nums) {
        // Update the current cumulative sum by adding the current number
        currentSum += num;
        
        // Check if the current cumulative sum has been seen before
        if (sums.has(currentSum)) {
            // If yes, a subarray with a sum of zero exists
            return true;
        }
        
        // Add the current cumulative sum to the set for future reference
        sums.add(currentSum);
    }
    
    // If no zero-sum subarray is found, return false
    return false;
}

// Dummy data for testing
const test_nums = [4, 2, -2, 3, 1];  // This array contains a zero-sum subarray [2, -2]
console.log(zeroSumSubarray(test_nums));  // Output: true
