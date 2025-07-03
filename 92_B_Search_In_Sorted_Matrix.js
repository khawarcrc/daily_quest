function searchInSortedMatrix(matrix, target) {
    // Start at the top-right corner of the matrix
    let row = 0;  // Initialize the row index to the first row
    let col = matrix[0].length - 1;  // Initialize the col index to the last column

    // Traverse the matrix while within the valid bounds
    while (row < matrix.length && col >= 0) {
        // If the current element is greater than the target, move left
        if (matrix[row][col] > target) {
            col--;  // Move one column to the left
        } 
        // If the current element is less than the target, move down
        else if (matrix[row][col] < target) {
            row++;  // Move one row down
        }
        // If the current element is equal to the target, return its position
        else {
            return [row, col];  // Target found at this row and column
        }
    }

    // If the loop ends, the target is not in the matrix
    return [-1, -1];  // Target not found
}

// Dummy Data
const matrix = [
    [1,  4,  7, 11],     // Row 0
    [2,  5,  8, 12],     // Row 1
    [3,  6,  9, 16],     // Row 2
    [10, 13, 14, 17]     // Row 3
];

const target = 6;  // The number we want to find in the matrix

// Function Call
const result = searchInSortedMatrix(matrix, target);  // Call the function and store the result

// Output
console.log(`Target ${target} found at position: [${result}]`);  // Expected output: [2, 1]