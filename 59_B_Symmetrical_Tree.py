
# Problem Statement:
# Given a binary tree, the task is to determine if the tree is symmetrical around its center.
# A binary tree is considered symmetrical if the left subtree is a mirror reflection of the right subtree.

# Code Execution Theory:
# - The function `symmetricalTree` initiates the symmetry check by calling the `treesAreMirrored` function,
#   which compares the left and right subtrees of the binary tree.
# - The `treesAreMirrored` function checks the following:
#   - If both nodes (left and right) are not None and their values are equal,
#     it proceeds to check their children recursively:
#     - The left child's left subtree against the right child's right subtree.
#     - The left child's right subtree against the right child's left subtree.
#   - If the values do not match or one of the nodes is None, it checks if both nodes are None (returning True) 
#     or if only one is None (returning False).
# - The recursion continues until the base case is reached, determining the symmetry of the tree.
# - If all corresponding nodes in the left and right subtrees are equal and properly mirrored, the function returns True.
# - Otherwise, it returns False, indicating the tree is not symmetrical.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def symmetricalTree(tree):
    # Call the helper function to check if the left and right subtrees are mirrored
    return treesAreMirrored(tree.left, tree.right)

def treesAreMirrored(left, right):
    # Both nodes are not None and their values match
    if left is not None and right is not None and left.value == right.value:
        # Recursively check the left child of the left subtree and the right child of the right subtree
        # Also check the right child of the left subtree and the left child of the right subtree
        return treesAreMirrored(left.left, right.right) and treesAreMirrored(left.right, right.left)
    
    # If both nodes are None, they are mirrored; otherwise, they are not
    return left == right

# Dummy data for testing
# Constructing a symmetrical binary tree
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

# Execute the function with the dummy data
print(symmetricalTree(root))  # Expected output: True


