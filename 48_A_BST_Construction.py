# Problem Statement:
# You are required to implement a Binary Search Tree (BST) that supports the following operations:
# - Insert: Add a value to the tree while maintaining the BST property.
# - Contains: Check whether a value exists in the tree.
# - Remove: Remove a value from the tree, ensuring that the BST structure remains intact after deletion.
# The BST should be implemented in such a way that it supports the insertion, searching, and removal of values 
# in logarithmic time, assuming a balanced tree.

# Key Concepts:
# - A Binary Search Tree (BST) is a binary tree where each node has at most two children, referred to as the left 
#   and right child. The left child’s value is always less than its parent node's value, and the right child’s 
#   value is always greater than or equal to its parent node's value. This property must hold for all nodes 
#   in the tree.
# - The primary benefit of a BST is that it allows for fast lookup, insertion, and removal of elements 
#   (O(log n) on average), assuming the tree is balanced.

# Insert Operation:
# - The `insert` operation is designed to add new nodes to the BST while preserving the BST properties.
# - Starting from the root, if the new value is smaller than the current node’s value, we move to the left subtree.
#   If the new value is greater than or equal to the current node’s value, we move to the right subtree.
# - The process continues until an appropriate empty spot is found (i.e., the left or right child is `None`), 
#   where the new node is inserted.
# - The time complexity of the `insert` operation is O(log n) on average for a balanced tree, where `n` 
#   is the number of nodes in the tree. In the worst case (when the tree becomes a linear structure, like a linked list), 
#   the time complexity degrades to O(n).

# Contains Operation:
# - The `contains` method checks whether a value is present in the tree.
# - It works similarly to the `insert` method in terms of tree traversal. Starting from the root, 
#   it compares the target value with the current node’s value.
# - If the value is smaller, it moves to the left subtree; if the value is larger, it moves to the right subtree.
#   If it finds the target value at a node, it returns `True`. If it reaches a `None` node, it returns `False`.
# - The time complexity of `contains` is O(log n) in the average case and O(n) in the worst case for 
#   an unbalanced tree.

# Remove Operation:
# - The `remove` method deletes a node from the tree while ensuring that the BST property is maintained after deletion.
# - There are three primary cases for node removal:
#   1. **Node with no children (leaf node)**: The node is simply removed.
#   2. **Node with one child**: The node is removed, and its child takes its place (the child is promoted).
#   3. **Node with two children**: The node’s value is replaced by the smallest value from its right subtree 
#      (the "in-order successor"), and the node containing that smallest value is then removed from the subtree.
# - Special handling is required when removing the root node, as it does not have a parent. In this case, 
#   one of the root’s children must become the new root.
# - The time complexity of `remove` is O(log n) on average, but in the worst case, it can degrade to O(n) 
#   if the tree becomes unbalanced.

# Helper Method - getMinValue:
# - The `getMinValue` method is a utility function used during the `remove` operation to find the minimum value 
#   in a node’s right subtree.
# - It works by traversing to the left-most node of the subtree, as the left-most node in a BST is always 
#   the smallest value in that subtree.
# - This method is crucial when removing a node with two children, as it helps in finding the replacement value 
#   (the in-order successor).
# - The time complexity of `getMinValue` is O(log n) for a balanced tree and O(n) in the worst case.

# Edge Cases:
# - Removing the root node is a special case that needs careful handling since it has no parent node. 
#   Depending on whether it has one or two children, we either promote a child or replace its value 
#   with the minimum value from the right subtree.
# - Inserting duplicate values is allowed in this implementation. Duplicate values are inserted in the right subtree 
#   by treating `>=` as a rule to move right. However, this can be customized to disallow duplicates or handle them differently.

# Overall Time Complexity:
# - For balanced trees, the time complexity for insert, contains, and remove operations is O(log n), where `n` is 
#   the number of nodes in the tree.
# - In the worst-case scenario (if the tree becomes unbalanced), the time complexity for these operations 
#   can degrade to O(n).

