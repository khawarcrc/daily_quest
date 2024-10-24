class BST {
    // Constructor for each node of the BST
    constructor(value, left = null, right = null) {
        this.value = value; // Value of the node
        this.left = left;   // Left child of the node
        this.right = right; // Right child of the node
    }
}

class TreeInfo {
    // Class to keep track of the root index while reconstructing the tree
    constructor(rootIndex) {
        this.rootIndex = rootIndex; // Index of the root in the preorder traversal
    }
}

function reconstructBst(preOrderTraversalValues) {
    // Initializes the TreeInfo object and calls the recursive function to reconstruct the tree
    const treeInfo = new TreeInfo(0);
    return reconstructBstFromRange(
        -Infinity, // Lower bound for the first root (smallest possible value)
        Infinity,  // Upper bound for the first root (largest possible value)
        preOrderTraversalValues,
        treeInfo
    );
}

function reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo) {
    // Base case: If all elements from the preorder array are processed, return null
    if (currentSubtreeInfo.rootIndex === preOrderTraversalValues.length) {
        return null;
    }

    // Get the value of the current root
    const rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIndex];

    // If the value is out of the current bounds, return null (invalid subtree)
    if (rootValue <= lowerBound || rootValue >= upperBound) {
        return null;
    }

    // Move to the next root value in the preorder array
    currentSubtreeInfo.rootIndex++;

    // Recursively construct the left and right subtrees
    const leftSubtree = reconstructBstFromRange(
        lowerBound,    // Lower bound stays the same for left subtree
        rootValue,     // Upper bound for left subtree is the current root value
        preOrderTraversalValues,
        currentSubtreeInfo
    );

    const rightSubtree = reconstructBstFromRange(
        rootValue,     // Lower bound for the right subtree is the current root value
        upperBound,    // Upper bound stays the same for the right subtree
        preOrderTraversalValues,
        currentSubtreeInfo
    );

    // Return the constructed BST with the current root, left subtree, and right subtree
    return new BST(rootValue, leftSubtree, rightSubtree);
}

// Dummy data: Preorder traversal of a BST
const preOrderTraversalValues = [10, 5, 2, 7, 15, 12, 20];

// Call the function to reconstruct the BST
const bst = reconstructBst(preOrderTraversalValues);

// Function to print the tree in-order (helper to verify the tree structure)
function printInOrder(node) {
    if (node === null) {
        return;
    }
    printInOrder(node.left);
    process.stdout.write(node.value + " "); // Using process.stdout.write for cleaner output
    printInOrder(node.right);
}

// Print the reconstructed tree in-order to verify
console.log("In-order traversal of the reconstructed BST:");
printInOrder(bst);
