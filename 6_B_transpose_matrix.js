// Function transposeMatrix(matrix):
//
// Purpose: Transposes the given 2D matrix (i.e., converts rows to columns and vice versa).
//
// Steps:
// 1. Initialize an empty array to store the transposed matrix.
// 2. Loop through each column index of the original matrix to create new rows for the transposed matrix.
// 3. For each column, create a new row by extracting elements from each row of the original matrix.
// 4. Add the new row to the transposed matrix.
// 5. Return the transposed matrix.
//
// Example Usage:
// 1. Define a sample matrix.
// 2. Print the original matrix.
// 3. Call transposeMatrix to get the transposed matrix.
// 4. Print the transposed matrix.

function transposeMatrix(matrix) {
  // Initialize an empty array to store the transposed matrix
  let transposeMatrix = [];

  // Iterate over each column index in the matrix
  for (let col = 0; col < matrix[0].length; col++) {
    // Initialize a new row for the transposed matrix
    let newRow = [];
    console.log(`\nProcessing column ${col + 1}:`);

    // Iterate over each row index in the matrix
    for (let row = 0; row < matrix.length; row++) {
      // Append the element at the current row and column to the new row
      console.log(
        `  Taking element from row ${row + 1}, column ${col + 1}: ${
          matrix[row][col]
        }`
      );
      newRow.push(matrix[row][col]);
    }

    // Append the newly formed row to the transposed matrix
    console.log(`  Formed new row: ${newRow}`);
    transposeMatrix.push(newRow);
  }

  // Return the transposed matrix
  return transposeMatrix;
}

// Define a sample matrix to transpose
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

// Print the original matrix
console.log("Original Matrix:");
matrix.forEach((row) => console.log(row));
// matrix length
console.log("matrix length", matrix.length);

// Execute the transposeMatrix function and store the result
let transposed = transposeMatrix(matrix);

// Print the transposed matrix
console.log("\nTransposed Matrix:");
transposed.forEach((row) => console.log(row));