# Summary:
# - The BST class provides methods for inserting values, checking for value existence, and removing values.
# - It ensures that the Binary Search Tree properties are maintained during each operation, while handling special cases 
#   like removing the root or nodes with children.
# - The class also includes a helper method `getMinValue` to assist in finding the smallest value in a subtree, 
#   which is critical for the remove operation.
# - The average time complexity for all operations in a balanced BST is O(log n), making the BST an efficient 
#   data structure for ordered data operations.



# Binary Search Tree (BST) Class Definition
class BST: 
    def __init__(self, value): 
        # Initialize the BST with a root value, and left and right pointers
        self.value = value 
        self.left = None
        self.right = None

    # Insert method to add a new node to the BST
    def insert(self, value): 
        currentNode = self  # Start at the root
        while True:  # Loop to traverse the tree
            if value < currentNode.value:  # If the new value is less, go to the left
                if currentNode.left is None:  # If no left child, insert new node
                    currentNode.left = BST(value)
                    break  # Exit after inserting
                else: 
                    currentNode = currentNode.left  # Move to the left node and continue
            else:  # If the new value is greater or equal, go to the right
                if currentNode.right is None:  # If no right child, insert new node
                    currentNode.right = BST(value)
                    break  # Exit after inserting
                else: 
                    currentNode = currentNode.right  # Move to the right node and continue
        return self  # Return self for potential chaining of operations

    # Contains method to check if a value exists in the tree
    def contains(self, value):  # Corrected the method name from `containe` to `contains`
        currentNode = self  # Start at the root
        while currentNode is not None:  # Traverse the tree until the node is None
            if value < currentNode.value:  # Move left if value is smaller
                currentNode = currentNode.left  
            elif value > currentNode.value:  # Move right if value is larger
                currentNode = currentNode.right   
            else: 
                return True  # Value found
        return False  # Value not found in the tree

    # Remove method to delete a node with the specified value
    def remove(self, value, parentNode=None): 
        currentNode = self  # Start at the root
        while currentNode is not None:  # Traverse the tree until the node is None
            if value < currentNode.value:  # Move left if the value is smaller
                parentNode = currentNode 
                currentNode = currentNode.left 
            elif value > currentNode.value:  # Move right if the value is larger
                parentNode = currentNode 
                currentNode = currentNode.right 
            else:  # Node to be removed is found
                if currentNode.left is not None and currentNode.right is not None:  
                    # Case where the node has two children
                    currentNode.value = currentNode.right.getMinValue()  # Replace with min value from right subtree
                    currentNode.right.remove(currentNode.value, currentNode)  # Recursively remove the node with the smallest value
                elif parentNode is None:  
                    # Special case where we're removing the root node
                    if currentNode.left is not None:  
                        # Root has only left child, so we promote the left child
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right    
                        currentNode.left = currentNode.left.left 
                    elif currentNode.right is not None:  
                        # Root has only right child, so we promote the right child
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left 
                        currentNode.right = currentNode.right.right 
                    else: 
                        currentNode.value = None  # Case where tree becomes empty
                elif parentNode.left == currentNode:  
                    # Case where the node to be removed is the left child
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right 
                elif parentNode.right == currentNode:  
                    # Case where the node to be removed is the right child
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right 
                break  # Exit after removal
        return self  # Return the modified tree

    # Helper method to find the minimum value in the right subtree
    def getMinValue(self): 
        currentNode = self  # Start at the node from which we want to find the min value
        while currentNode.left is not None:  # Keep moving to the left-most node
            currentNode = currentNode.left 
        return currentNode.value  # Return the smallest value

# Create a sample BST and insert values into it
bst = BST(10)  # Root node with value 10
bst.insert(5)  # Insert node with value 5
bst.insert(15)  # Insert node with value 15
bst.insert(2)  # Insert node with value 2
bst.insert(5)  # Insert duplicate value 5
bst.insert(1)  # Insert node with value 1
bst.insert(13)  # Insert node with value 13
bst.insert(22)  # Insert node with value 22
bst.insert(14)  # Insert node with value 14

# Check if the tree contains certain values
print(bst.contains(15))  # Should return True
print(bst.contains(99))  # Should return False

# Remove a node from the BST
bst.remove(10)  # Remove the root node (value 10)

# Check tree structure after removal
print(bst.contains(10))  # Should return False
