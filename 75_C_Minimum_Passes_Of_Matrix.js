function minimumPassesOfMatrix(matrix) {
    /**
     * Controls the process and returns the final number of passes required.
     * - If negative values remain after processing, returns -1.
     */
    const passes = convertNegatives(matrix); // Transform negative values into positives
    // Check if any negative value remains. If yes, return -1; else, return the passes count.
    return containsNegative(matrix) ? -1 : passes - 1;
}

function convertNegatives(matrix) {
    /**
     * Performs a BFS to convert negative values into positive values.
     * Uses a single queue to track cells to be processed.
     */
    let queue = getAllPositivePositions(matrix); // Initialize queue with all positive positions
    let passes = 0; // Initialize pass count

    // Continue processing until no more cells to process
    while (queue.length > 0) {
        let currentSize = queue.length; // Number of cells to process in the current pass
        let madeProgress = false; // Track if any changes are made during this pass

        while (currentSize > 0) {
            const [currentRow, currentCol] = queue.shift(); // Dequeue the next cell
            // Get all valid adjacent positions
            const adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix);
            for (const [row, col] of adjacentPositions) {
                const value = matrix[row][col];
                if (value < 0) {
                    // Convert negative to positive and enqueue the position
                    matrix[row][col] *= -1;
                    queue.push([row, col]);
                    madeProgress = true;
                }
            }
            currentSize--; // Decrement the count of cells to process in this pass
        }

        if (madeProgress) {
            passes++; // Increment the pass count if changes occurred
        }
    }

    return passes;
}

function getAllPositivePositions(matrix) {
    /**
     * Identifies all initial positive cell positions in the matrix.
     * Returns a list of coordinates of positive cells.
     */
    const positivePositions = [];
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            const value = matrix[row][col];
            if (value > 0) {
                positivePositions.push([row, col]); // Add position to the list if value is positive
            }
        }
    }
    return positivePositions;
}

function getAdjacentPositions(row, col, matrix) {
    /**
     * Returns a list of valid adjacent cell positions for the given cell.
     */
    const adjacentPositions = [];
    if (row > 0) {
        adjacentPositions.push([row - 1, col]); // Top neighbor
    }
    if (row < matrix.length - 1) {
        adjacentPositions.push([row + 1, col]); // Bottom neighbor
    }
    if (col > 0) {
        adjacentPositions.push([row, col - 1]); // Left neighbor
    }
    if (col < matrix[0].length - 1) {
        adjacentPositions.push([row, col + 1]); // Right neighbor
    }
    return adjacentPositions;
}

function containsNegative(matrix) {
    /**
     * Checks if the matrix still contains any negative values.
     * Returns true if any negative value exists, otherwise false.
     */
    for (const row of matrix) {
        for (const value of row) {
            if (value < 0) {
                return true; // Found a negative value
            }
        }
    }
    return false;
}

// Dummy Data for Testing
const matrix = [
    [0, -1, -3, 2, 0], // Example matrix with positives, negatives, and zeros
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
];

// Test the function with the dummy matrix
const result = minimumPassesOfMatrix(matrix);
console.log(`Minimum passes required: ${result}`); // Expected Output: 4
