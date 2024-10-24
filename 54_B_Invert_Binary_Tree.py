# Problem Statement:
# The function 'invertBinaryTree' is designed to invert a binary tree using a recursive approach.
# Inverting a binary tree involves swapping the left and right children of every node in the tree.
# The recursion ensures that the tree is traversed in a depth-first manner, with left and right
# children being swapped at each node.

# Steps of Execution:
# 1. If the current node is None, return (base case for recursion).
# 2. Swap the left and right children of the current node.
# 3. Recursively call 'invertBinaryTree' on the left child.
# 4. Recursively call 'invertBinaryTree' on the right child.
# 5. The function completes once the entire tree has been traversed, and the left and right
#    children have been swapped at each node.

# Time Complexity: O(n), where n is the number of nodes in the tree (since each node is visited once).
# Space Complexity: O(h), where h is the height of the tree, which determines the recursive call stack size.


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to invert the binary tree using recursion
def invertBinaryTree(tree):
    # Base case: if the tree is None, return
    if tree is None:
        return

    # Swap the left and right children of the current node
    swapLeftAndRight(tree)

    # Recursively invert the left subtree
    invertBinaryTree(tree.left)

    # Recursively invert the right subtree
    invertBinaryTree(tree.right)


# Function to swap the left and right child of a node
def swapLeftAndRight(tree):

    # Swap the left and right child nodes
    tree.left, tree.right = tree.right, tree.left


# Function to print the binary tree in level-order
def printLevelOrder(tree):
    if tree is None:
        return

    # Use a queue for level-order traversal
    queue = [tree]

    while len(queue):
        current = queue.pop(0)
        # Print the current node's value
        print(current.value, end=" ")

        # Append the left and right children to the queue if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Dummy Data (Sample Binary Tree)
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

# Print the tree before inversion
print("Original Binary Tree (Level-Order):")
printLevelOrder(root)
print("\n")

# Invert the binary tree
invertBinaryTree(root)

# Print the inverted binary tree
print("\nInverted Binary Tree (Level-Order):")
printLevelOrder(root)
