class BST {
    constructor(value) {
        // Initialize the BST with a root value, and left and right pointers
        this.value = value;
        this.left = null;
        this.right = null;
    }

    // Insert method to add a new node to the BST
    insert(value) {
        let currentNode = this; // Start at the root
        while (true) { // Loop to traverse the tree
            if (value < currentNode.value) { // If the new value is less, go to the left
                if (currentNode.left === null) { // If no left child, insert new node
                    currentNode.left = new BST(value);
                    break; // Exit after inserting
                } else {
                    currentNode = currentNode.left; // Move to the left node and continue
                }
            } else { // If the new value is greater or equal, go to the right
                if (currentNode.right === null) { // If no right child, insert new node
                    currentNode.right = new BST(value);
                    break; // Exit after inserting
                } else {
                    currentNode = currentNode.right; // Move to the right node and continue
                }
            }
        }
        return this; // Return the current tree for potential chaining
    }

    // Contains method to check if a value exists in the tree
    contains(value) {
        let currentNode = this; // Start at the root
        while (currentNode !== null) { // Traverse the tree until node is null
            if (value < currentNode.value) { // Move left if value is smaller
                currentNode = currentNode.left;
            } else if (value > currentNode.value) { // Move right if value is larger
                currentNode = currentNode.right;
            } else {
                return true; // Value found
            }
        }
        return false; // Value not found in the tree
    }

    // Remove method to delete a node with the specified value
    remove(value, parentNode = null) {
        let currentNode = this; // Start at the root
        while (currentNode !== null) { // Traverse the tree until node is null
            if (value < currentNode.value) { // Move left if the value is smaller
                parentNode = currentNode;
                currentNode = currentNode.left;
            } else if (value > currentNode.value) { // Move right if the value is larger
                parentNode = currentNode;
                currentNode = currentNode.right;
            } else { // Node to be removed is found
                if (currentNode.left !== null && currentNode.right !== null) {
                    // Case where the node has two children
                    currentNode.value = currentNode.right.getMinValue(); // Replace with min value from right subtree
                    currentNode.right.remove(currentNode.value, currentNode); // Recursively remove the node with the smallest value
                } else if (parentNode === null) {
                    // Special case: removing the root node
                    if (currentNode.left !== null) {
                        // Root has only left child, so we promote the left child
                        currentNode.value = currentNode.left.value;
                        currentNode.right = currentNode.left.right;
                        currentNode.left = currentNode.left.left;
                    } else if (currentNode.right !== null) {
                        // Root has only right child, so we promote the right child
                        currentNode.value = currentNode.right.value;
                        currentNode.left = currentNode.right.left;
                        currentNode.right = currentNode.right.right;
                    } else {
                        // Root has no children, tree becomes empty
                        // Do nothing, tree remains empty
                    }
                } else if (parentNode.left === currentNode) {
                    // Case: node to remove is the left child
                    parentNode.left = currentNode.left !== null ? currentNode.left : currentNode.right;
                } else if (parentNode.right === currentNode) {
                    // Case: node to remove is the right child
                    parentNode.right = currentNode.left !== null ? currentNode.left : currentNode.right;
                }
                break; // Exit after removal
            }
        }
        return this; // Return the modified tree
    }

    // Helper method to find the minimum value in the right subtree
    getMinValue() {
        let currentNode = this; // Start at the node from which we want to find the min value
        while (currentNode.left !== null) { // Keep moving to the left-most node
            currentNode = currentNode.left;
        }
        return currentNode.value; // Return the smallest value
    }
}

// Create a sample BST and insert values into it
const bst = new BST(10); // Root node with value 10
bst.insert(5); // Insert node with value 5
bst.insert(15); // Insert node with value 15
bst.insert(2); // Insert node with value 2
bst.insert(5); // Insert duplicate value 5
bst.insert(1); // Insert node with value 1
bst.insert(13); // Insert node with value 13
bst.insert(22); // Insert node with value 22
bst.insert(14); // Insert node with value 14

// Check if the tree contains certain values
console.log(bst.contains(15)); // Should return true
console.log(bst.contains(99)); // Should return false

// Remove a node from the BST
bst.remove(10); // Remove the root node (value 10)

// Check tree structure after removal
console.log(bst.contains(10)); // Should return false
