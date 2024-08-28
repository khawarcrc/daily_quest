// 1. Define a BinaryTree class with value, left, and right properties.

// 2. Implement the nodeDepths function to calculate the sum of all node depths in a binary tree.

// 3. Inside nodeDepths, define a helper function (calculateDepths) that:
//    - Takes a node and its depth as parameters.
//    - If the node is null, returns 0 (base case).
//    - Logs the current node and its depth for tracing.
//    - Recursively computes the sum of depths for left and right children.
//    - Logs the accumulated depths from children.
//    - Returns the current node's depth plus the depths from left and right children.

// 4. Call calculateDepths starting from the root node with an initial depth of 0.

// 5. Create a binary tree structure for testing.

// 6. Calculate and log the sum of all node depths using the nodeDepths function.

class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function nodeDepths(root) {
    // Helper function to calculate depths recursively
    function calculateDepths(node, depth) {
        if (node === null) {
            return 0;
        }
        // Log current node and its depth
        console.log(`Visiting node with value ${node.value} at depth ${depth}`);
        
        // Calculate depths of left and right children and accumulate total depth
        const leftDepths = calculateDepths(node.left, depth + 1);
        const rightDepths = calculateDepths(node.right, depth + 1);
        
        // Log the accumulated depth from left and right children
        console.log(`Node with value ${node.value} has leftDepths ${leftDepths} and rightDepths ${rightDepths}`);
        
        // Return the current node's depth plus the accumulated depths
        return depth + leftDepths + rightDepths;
    }

    // Start the recursion with the root node at depth 0
    return calculateDepths(root, 0);
}

// Create a binary tree for testing
const root = new BinaryTree(1);
root.left = new BinaryTree(2);
root.right = new BinaryTree(3);
root.left.left = new BinaryTree(4);
root.left.right = new BinaryTree(5);
root.right.left = new BinaryTree(6);
root.right.right = new BinaryTree(7);

// Calculate the sum of node depths
const sumDepths = nodeDepths(root);
console.log("Sum of all node depths:", sumDepths);
