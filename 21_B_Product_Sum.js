// Problem Statement:
// Write a function `productSum` that takes a special array and computes its product sum.
// A special array can contain either integers or other arrays.
// The product sum is calculated by summing up the elements of the array and multiplying by a multiplier
// based on the depth (nested level) of the arrays.
// The multiplier starts at 1 for the outer array and increases by 1 for each inner array.

// Steps to solve:
// 1. Initialize a variable `sum` to 0 to hold the cumulative sum of the array.
// 2. Loop through each element in the array.
// 3. If the element is a array, recursively call `productSum` on that array, increasing the multiplier by 1.
// 4. If the element is a number, add it to the sum.
// 5. After iterating through all elements, multiply the `sum` by the current multiplier.
// 6. Return the final product sum.

function productSum(array, multiplier = 1) {
    // Initialize sum to 0 for the current level
    let sum = 0;
    // Iterate over each element in the array
    for (let element of array) {
        // If the element is an array, recursively calculate the product sum
        if (Array.isArray(element)) {
            sum += productSum(element, multiplier + 1);
        } else {
            // If the element is an integer, add it to the sum
            sum += element;
        }
    }
    // Return the total sum multiplied by the current multiplier (based on depth level)
    return sum * multiplier;
}

// Dummy data for testing
// Example array: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
// The depth levels for each element are:
// 1. Elements at depth 1: 5, 2, 3
// 2. Elements at depth 2: [7, -1], [6, [-13, 8], 4]
// 3. Elements at depth 3: [-13, 8]


// Call the function with the dummy data
console.log(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]));
// Expected output: 12
