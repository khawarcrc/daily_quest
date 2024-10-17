/*
Problem Statement:
------------------
You are tasked with implementing a Binary Search Tree (BST) in JavaScript. A BST is a data structure where each node has at most two children. The left child contains a value smaller than its parent node, and the right child contains a value larger than its parent node. The BST should allow the following operations:
  - Insert a key into the tree.
  - Check whether a key exists in the tree.
  - Delete a key from the tree.
  - Perform an inorder traversal to retrieve the keys in ascending order.

The challenge is to implement the BST efficiently, making sure that operations such as inserting, searching, and deleting have an average time complexity of O(log n) for balanced trees, and O(n) in the worst case (unbalanced trees).

Theory of Code:
---------------
1. **TreeNode Class**:
   - Represents a single node in the tree.
   - Each node contains:
     - `key`: the value of the node.
     - `left`: pointer/reference to the left child (nodes with smaller keys).
     - `right`: pointer/reference to the right child (nodes with larger keys).
   - Each node starts with its left and right children set to `null`.

2. **BinarySearchTree Class**:
   - Represents the entire binary search tree, starting with an empty `root`.
   - The `root` is initially `null`, indicating that the tree is empty.

3. **Insert Operation**:
   - Goal: Add a new key into the BST while maintaining the BST properties.
   - Process:
     - If the tree is empty (`root` is `null`), the new key becomes the root.
     - Otherwise, we recursively find the correct location by comparing the key to the current node:
       - If the key is smaller than the current node's key, we move to the left subtree.
       - If the key is larger, we move to the right subtree.
     - If we reach a `null` node, we insert the new key at that position.
   - The recursion ensures that we traverse the tree in a binary search manner, either going left or right, making the operation efficient.

4. **Contains Operation**:
   - Goal: Check whether a specific key exists in the tree.
   - Process:
     - Starting from the root, we recursively compare the key with the current node's key:
       - If the key matches the current node's key, return `true` (key found).
       - If the key is smaller, move to the left subtree.
       - If the key is larger, move to the right subtree.
     - If we reach a `null` node, the key is not found, so return `false`.
   - This operation follows the same binary search principles as insertion.

5. **Delete Operation**:
   - Goal: Remove a key from the tree while maintaining the BST properties.
   - Process:
     - Recursively search for the key in the tree.
     - Once found, there are three possible cases for deletion:
       - **Case 1: Node has no children (leaf node)**:
         - Simply remove the node by returning `null` to its parent.
       - **Case 2: Node has one child**:
         - Replace the node with its child.
       - **Case 3: Node has two children**:
         - Find the inorder successor (the smallest node in the right subtree).
         - Replace the node’s key with the successor's key.
         - Recursively delete the successor node.
   - The delete operation handles these cases efficiently while ensuring the tree remains a valid BST after deletion.

6. **_minValueNode Helper Method**:
   - This method is used to find the smallest node (inorder successor) in the right subtree during deletion.
   - The smallest node in a subtree is always the leftmost node, so we traverse to the leftmost child.

7. **Inorder Traversal**:
   - Goal: Retrieve all the keys in the BST in ascending order.
   - Process:
     - Traverse the tree in the following order:
       1. Visit the left subtree (smallest keys).
       2. Visit the current node (root of the subtree).
       3. Visit the right subtree (larger keys).
   - This traversal is performed recursively, and it guarantees that the keys are visited in ascending order.

8. **Private Methods (Underscore Prefix)**:
   - Methods like `_insert`, `_contains`, and `_delete` are prefixed with an underscore (`_`) to indicate they are private. This is a common convention in programming to signal that these methods should only be used internally by the class and not be accessed directly from outside the class.
   - JavaScript does not enforce private methods (unless using the newer `#` syntax), but this naming convention helps developers understand the intended usage of the method.

9. **Recursion**:
   - The insert, contains, and delete operations are all implemented using recursion.
   - Recursion is a technique where a function calls itself to solve smaller instances of the problem, which allows us to traverse the tree by moving left or right at each step.
   - Each recursive call operates on a smaller part of the tree (either the left or right subtree) until we reach the base case (a `null` node or finding the correct node).

10. **Edge Cases**:
   - Insertion, search, and deletion handle various edge cases:
     - Inserting a key into an empty tree.
     - Searching for a key that doesn't exist.
     - Deleting nodes with zero, one, or two children.
     - Deleting the root node or other internal nodes.
     - Ensuring that the BST properties are maintained after any operation.

Time Complexity:
----------------
- **Insert**: O(log n) on average, O(n) in the worst case (unbalanced tree).
- **Contains**: O(log n) on average, O(n) in the worst case (unbalanced tree).
- **Delete**: O(log n) on average, O(n) in the worst case (unbalanced tree).
- **Inorder Traversal**: O(n), where n is the number of nodes (since each node is visited once).

Summary:
--------
This code implements a binary search tree in JavaScript with key operations like insertion,
 searching, deletion, and inorder traversal. Recursion is heavily used to traverse the tree,
  and edge cases like handling empty trees and node deletions are efficiently managed. 
  The use of private methods (via underscore convention) helps separate internal logic from public API methods.
*/



