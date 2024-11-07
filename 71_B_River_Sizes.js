// Problem Statement:
// Write a function that takes in a two-dimensional array (matrix) of potentially varying sizes.
// Each element in the matrix represents a node in a graph and is either a 0 or a 1. 
// A "river" is a group of 1s connected horizontally or vertically (not diagonally).
// The function should return an array of the sizes of all rivers represented in the input matrix.

function riverSizes(matrix) {
    const sizes = [];  // Store the sizes of each river
    const visited = matrix.map(row => row.map(() => false));  // Track visited nodes

    // Traverse each cell in the matrix
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            // Skip if the node is already visited
            if (visited[i][j]) continue;
            // Calculate river size if a new river is found
            traverseNode(i, j, matrix, visited, sizes);
        }
    }
    return sizes;
}

function traverseNode(i, j, matrix, visited, sizes) {
    let currentRiverSize = 0;  // Initialize river size counter
    const nodesToExplore = [[i, j]];  // Stack to explore nodes for current river

    while (nodesToExplore.length) {
        const currentNode = nodesToExplore.pop();  // Get the current node
        const [i, j] = currentNode;

        // Skip if already visited
        if (visited[i][j]) continue;
        visited[i][j] = true;  // Mark node as visited

        // Skip if current node is 0 (not part of a river)
        if (matrix[i][j] === 0) continue;
        currentRiverSize += 1;  // Increment the size of the current river

        // Get unvisited neighbors and add them to the stack
        const unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited);
        for (const neighbor of unvisitedNeighbors) {
            nodesToExplore.push(neighbor);
        }
    }

    // Append the river size if a river was found
    if (currentRiverSize > 0) sizes.push(currentRiverSize);
}

function getUnvisitedNeighbors(i, j, matrix, visited) {
    const unvisitedNeighbors = [];  // List to store unvisited neighbors

    // Check each possible direction (up, down, left, right)
    if (i > 0 && !visited[i - 1][j]) unvisitedNeighbors.push([i - 1, j]);  // Up
    if (i < matrix.length - 1 && !visited[i + 1][j]) unvisitedNeighbors.push([i + 1, j]);  // Down
    if (j > 0 && !visited[i][j - 1]) unvisitedNeighbors.push([i, j - 1]);  // Left
    if (j < matrix[0].length - 1 && !visited[i][j + 1]) unvisitedNeighbors.push([i, j + 1]);  // Right

    return unvisitedNeighbors;
}

// Dummy data for testing
const matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
];

// Example usage
console.log(riverSizes(matrix));  // Expected output: Sizes of rivers, e.g., [2, 1, 5, 2]
