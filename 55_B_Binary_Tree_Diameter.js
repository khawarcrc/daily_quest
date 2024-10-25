// Problem Statement:
// Given a binary tree, we want to find its diameter, which is defined as the longest path
// between any two nodes in the tree. The path may or may not pass through the root node.
//
// Execution:
// To demonstrate the function, we will create a sample binary tree and calculate its diameter.
// Example of the binary tree structure:
//         1
//        / \
//       2   3
//      / \
//     4   5
//
// The diameter of this tree is 4 (the path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3).
//
// The algorithm works by recursively calculating the height and diameter of each subtree.
// - For each node, the diameter is either:
//     1. The diameter of the left or right subtree, or
//     2. The longest path through the root, calculated as the sum of heights of the left
//        and right subtrees at the current node.
//
// - The height of a node is calculated as 1 plus the maximum height of its left and right children.
// - Using a helper class `TreeInfo`, we store the diameter and height for each node, making it
//   easy to update the diameter and height at each step.

class BinaryTree {
  constructor(value, left = null, right = null) {
    this.value = value; // Node value
    this.left = left; // Left child
    this.right = right; // Right child
  }
}

function binaryTreeDiameter(tree) {
  // Main function to calculate the diameter of the binary tree.
  // Calls the helper function 'getTreeInfo' to retrieve diameter.
  return getTreeInfo(tree).diameter;
}

function getTreeInfo(tree) {
  // Helper function to calculate the diameter and height of the tree at each node.
  // Uses recursion to gather information from each subtree.
  if (tree === null) {
    return new TreeInfo(0, 0); // If the tree is empty, diameter and height are both 0
  }

  // Get TreeInfo for left and right subtrees recursively
  const leftTreeInfo = getTreeInfo(tree.left);
  const rightTreeInfo = getTreeInfo(tree.right);

  // Calculate the longest path through the root as the sum of left and right heights
  const longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height;
  // Find the maximum diameter so far among left, right, or the longest path through root
  const maxDiameter = Math.max(leftTreeInfo.diameter, rightTreeInfo.diameter);
  const currentDiameter = Math.max(longestPathThroughRoot, maxDiameter);
  // Calculate the height of the current node
  const currentHeight = 1 + Math.max(leftTreeInfo.height, rightTreeInfo.height);

  // Debug logs to verify calculation at each step
  console.log(
    `Node: ${tree.value}, Height: ${currentHeight}, Diameter: ${currentDiameter}, Path Through Root: ${longestPathThroughRoot}`
  );

  return new TreeInfo(currentDiameter, currentHeight); // Return updated diameter and height
}

class TreeInfo {
  // Helper class to store diameter and height of the tree.
  // - diameter: Maximum length of the longest path found so far.
  // - height: Maximum height of the tree at each node.
  constructor(diameter, height) {
    this.diameter = diameter; // Diameter of the tree at this node
    this.height = height; // Height of the tree at this node
  }
}

// Creating dummy data to test the function
// Constructing the example binary tree:
//         1
//        / \
//       2   3
//      / \
//     4   5
const root = new BinaryTree(1);
root.left = new BinaryTree(2);
root.right = new BinaryTree(3);
root.left.left = new BinaryTree(4);
root.left.right = new BinaryTree(5);

// Calculating the diameter of the binary tree
const diameter = binaryTreeDiameter(root);
console.log(`The diameter of the binary tree is: ${diameter}`);
