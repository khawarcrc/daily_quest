function spiralTraverse(array) {
    // Initialize an empty array to store the result
    const result = [];

    // Define the starting and ending boundaries for rows and columns
    let startRow = 0;
    let endRow = array.length - 1;
    let startCol = 0;
    let endCol = array[0].length - 1;

    // Continue looping as long as the boundaries have not crossed
    while (startRow <= endRow && startCol <= endCol) {
        // Traverse the top row from left to right
        for (let col = startCol; col <= endCol; col++) {
            result.push(array[startRow][col]);
        }

        // Traverse the right column from top to bottom
        for (let row = startRow + 1; row <= endRow; row++) {
            result.push(array[row][endCol]);
        }

        // Traverse the bottom row from right to left (if there are remaining rows)
        if (startRow < endRow) {
            for (let col = endCol - 1; col >= startCol; col--) {
                result.push(array[endRow][col]);
            }
        }

        // Traverse the left column from bottom to top (if there are remaining columns)
        if (startCol < endCol) {
            for (let row = endRow - 1; row > startRow; row--) {
                result.push(array[row][startCol]);
            }
        }

        // Move the boundaries inward for the next layer
        startRow++;
        endRow--;
        startCol++;
        endCol--;
    }

    return result;
}

// Dummy data (4x4 matrix)
const array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
];

// Call the function with the dummy data
console.log(spiralTraverse(array)); 
// Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
