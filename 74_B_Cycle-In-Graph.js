/**
 * Determines if a directed graph contains a cycle.
 *
 * @param {number[][]} edges - An adjacency list where each index represents a node, and the list at that index represents the nodes it points to.
 * @returns {boolean} - True if the graph contains a cycle, otherwise False.
 */
function cycleInGraph(edges) {
    // Number of nodes in the graph
    const numberOfNodes = edges.length;

    // Arrays to track visited nodes and nodes currently in the recursion stack
    const visited = new Array(numberOfNodes).fill(false);
    const currentlyInStack = new Array(numberOfNodes).fill(false);

    // Iterate through each node in the graph
    for (let node = 0; node < numberOfNodes; node++) {
        // Skip the node if it has already been visited
        if (visited[node]) continue;

        // Check for a cycle starting from the current node
        const containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack);
        if (containsCycle) return true;
    }

    // No cycle was detected
    return false;
}

/**
 * Helper function to determine if there is a cycle starting from a given node.
 *
 * @param {number} node - The current node.
 * @param {number[][]} edges - The adjacency list of the graph.
 * @param {boolean[]} visited - Tracks nodes that have been fully explored.
 * @param {boolean[]} currentlyInStack - Tracks nodes in the current recursion stack.
 * @returns {boolean} - True if a cycle is detected, otherwise False.
 */
function isNodeInCycle(node, edges, visited, currentlyInStack) {
    // Mark the current node as visited and add it to the stack
    visited[node] = true;
    currentlyInStack[node] = true;

    // Get all the neighbors of the current node
    const neighbors = edges[node];
    for (const neighbor of neighbors) {
        // If the neighbor hasn't been visited, visit it recursively
        if (!visited[neighbor]) {
            const containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack);
            if (containsCycle) return true;
        }
        // If the neighbor is already in the stack, a cycle is detected
        else if (currentlyInStack[neighbor]) {
            return true;
        }
    }

    // Remove the current node from the stack as the path exploration is complete
    currentlyInStack[node] = false;
    return false;
}

// Sample input data representing a directed graph using adjacency list format
// Each index represents a node, and the list at each index represents the nodes it points to
const edges = [
    [1, 2],    // Node 0 has edges to nodes 1 and 2
    [2],       // Node 1 has an edge to node 2
    [0, 3],    // Node 2 has edges to nodes 0 and 3, forming a cycle (0 -> 1 -> 2 -> 0)
    [4],       // Node 3 has an edge to node 4
    []         // Node 4 has no edges
];

// Test the function with the sample input
console.log(cycleInGraph(edges)); // Output should be true, as there is a cycle in the graph
