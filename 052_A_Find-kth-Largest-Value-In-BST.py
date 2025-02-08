# """
# Problem Statement:
# Given a Binary Search Tree (BST), write a function to find the Kth largest value in the BST.

# A Binary Search Tree (BST) is a binary tree where each node has a value, and for every node:
# - The left subtree contains only nodes with values less than the node's value.
# - The right subtree contains only nodes with values greater than the node's value.

# In this problem, we need to find the Kth largest element in the BST. The largest element is defined as the element with the highest value. 

# To solve this problem, we can utilize the following approach:

# Theory:
# 1. **In-Order Traversal:**
#    - Perform an in-order traversal of the BST. In a BST, in-order traversal visits the nodes in ascending order (left, root, right).
#    - Therefore, if we traverse the BST in-order, we will obtain the node values sorted in increasing order.

# 2. **Accessing Kth Largest Value:**
#    - To find the Kth largest value, we can determine its position in the sorted list:
#      - The Kth largest element in the BST corresponds to the element at the index `len(sortedNodeValues) - k` in the sorted node values list.
#    - For example, if K = 2, we want the second largest value, which is found at the index `len(sortedNodeValues) - 2`.

# 3. **Complexity:**
#    - The time complexity for performing in-order traversal of a BST is O(n), where n is the number of nodes in the tree.
#    - The space complexity is also O(n) for storing the sorted node values in a list.

# By following this approach, we can efficiently find the Kth largest value in a given BST.
# """




class BinaryTree:
    def __init__(self, value, left=None, right=None):
        # Initialize the Binary Tree node with a value and optional left and right children
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    # Initialize a list to store the sorted node values
    sortedNodeValues = []
    # Perform in-order traversal to get sorted node values
    inOrderTraverse(tree, sortedNodeValues)
    
    # Return the Kth largest value; subtract k to access from the end of the sorted list
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    # Base case: if the node is None, return
    if node is None:
        return

    # Traverse the left subtree
    inOrderTraverse(node.left, sortedNodeValues)
    
    # Append the current node's value to the sorted list
    sortedNodeValues.append(node.value)  # Fixed: Changed from node.values to node.value
    
    # Traverse the right subtree
    inOrderTraverse(node.right, sortedNodeValues)

# Dummy data to create a sample BST
# Example BST:
#         10
#        /  \
#       5   15
#      / \    \
#     2   5   20

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.left = BinaryTree(2)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(20)

# Specify the value of k to find the Kth largest value
k = 2

# Print the result
print(f"The {k}th largest value in the BST is: {findKthLargestValueInBst(root, k)}")

# To understand the execution, print the sorted node values
sortedNodeValues = []
inOrderTraverse(root, sortedNodeValues)
print("Sorted node values:", sortedNodeValues)
