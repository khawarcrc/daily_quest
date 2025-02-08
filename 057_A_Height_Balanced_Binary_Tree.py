
# Problem Statement:
# 
# Write a function to determine if a given binary tree is height-balanced. A binary tree is considered 
# height-balanced if, for every node in the tree, the height difference between the left and right 
# subtrees is no greater than 1. Implement this function by creating a recursive approach to check 
# the balance and height of each subtree within the binary tree.
#
# The function should:
# - Return True if the tree is balanced and False if it is not.
# - Use a helper class to store information about each node’s balance and height status.
#
# Execution Theory:
# 
# 1. The program defines two classes: `BinaryTree` and `TreeInfo`.
#     - `BinaryTree`: Represents each node in the tree and holds references to left and right child nodes.
#     - `TreeInfo`: Stores information about whether a subtree is balanced and the height of that subtree.
#
# 2. The `heightBalancedBinaryTree` function is the main function that checks if the tree is balanced.
#     - It initiates the recursive `getTreeInfo` function, which traverses the entire tree.
#     - The `getTreeInfo` function uses a recursive approach, checking the balance and height of each subtree.
#
# 3. Recursive Tree Information Retrieval:
#     - Starting from the root node, the `getTreeInfo` function:
#         a. Recursively calls itself to process the left subtree, returning balance and height details.
#         b. Recursively calls itself to process the right subtree, returning balance and height details.
#     - Each node calculates its own subtree balance by evaluating:
#         - If both left and right subtrees are balanced.
#         - If the height difference between the left and right subtrees is ≤ 1.
#     - Each node’s height is calculated as the maximum height of its left or right subtree plus 1.
# 
# 4. Base Case:
#     - When `getTreeInfo` encounters a leaf node’s child (None), it returns `True` for balance 
#       and a height of -1. This allows leaf nodes to be considered balanced with height 0.
#
# Overall Concept:
#
# The core concept is to use recursion to gather balance and height information for each subtree,
# combining these results from the leaf nodes up to the root node. By returning balance status and
# height at each node, the algorithm ensures that each node’s balance and height status contributes
# to an accurate assessment of whether the entire binary tree is height-balanced.




class BinaryTree:
    def __init__(self, value, left=None, right=None):
        # Initializes a node in the binary tree with a value and optional left and right child nodes
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        # Stores information about whether a subtree is balanced and its height
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Get information about the entire tree's balance status and height
    treeInfo = getTreeInfo(tree)
    print(f"Tree is balanced: {treeInfo.isBalanced}")
    return treeInfo.isBalanced


def getTreeInfo(node):
    # Base case: if the node is None, return True for balance and -1 for height (leaf level)
    if node is None:
        print("Reached a leaf node, returning True and height -1")
        return TreeInfo(True, -1)

    # Recursively get information about the left subtree
    leftSubTreeInfo = getTreeInfo(node.left)
    print(f"Node {node.value} - Left subtree info: isBalanced={leftSubTreeInfo.isBalanced}, height={leftSubTreeInfo.height}")

    # Recursively get information about the right subtree
    rightSubTreeInfo = getTreeInfo(node.right)
    print(f"Node {node.value} - Right subtree info: isBalanced={rightSubTreeInfo.isBalanced}, height={rightSubTreeInfo.height}")

    # Check if the current node's subtree is balanced
    isBalanced = (
        leftSubTreeInfo.isBalanced
        and rightSubTreeInfo.isBalanced
        and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    )
    # Calculate the height of the current node's subtree
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1

    print(f"Node {node.value} - isBalanced={isBalanced}, height={height}")
    return TreeInfo(isBalanced, height)


# Dummy data - creating a balanced binary tree
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

# Calling the function to check if the tree is balanced
print("Is the binary tree height-balanced?", heightBalancedBinaryTree(root))
