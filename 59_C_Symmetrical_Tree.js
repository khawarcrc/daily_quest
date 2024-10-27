class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function symmetricalTree(tree) {
    // Initialize two stacks for left and right subtrees
    let stackLeft = [tree.left];
    let stackRight = [tree.right];

    // Loop until there are no nodes left in the left stack
    while (stackLeft.length > 0) {
        let left = stackLeft.pop();  // Pop the left node from the stack
        let right = stackRight.pop();  // Pop the right node from the stack

        // Check if both nodes are null (base case)
        if (left === null && right === null) continue;

        // If one node is null or their values don't match, return false
        if (left === null || right === null || left.value !== right.value) {
            return false;
        }

        // Add left and right children of the left node to the stack
        stackLeft.push(left.left);
        stackLeft.push(left.right);
        // Add right and left children of the right node to the stack (note the order)
        stackRight.push(right.right);
        stackRight.push(right.left);
    }

    return true;  // Return true if the tree is symmetrical
}

// Dummy data for testing
// Constructing a symmetrical binary tree
//         1
//        / \
//       2   2
//      / \ / \
//     3  4 4  3

const root = new Node(1);
root.left = new Node(2);
root.right = new Node(2);
root.left.left = new Node(3);
root.left.right = new Node(4);
root.right.left = new Node(4);
root.right.right = new Node(3);

// Execute the function with the dummy data
console.log(symmetricalTree(root));  // Expected output: true
