function levenshteinDistance(str1, str2) {
    // Initialize a 2D array to store edit distances.
    // The dimensions of the array are (str2.length + 1) x (str1.length + 1) to account for empty string comparisons.
    const edits = Array.from(Array(str2.length + 1), () => Array(str1.length + 1).fill(0));

    // Fill the first row and first column with incremental values.
    // This represents the cost of transforming an empty string into the first n characters of str1 or str2.
    for (let i = 0; i <= str2.length; i++) edits[i][0] = i; // Cost of deletions
    for (let j = 0; j <= str1.length; j++) edits[0][j] = j; // Cost of insertions

    console.log("Initial edits matrix:");
    console.table(edits);  // Display initial matrix for visualization

    // Compute the edit distance for each cell in the array.
    for (let i = 1; i <= str2.length; i++) {
        for (let j = 1; j <= str1.length; j++) {
            if (str2[i - 1] === str1[j - 1]) {
                // If characters are the same, no additional cost to transform.
                edits[i][j] = edits[i - 1][j - 1];
            } else {
                // Calculate the minimum cost among substitution, deletion, and insertion.
                edits[i][j] = 1 + Math.min(
                    edits[i - 1][j - 1],  // Cost of substitution
                    edits[i - 1][j],      // Cost of deletion
                    edits[i][j - 1]       // Cost of insertion
                );
            }
            console.log(`After processing cell [${i}][${j}], matrix is:`); // Log after processing each cell
            console.table(edits);  // Display matrix after each cell is processed for tracing
        }
    }

    // The minimum edit distance is found in the last cell of the matrix.
    console.log("Final edits matrix:");
    console.table(edits);  // Display final matrix for final review

    return edits[str2.length][str1.length]; // Return the computed Levenshtein distance
}

// Dummy data for testing the function
const str1 = "kitten";   // First string
const str2 = "sitting";  // Second string
// Log the result of the Levenshtein distance calculation
console.log(`The Levenshtein distance between '${str1}' and '${str2}' is: ${levenshteinDistance(str1, str2)}`);
