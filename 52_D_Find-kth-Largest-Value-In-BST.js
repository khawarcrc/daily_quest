class BST {
    constructor(value, left = null, right = null) {
        // Initialize a Binary Search Tree node with a value and optional left and right children
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

class TreeInfo {
    constructor(numberOfNodesVisited, latestVisitedNodeValue) {
        // Initialize TreeInfo to keep track of the number of nodes visited and the latest visited node value
        this.numberOfNodesVisited = numberOfNodesVisited;
        this.latestVisitedNodeValue = latestVisitedNodeValue;
    }
}

function findKthLargestValueInBst(tree, k) {
    // Create an instance of TreeInfo to track the number of nodes visited and the latest visited node value
    const treeInfo = new TreeInfo(0, -1);
    
    // Perform reverse in-order traversal of the BST
    reverseInOrderTraverse(tree, k, treeInfo);
    
    // Return the latest visited node value which corresponds to the Kth largest value
    return treeInfo.latestVisitedNodeValue;
}

function reverseInOrderTraverse(node, k, treeInfo) {
    // Base case: if the node is null or if we've already visited K nodes, return
    if (node === null || treeInfo.numberOfNodesVisited >= k) return;

    // Traverse the right subtree first (to get the largest values first)
    reverseInOrderTraverse(node.right, k, treeInfo);
    
    // If we haven't visited K nodes yet, visit this node
    if (treeInfo.numberOfNodesVisited < k) {
        treeInfo.numberOfNodesVisited += 1;  // Increment the count of visited nodes
        treeInfo.latestVisitedNodeValue = node.value;  // Update the latest visited node value
        console.log(`Visited Node: ${node.value}, Nodes Visited: ${treeInfo.numberOfNodesVisited}`);  // Print for understanding

        // Traverse the left subtree
        reverseInOrderTraverse(node.left, k, treeInfo);
    }
}

// Dummy data to create a sample BST
// Example BST:
//         10
//        /  \
//       5   15
//      / \    \
//     2   5   20

const root = new BST(10);
root.left = new BST(5);
root.right = new BST(15);
root.left.left = new BST(2);
root.left.right = new BST(5);
root.right.right = new BST(20);

// Specify the value of k to find the Kth largest value
const k = 2;

// Print the result
console.log(`The ${k}th largest value in the BST is: ${findKthLargestValueInBst(root, k)}`);

// To understand the execution, we will see the console.log statements as we visit nodes
