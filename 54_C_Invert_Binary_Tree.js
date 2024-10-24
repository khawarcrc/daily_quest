// Binary Tree Node class
class BinaryTreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Function to invert the binary tree using BFS
function invertBinaryTree(tree) {
    // Initialize the queue with the root node
    const queue = [tree];

    // Continue while there are nodes in the queue
    while (queue.length > 0) {
        // Pop the first node in the queue
        const current = queue.shift();

        // If the current node is null, skip to the next iteration
        if (current === null) continue;

        // Swap the left and right children of the current node
        swapLeftAndRight(current);

        // Append the left and right children (if they exist) to the queue
        if (current.left !== null) queue.push(current.left);
        if (current.right !== null) queue.push(current.right);
    }
}

// Function to swap the left and right child of a node
function swapLeftAndRight(tree) {
    [tree.left, tree.right] = [tree.right, tree.left];
}

// Function to print the binary tree in level-order
function printLevelOrder(tree) {
    if (tree === null) return;

    // Use a queue for level-order traversal
    const queue = [tree];

    while (queue.length > 0) {
        const current = queue.shift();
        // Print the current node's value
        process.stdout.write(`${current.value} `);

        // Append the left and right children to the queue if they exist
        if (current.left !== null) queue.push(current.left);
        if (current.right !== null) queue.push(current.right);
    }
}

// Dummy Data (Sample Binary Tree)
//         1
//       /   \
//      2     3
//     / \   / \
//    4   5 6   7

const root = new BinaryTreeNode(1);
root.left = new BinaryTreeNode(2);
root.right = new BinaryTreeNode(3);
root.left.left = new BinaryTreeNode(4);
root.left.right = new BinaryTreeNode(5);
root.right.left = new BinaryTreeNode(6);
root.right.right = new BinaryTreeNode(7);

// Print original binary tree (before inversion)
console.log("Original Binary Tree (Level-Order):");
printLevelOrder(root);
console.log("\n");

// Invert the binary tree
invertBinaryTree(root);

// Print the inverted binary tree (after inversion)
console.log("Inverted Binary Tree (Level-Order):");
printLevelOrder(root);

// Expected Inverted Binary Tree:
//         1
//       /   \
//      3     2
//     / \   / \
//    7   6 5   4
