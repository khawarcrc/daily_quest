class BinaryTree {
    constructor(value, left = null, right = null) {
        // Initialize the Binary Tree node with a value and optional left and right children
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

function findKthLargestValueInBst(tree, k) {
    // Initialize an array to store the sorted node values
    const sortedNodeValues = [];
    // Perform in-order traversal to get sorted node values
    inOrderTraverse(tree, sortedNodeValues);
    
    // Return the Kth largest value; subtract k to access from the end of the sorted list
    return sortedNodeValues[sortedNodeValues.length - k];
}

function inOrderTraverse(node, sortedNodeValues) {
    // Base case: if the node is null, return
    if (node === null) {
        return;
    }

    // Traverse the left subtree
    inOrderTraverse(node.left, sortedNodeValues);
    
    // Append the current node's value to the sorted array
    sortedNodeValues.push(node.value);
    
    // Traverse the right subtree
    inOrderTraverse(node.right, sortedNodeValues);
}

// Dummy data to create a sample BST
// Example BST:
//         10
//        /  \
//       5   15
//      / \    \
//     2   5   20

const root = new BinaryTree(10);
root.left = new BinaryTree(5);
root.right = new BinaryTree(15);
root.left.left = new BinaryTree(2);
root.left.right = new BinaryTree(5);
root.right.right = new BinaryTree(20);

// Specify the value of k to find the Kth largest value
const k = 2;

// Print the result
console.log(`The ${k}th largest value in the BST is: ${findKthLargestValueInBst(root, k)}`);

// To understand the execution, print the sorted node values
const sortedNodeValues = [];
inOrderTraverse(root, sortedNodeValues);
console.log("Sorted node values:", sortedNodeValues);
