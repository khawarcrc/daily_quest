# Problem Statement:
# Given a binary tree, we want to find its diameter, which is defined as the longest path 
# between any two nodes in the tree. The path may or may not pass through the root node.
# 
# Execution:
# To demonstrate the function, we will create a sample binary tree and calculate its diameter.
# Example of the binary tree structure:
#         1
#        / \
#       2   3
#      / \
#     4   5
#
# The diameter of this tree is 4 (the path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3).
# 
# The algorithm works by recursively calculating the height and diameter of each subtree.
# - For each node, the diameter is either:
#     1. The diameter of the left or right subtree, or
#     2. The longest path through the root, calculated as the sum of heights of the left 
#        and right subtrees at the current node.
# 
# - The height of a node is calculated as 1 plus the maximum height of its left and right children.
# - Using a helper class `TreeInfo`, we store the diameter and height for each node, making it
#   easy to update the diameter and height at each step.

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Node value
        self.left = left    # Left child
        self.right = right  # Right child


def binaryTreeDiameter(tree):
    # """
    # Main function to calculate the diameter of the binary tree.
    # Calls the helper function 'getTreeInfo' to retrieve diameter.
    # """
    return getTreeInfo(tree).diameter  # Retrieve diameter from TreeInfo returned by helper function


def getTreeInfo(tree):
    # """
    # Helper function to calculate the diameter and height of the tree at each node.
    # Uses recursion to gather information from each subtree.
    # """
    if tree is None:
        return TreeInfo(0, 0)  # If the tree is empty, diameter and height are both 0

    # Get TreeInfo for left and right subtrees recursively
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    # Calculate the longest path through the root as the sum of left and right heights
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    # Find the maximum diameter so far among left, right, or the longest path through root
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    # Calculate the height of the current node
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)  # Return updated diameter and height


class TreeInfo:
    # """
    # Helper class to store diameter and height of the tree.
    # - diameter: Maximum length of the longest path found so far.
    # - height: Maximum height of the tree at each node.
    # """
    def __init__(self, diameter, height):
        self.diameter = diameter  # Diameter of the tree at this node
        self.height = height      # Height of the tree at this node


# Creating dummy data to test the function
if __name__ == "__main__":
    # Constructing the example binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    # Calculating the diameter of the binary tree
    diameter = binaryTreeDiameter(root)
    print(f"The diameter of the binary tree is: {diameter}")
