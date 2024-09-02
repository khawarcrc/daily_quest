function sortedSquaredArray(array) {
    // Create a new array filled with zeros, same length as the input array
    const sortedSquares = new Array(array.length).fill(0);
    
    // Initialize two pointers: one at the start and one at the end of the array
    let smallerValueIdx = 0;
    let largerValueIdx = array.length - 1;
    
    console.log("Initial array:", array);
    console.log("Starting process to create sorted squares array...");

    // Iterate through the array in reverse order
    for (let idx = array.length - 1; idx >= 0; idx--) {
        // Get the current values at the pointers
        const smallerValue = array[smallerValueIdx];
        const largerValue = array[largerValueIdx];
        
        console.log(`\nIteration ${array.length - idx}:`);
        console.log(`Comparing absolute values | Smaller: ${Math.abs(smallerValue)} | Larger: ${Math.abs(largerValue)}`);
        
        // Compare the absolute values of the current elements
        if (Math.abs(smallerValue) > Math.abs(largerValue)) {
            // If the smaller value has a larger absolute value, square it and place it at the current index
            sortedSquares[idx] = smallerValue * smallerValue;
            console.log(`Placing ${sortedSquares[idx]} at index ${idx}`);
            // Move the smallerValueIdx pointer to the right
            smallerValueIdx++;
            console.log(`Moving smallerValueIdx to ${smallerValueIdx}`);
        } else {
            // If the larger value has a larger absolute value, square it and place it at the current index
            sortedSquares[idx] = largerValue * largerValue;
            console.log(`Placing ${sortedSquares[idx]} at index ${idx}`);
            // Move the largerValueIdx pointer to the left
            largerValueIdx--;
            console.log(`Moving largerValueIdx to ${largerValueIdx}`);
        }
    }
    
    // Log the final sorted array of squared values
    console.log("\nFinal sorted squares array:", sortedSquares);
    
    // Return the sorted array of squared values
    return sortedSquares;
}

// Test the function with an example array
const array = [-7, -3, 1, 9, 12];
const result = sortedSquaredArray(array);
console.log("Result:", result);  // Output should be [1, 9, 49, 81, 144]

// function sortedSquaredArray(array) {
//     // Create a new array filled with zeros, same length as the input array
//     const sortedSquares = new Array(array.length).fill(0);
    
//     // Initialize two pointers: one at the start and one at the end of the array
//     let smallerValueIdx = 0;
//     let largerValueIdx = array.length - 1;
    
//     // Iterate through the array in reverse order
//     for (let idx = array.length - 1; idx >= 0; idx--) {
//         // Get the current values at the pointers
//         const smallerValue = array[smallerValueIdx];
//         const largerValue = array[largerValueIdx];
        
//         // Compare the absolute values of the current elements
//         if (Math.abs(smallerValue) > Math.abs(largerValue)) {
//             // If the smaller value has a larger absolute value, square it and place it at the current index
//             sortedSquares[idx] = smallerValue * smallerValue;
//             // Move the smallerValueIdx pointer to the right
//             smallerValueIdx++;
//         } else {
//             // If the larger value has a larger absolute value, square it and place it at the current index
//             sortedSquares[idx] = largerValue * largerValue;
//             // Move the largerValueIdx pointer to the left
//             largerValueIdx--;
//         }
//     }
    
//     // Return the sorted array of squared values
//     return sortedSquares;
// }

// // Test the function with an example array
// const array = [-7, -3, 1, 9, 12];
// const result = sortedSquaredArray(array);
// console.log(result);  // Output should be [1, 9, 49, 81, 144]



// # 1. Initialize the Result Array:
// #    a. A new array of the same length as the input is created to store the squared values.

// # 2. Set Up Pointers:
// #    a. Two pointers are set, one at the beginning and one at the end of the array.

// # 3. Iterate in Reverse:
// #    a. The array is traversed in reverse order to place the largest squared values at the end of the result array.

// # 4. Retrieve Pointer Values:
// #    a. In each iteration, the current values at the two pointers are retrieved.

// # 5. Compare Absolute Values:
// #    a. The absolute values of the current elements are compared.

// # 6. Square and Place the Larger Value:
// #    a. The larger of the squared values is placed at the current index in the result array.

// # 7. Move the Pointer:
// #    a. Depending on which value was larger, the corresponding pointer is adjusted (moved inward).

// # 8. Return the Result:
// #    a. After the loop finishes, the result array containing the sorted squared values is returned.
