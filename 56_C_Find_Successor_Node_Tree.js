class BinaryTree {
    constructor(value, left = null, right = null, parent = null) {
        this.value = value;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }
}

function findSuccessor(tree, node) {
    // If node has a right child, successor is the leftmost node in right subtree
    if (node.right !== null) {
        return getLeftMostChild(node.right);
    }
    // If no right child, find the rightmost parent
    return getRightMostParent(node);
}

function getLeftMostChild(node) {
    // Traverse to the leftmost child node
    let currentNode = node;
    while (currentNode.left !== null) {
        currentNode = currentNode.left;
    }
    return currentNode;
}

function getRightMostParent(node) {
    // Traverse upwards to find the nearest ancestor that is a left child
    let currentNode = node;
    while (currentNode.parent !== null && currentNode.parent.right === currentNode) {
        currentNode = currentNode.parent;
    }
    return currentNode.parent;
}

// Edge Case Handling
// - Node is null: Return null (no successor)
// - Node has no right child and no valid rightmost parent: Return null (no successor)

// Enhanced function with edge case handling:
function findSuccessorWithEdgeCases(tree, node) {
    if (node === null) return null;  // Edge Case: Node is null
    
    if (node.right !== null) {
        return getLeftMostChild(node.right);
    }
    
    return getRightMostParent(node) || null;  // If no valid rightmost parent, return null
}

// Creating dummy data for testing
const root = new BinaryTree(20);
const node10 = new BinaryTree(10);
const node30 = new BinaryTree(30);
const node5 = new BinaryTree(5);
const node15 = new BinaryTree(15);
const node25 = new BinaryTree(25);
const node35 = new BinaryTree(35);

// Setting up parent relationships
node10.parent = root;
node30.parent = root;
node5.parent = node10;
node15.parent = node10;
node25.parent = node30;
node35.parent = node30;

// Linking nodes to form the tree structure
root.left = node10;
root.right = node30;
node10.left = node5;
node10.right = node15;
node30.left = node25;
node30.right = node35;

/*
Tree Structure:
         20
       /    \
     10      30
    /   \    /  \
   5    15  25   35

- Node 10's successor is 15 (its right child).
- Node 15's successor is 20 (nearest ancestor where node 10 is a left child).
- Node 20's successor is 25 (leftmost node in the right subtree).
- Node 35 has no successor (it's the rightmost node in the tree).
*/

// Testing the findSuccessorWithEdgeCases function
const testNode = node10;
const successor = findSuccessorWithEdgeCases(root, testNode);

if (successor) {
    console.log(`The successor of node ${testNode.value} is ${successor.value}`);
} else {
    console.log(`The node ${testNode.value} has no successor.`);
}
