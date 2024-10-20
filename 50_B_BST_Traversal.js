// Define the structure for a node in the binary tree
class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Function to perform in-order traversal (Left, Root, Right)
// in-order traversal (left → root → right)
function inOrderTraverse(tree, array) {
    // Base case: if the current node is null (leaf node's child)
    if (tree !== null) {
        // Recursively traverse the left subtree
        inOrderTraverse(tree.left, array);
        // Visit the root node and append its value to the array
        array.push(tree.value);
        // Recursively traverse the right subtree
        inOrderTraverse(tree.right, array);
    }
    return array;
}

// Function to perform pre-order traversal (Root, Left, Right)
function preOrderTraverse(tree, array) {
    // Base case: if the current node is null (leaf node's child)
    if (tree !== null) {
        // Visit the root node and append its value to the array
        array.push(tree.value);
        // Recursively traverse the left subtree
        preOrderTraverse(tree.left, array);
        // Recursively traverse the right subtree
        preOrderTraverse(tree.right, array);
    }
    return array;
}

// Function to perform post-order traversal (Left, Right, Root)
function postOrderTraverse(tree, array) {
    // Base case: if the current node is null (leaf node's child)
    if (tree !== null) {
        // Recursively traverse the left subtree
        postOrderTraverse(tree.left, array);
        // Recursively traverse the right subtree
        postOrderTraverse(tree.right, array);
        // Visit the root node and append its value to the array
        array.push(tree.value);
    }
    return array;
}

// Create dummy data (binary tree)
const root = new TreeNode(5);  // Root node
root.left = new TreeNode(3);   // Left child of root
root.right = new TreeNode(7);  // Right child of root
root.left.left = new TreeNode(2);   // Left child of 3
root.left.right = new TreeNode(4);  // Right child of 3
root.right.right = new TreeNode(8); // Right child of 7

// Perform the traversals
const inOrderResult = inOrderTraverse(root, []);   // In-order traversal result
const preOrderResult = preOrderTraverse(root, []); // Pre-order traversal result
const postOrderResult = postOrderTraverse(root, []); // Post-order traversal result

// Output the results
console.log("In-order Traversal:", inOrderResult);
console.log("Pre-order Traversal:", preOrderResult);
console.log("Post-order Traversal:", postOrderResult);
