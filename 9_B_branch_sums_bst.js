// 1. Define a BinaryTree class to represent each node with a value and left/right children initialized to null.

// 2. Use the branchSums function to initialize an empty array and start the recursive process to calculate branch sums.

// 3. Implement calculateBranchSums function to recursively traverse the tree:
//    - If the node is null, return (base case).
//    - Add the current node's value to the running sum.
//    - If the node is a leaf (no children), push the running sum to the sums array.

// 4. If the node is not a leaf, recursively call calculateBranchSums on the left and right children with updated sums.

// 5. Construct a binary tree and use the branchSums function to calculate and print the sums of all branches from root to leaf.


class BinaryTree {
    // Constructor to initialize the node with a value and set left and right children to null
    constructor(value) {
      this.value = value; // Assigns the given value to the node
      this.left = null;   // Initially, the left child is set to null
      this.right = null;  // Initially, the right child is set to null
    }
  }
  
  function branchSums(root) {
    // Function to calculate the sums of all branches in the binary tree
    // root -- the root node of the binary tree
    // Returns an array containing the sums of each branch
    const sums = [];  // Initialize an empty array to store the sums
    calculateBranchSums(root, 0, sums);  // Call the helper function to compute branch sums
    return sums;  // Return the array of sums
  }
  
  function calculateBranchSums(node, runningSum, sums) {
    // Helper function to calculate the sum of each branch and append it to the sums array
    // node -- the current node in the binary tree
    // runningSum -- the sum accumulated up to this node
    // sums -- array that stores the sum of each branch
  
    if (!node) {  // Base case: if the node is null, return
      return;
    }
  
    const newRunningSum = runningSum + node.value;  // Update the running sum by adding the current node's value
    console.log(`At node with value ${node.value}, running sum is ${newRunningSum}`);  // Print current node and running sum
  
    if (!node.left && !node.right) {  // Check if the current node is a leaf
      sums.push(newRunningSum);  // Append the running sum to the array if it's a leaf node
      console.log(`Leaf node found with value ${node.value}, appending sum ${newRunningSum} to sums`);  // Print leaf node and sum
      return;
    }
  
    // Recursively call the function for the left and right children
    calculateBranchSums(node.left, newRunningSum, sums);  // Traverse left child
    calculateBranchSums(node.right, newRunningSum, sums);  // Traverse right child
  }
  
  // Dummy data for testing
  const root = new BinaryTree(1);  // Create the root node with value 1
  root.left = new BinaryTree(2);   // Create left child of root with value 2
  root.right = new BinaryTree(3);  // Create right child of root with value 3
  root.left.left = new BinaryTree(4);  // Create left child of node 2 with value 4
  root.left.right = new BinaryTree(5);  // Create right child of node 2 with value 5
  root.right.left = new BinaryTree(6);  // Create left child of node 3 with value 6
  root.right.right = new BinaryTree(7);  // Create right child of node 3 with value 7
  
  // The structure of the tree is:
  //        1
  //      /   \
  //     2     3
  //    / \   / \
  //   4   5 6   7
  
  // Calculate the branch sums
  const sums = branchSums(root);  // Get the branch sums from the tree
  console.log("Branch sums:", sums);  // Print the array of branch sums
  