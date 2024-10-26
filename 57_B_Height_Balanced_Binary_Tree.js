class BinaryTree {
    constructor(value, left = null, right = null) {
        // Initializes a node in the binary tree with a value and optional left and right child nodes
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

class TreeInfo {
    constructor(isBalanced, height) {
        // Stores information about whether a subtree is balanced and its height
        this.isBalanced = isBalanced;
        this.height = height;
    }
}

function heightBalancedBinaryTree(tree) {
    // Get information about the entire tree's balance status and height
    const treeInfo = getTreeInfo(tree);
    console.log(`Tree is balanced: ${treeInfo.isBalanced}`);
    return treeInfo.isBalanced;
}

function getTreeInfo(node) {
    // Base case: if the node is null, return true for balance and -1 for height (leaf level)
    if (node === null) {
        console.log("Reached a leaf node, returning true and height -1");
        return new TreeInfo(true, -1);
    }

    // Recursively get information about the left subtree
    const leftSubTreeInfo = getTreeInfo(node.left);
    console.log(`Node ${node.value} - Left subtree info: isBalanced=${leftSubTreeInfo.isBalanced}, height=${leftSubTreeInfo.height}`);

    // Recursively get information about the right subtree
    const rightSubTreeInfo = getTreeInfo(node.right);
    console.log(`Node ${node.value} - Right subtree info: isBalanced=${rightSubTreeInfo.isBalanced}, height=${rightSubTreeInfo.height}`);

    // Check if the current node's subtree is balanced
    const isBalanced = (
        leftSubTreeInfo.isBalanced &&
        rightSubTreeInfo.isBalanced &&
        Math.abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    );

    // Calculate the height of the current node's subtree
    const height = Math.max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1;

    console.log(`Node ${node.value} - isBalanced=${isBalanced}, height=${height}`);
    return new TreeInfo(isBalanced, height);
}

// Dummy data - creating a balanced binary tree
const root = new BinaryTree(1);
root.left = new BinaryTree(2);
root.right = new BinaryTree(3);
root.left.left = new BinaryTree(4);
root.left.right = new BinaryTree(5);
root.right.left = new BinaryTree(6);
root.right.right = new BinaryTree(7);

// Calling the function to check if the tree is balanced
console.log("Is the binary tree height-balanced?", heightBalancedBinaryTree(root));
