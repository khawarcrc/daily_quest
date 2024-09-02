function twoNumberSum(array, targetSum) {
    // Step 1: Sort the input array in ascending order.
    array.sort((a, b) => a - b);
    
    // Step 2: Initialize two pointers. 
    // 'left' starts at the beginning of the array.
    // 'right' starts at the end of the array.
    let left = 0;
    let right = array.length - 1;
        
    // Step 3: Loop while 'left' pointer is less than 'right' pointer.
    while (left < right) {
        // Calculate the current sum of the values at the two pointers.
        const currentSum = array[left] + array[right];
        
        // Step 4: Check if the current sum is equal to the target sum.
        if (currentSum === targetSum) {
            // If it is, return the pair of numbers.
            return [array[left], array[right]];
        // Step 5: If the current sum is less than the target sum,
        // move the 'left' pointer to the right to increase the sum.
        } else if (currentSum < targetSum) {
            left += 1;
        // Step 6: If the current sum is greater than the target sum,
        // move the 'right' pointer to the left to decrease the sum.
        } else if (currentSum > targetSum) {
            right -= 1;
        }
    }
    
    // Step 7: If no pair is found that sums to the target sum,
    // return an empty array.
    return [];
}

// Example of calling the function with input
const array = [3, 5, -4, 8, 11, 1, -1, 6];
const targetSum = 10;

// Calling the function and printing the result
const result = twoNumberSum(array, targetSum);
console.log(result);  // Output should be [11, -1] or [-1, 11] (order doesn't matter)
