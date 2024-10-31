function numberOfWaysToTraverseGraph(width, height) {
    // Initialize a 2D array with dimensions (height + 1) x (width + 1) to store
    // the number of ways to reach each cell in the grid.
    // Each element is initially set to 0.
    const numberOfWays = Array.from({ length: height + 1 }, () => Array(width + 1).fill(0));
    
    // Iterate through each cell in the grid starting from (1, 1) to (width, height)
    for (let widthIdx = 1; widthIdx <= width; widthIdx++) {
        for (let heightIdx = 1; heightIdx <= height; heightIdx++) {
            // Set the base cases: if we're in the first row (heightIdx === 1) 
            // or the first column (widthIdx === 1), there's only 1 way to reach each cell.
            if (widthIdx === 1 || heightIdx === 1) {
                numberOfWays[heightIdx][widthIdx] = 1; // Only one way to reach any cell in the first row or column
            } else {
                // Calculate the number of ways to reach the current cell by summing
                // the ways from the left cell (waysLeft) and the top cell (waysUp).
                const waysLeft = numberOfWays[heightIdx][widthIdx - 1]; // Ways to reach from the left cell
                const waysUp = numberOfWays[heightIdx - 1][widthIdx];   // Ways to reach from the top cell
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp;  // Total ways to reach the current cell
            }

            // Log the current number of ways to reach the cell (widthIdx, heightIdx)
            console.log(`Ways to reach (${widthIdx}, ${heightIdx}): ${numberOfWays[heightIdx][widthIdx]}`);
            // Display the entire numberOfWays array as a table for better visualization
            console.table(numberOfWays);
        }
    }

    // Log the final result: the number of ways to reach the bottom-right corner of the grid
    console.log(`Final number of ways to reach (${width}, ${height}): ${numberOfWays[height][width]}`);
    return numberOfWays[height][width]; // Return the total number of ways to traverse the grid
}

// Dummy data for testing: width and height of a 3x3 grid
const width = 3;
const height = 3;
// Log the total ways to traverse the specified grid
console.log(`Total ways to traverse a ${width}x${height} grid: ${numberOfWaysToTraverseGraph(width, height)}`);  // Expected output: 6
