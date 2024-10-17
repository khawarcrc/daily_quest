class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Function to validate if a given binary tree is a binary search tree (BST)
function validateBst(tree) {
    // Start the recursive check from the root of the tree
    // The tree must follow the condition: minValue < node.value < maxValue
    return validateBstHelper(tree, -Infinity, Infinity);
}

// Recursive helper function to validate the BST
function validateBstHelper(tree, minValue, maxValue) {
    // Base case: if we reach a leaf node (null), it's valid by default
    if (tree === null) {
        return true;
    }

    // Check if the current node's value violates the BST property
    // Node's value must be strictly greater than minValue and less than maxValue
    if (tree.value <= minValue || tree.value >= maxValue) {
        return false;
    }

    // Recursively validate the left subtree (all values should be < current node's value)
    const leftIsValid = validateBstHelper(tree.left, minValue, tree.value);

    // Recursively validate the right subtree (all values should be > current node's value)
    return leftIsValid && validateBstHelper(tree.right, tree.value, maxValue);
}

// Dummy data to test the function
// Constructing a valid BST:
//        10
//       /  \
//      5   15
//     / \   \
//    2   5  22

const bst = new BST(10);
bst.left = new BST(5);
bst.right = new BST(15);
bst.left.left = new BST(2);
bst.left.right = new BST(5);
bst.right.right = new BST(22);

// Test the function
console.log(validateBst(bst));  // Output should be true since it's a valid BST