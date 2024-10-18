# Problem Statement:
# Given a binary tree, we want to perform three types of tree traversals:
# 1. In-order traversal: Visit the left subtree, root node, and right subtree.
# 2. Pre-order traversal: Visit the root node, left subtree, and right subtree.
# 3. Post-order traversal: Visit the left subtree, right subtree, and root node.
# The goal is to traverse the binary tree using each method and output the nodes
# in the specific order required for each traversal type.

# Theory to Solve the Problem:
# A binary tree is a hierarchical structure where each node has at most two children:
# a left child and a right child. The traversal of a tree means visiting each node 
# exactly once in a specified order. We will implement three traversal methods:
# 1. In-order Traversal (Left, Root, Right): This visits nodes in ascending order for a Binary Search Tree (BST).
# 2. Pre-order Traversal (Root, Left, Right): This visits the root node first before its subtrees.
# 3. Post-order Traversal (Left, Right, Root): This visits subtrees before the root node.

# Each traversal can be done recursively, where the base case is when we reach a `None` node (leaf node's child).
# The recursive approach ensures that we visit the tree in the required order.

# Define the structure for a node in the binary tree


# In-order: Left subtree → Root → Right subtree.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree, array):
    # Base case: if the current node is None (leaf node's child)
    if tree is not None:
        # Recursively traverse the left subtree
        inOrderTraverse(tree.left, array)
        # Visit the root node and append its value to the array
        array.append(tree.value)
        # Recursively traverse the right subtree
        inOrderTraverse(tree.right, array)
    return array


# Function to perform pre-order traversal (Root, Left, Right)
# Pre-order: Root → Left subtree → Right subtree
def preOrderTraverse(tree, array):
    # Base case: if the current node is None (leaf node's child)
    if tree is not None:
        # Visit the root node and append its value to the array
        array.append(tree.value)
        # Recursively traverse the left subtree
        preOrderTraverse(tree.left, array)
        # Recursively traverse the right subtree
        preOrderTraverse(tree.right, array)
    return array


# Function to perform post-order traversal (Left, Right, Root)
# Post-order: Left subtree → Right subtree → Root.
def postOrderTraverse(tree, array):
    # Base case: if the current node is None (leaf node's child)
    if tree is not None:
        # Recursively traverse the left subtree
        postOrderTraverse(tree.left, array)
        # Recursively traverse the right subtree
        postOrderTraverse(tree.right, array)
        # Visit the root node and append its value to the array
        array.append(tree.value)
    return array



# Create dummy data (binary tree)
root = TreeNode(5)  # Root node
root.left = TreeNode(3)  # Left child of root
root.right = TreeNode(7)  # Right child of root
root.left.left = TreeNode(2)  # Left child of 3
root.left.right = TreeNode(4)  # Right child of 3
root.right.right = TreeNode(8)  # Right child of 7

# Perform the traversals
in_order_result = inOrderTraverse(root, [])  # In-order traversal result
pre_order_result = preOrderTraverse(root, [])  # Pre-order traversal result
post_order_result = postOrderTraverse(root, [])  # Post-order traversal result

# Output the results
print("In-order Traversal:", in_order_result)
print("Pre-order Traversal:", pre_order_result)
print("Post-order Traversal:", post_order_result)



#     5
#    / \
#   3   7
#  / \   \
# 2   4   8
