function levenshteinDistance(str1, str2) {
    // Initialize a 2D array to store edit distances
    const edits = Array.from(Array(str2.length + 1), () => Array(str1.length + 1).fill(0));

    // Fill the first row and first column with incremental values
    for (let i = 0; i <= str2.length; i++) edits[i][0] = i;
    for (let j = 0; j <= str1.length; j++) edits[0][j] = j;

    console.log("Initial edits matrix:");
    console.table(edits);  // Display initial matrix

    // Compute the edit distance for each cell in the array
    for (let i = 1; i <= str2.length; i++) {
        for (let j = 1; j <= str1.length; j++) {
            if (str2[i - 1] === str1[j - 1]) {
                // If characters are the same, no additional cost
                edits[i][j] = edits[i - 1][j - 1];
            } else {
                // Minimum of substitution, deletion, or insertion
                edits[i][j] = 1 + Math.min(
                    edits[i - 1][j - 1],  // substitution
                    edits[i - 1][j],      // deletion
                    edits[i][j - 1]       // insertion
                );
            }
            console.log(`After processing cell [${i}][${j}], matrix is:`);
            console.table(edits);  // Display matrix after each cell is processed
        }
    }

    // The minimum edit distance is found in the last cell
    console.log("Final edits matrix:");
    console.table(edits);  // Display final matrix

    return edits[str2.length][str1.length];
}

// Dummy data for testing the function
const str1 = "kitten";
const str2 = "sitting";
console.log(`The Levenshtein distance between '${str1}' and '${str2}' is: ${levenshteinDistance(str1, str2)}`);