// Class representing a single node in the Binary Search Tree
class TreeNode {
    constructor(key) {
        // Initialize node with a key and set left and right children as null
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

// Class representing the entire Binary Search Tree
class BinarySearchTree {
    constructor() {
        // Initialize the tree with an empty root (no nodes in the tree yet)
        this.root = null;
    }

    // Public method to insert a key into the BST
    insert(key) {
        // Check if the tree is empty, then the new key becomes the root
        if (this.root === null) {
            this.root = new TreeNode(key);
        } else {
            // Call the private _insert method to recursively find the right place
            this._insert(this.root, key);
        }
    }

    // Private method to recursively insert a key in the correct position
    _insert(node, key) {
        // Base case: prevent inserting duplicate keys
        if (key === node.key) {
            return;
        }
        // If the key is smaller than the current node's key, go to the left subtree
        else if (key < node.key) {
            if (node.left === null) {
                // Insert new key as left child if no left child exists
                node.left = new TreeNode(key);
            } else {
                // Recur to insert in the left subtree
                this._insert(node.left, key);
            }
        }
        // If the key is larger than the current node's key, go to the right subtree
        else {
            if (node.right === null) {
                // Insert new key as right child if no right child exists
                node.right = new TreeNode(key);
            } else {
                // Recur to insert in the right subtree
                this._insert(node.right, key);
            }
        }
    }

    // Public method to check if a key exists in the BST
    contains(key) {
        // Call the private _contains method to recursively search for the key
        return this._contains(this.root, key);
    }

    // Private method to recursively check if a key exists in the tree
    _contains(node, key) {
        // Base case: if the current node is null, key does not exist
        if (node === null) {
            return false;
        }
        // If the current node's key matches the search key, key exists
        if (key === node.key) {
            return true;
        }
        // If the key is smaller, search in the left subtree
        else if (key < node.key) {
            return this._contains(node.left, key);
        }
        // If the key is larger, search in the right subtree
        else {
            return this._contains(node.right, key);
        }
    }

    // Public method to delete a key from the BST
    delete(key) {
        // Call the private _delete method to handle deletion
        this.root = this._delete(this.root, key);
    }

    // Private method to recursively delete a key and adjust the tree
    _delete(node, key) {
        // Base case: if node is null, return null (key not found)
        if (node === null) {
            return node;
        }

        // If the key is smaller, go to the left subtree to delete the key
        if (key < node.key) {
            node.left = this._delete(node.left, key);
        }
        // If the key is larger, go to the right subtree to delete the key
        else if (key > node.key) {
            node.right = this._delete(node.right, key);
        }
        // If the key matches, this is the node to be deleted
        else {
            // Case 1: Node has no left child (replace node with right child)
            if (node.left === null) {
                return node.right;
            }
            // Case 2: Node has no right child (replace node with left child)
            else if (node.right === null) {
                return node.left;
            }
            // Case 3: Node has two children
            // Find the inorder successor (smallest value in the right subtree)
            let temp = this._minValueNode(node.right);
            // Replace node's key with the inorder successor's key
            node.key = temp.key;
            // Delete the inorder successor
            node.right = this._delete(node.right, temp.key);
        }

        return node;
    }

    // Helper method to find the smallest node in a subtree
    _minValueNode(node) {
        let current = node;
        // Traverse to the leftmost node (smallest node)
        while (current.left !== null) {
            current = current.left;
        }
        return current;
    }

    // Public method to return the inorder traversal (left-root-right)
    inorderTraversal() {
        return this._inorderTraversal(this.root, []);
    }

    // Private recursive method to perform inorder traversal
    _inorderTraversal(node, result) {
        if (node !== null) {
            // Recur on the left subtree
            this._inorderTraversal(node.left, result);
            // Add current node's key to the result array
            result.push(node.key);
            // Recur on the right subtree
            this._inorderTraversal(node.right, result);
        }
        return result;
    }
}

// Example usage of the Binary Search Tree
const bst = new BinarySearchTree();
bst.insert(50);  // Insert root node
bst.insert(30);  // Insert node to the left
bst.insert(70);  // Insert node to the right
bst.insert(20);  // Insert node further to the left
bst.insert(40);  // Insert node further to the left-right
bst.insert(60);  // Insert node further to the right-left
bst.insert(80);  // Insert node further to the right-right

console.log("Inorder Traversal:", bst.inorderTraversal());  // Output: [20, 30, 40, 50, 60, 70, 80]
console.log("Contains 40:", bst.contains(40));  // Output: true
console.log("Contains 100:", bst.contains(100));  // Output: false

// Deletion operations with edge case handling
bst.delete(20);  // Deleting a leaf node
console.log("Inorder Traversal after deleting 20:", bst.inorderTraversal());  // Output: [30, 40, 50, 60, 70, 80]

bst.delete(30);  // Deleting a node with one child
console.log("Inorder Traversal after deleting 30:", bst.inorderTraversal());  // Output: [40, 50, 60, 70, 80]

bst.delete(50);  // Deleting a node with two children
console.log("Inorder Traversal after deleting 50:", bst.inorderTraversal());  // Output: [40, 60, 70, 80]
