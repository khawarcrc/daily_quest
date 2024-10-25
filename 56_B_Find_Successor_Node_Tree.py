# Problem Statement:
# Given a binary tree and a specific node within that tree, write a function `findSuccessor`
# to find the in-order successor of the given node. The in-order successor of a node is
# the node that appears immediately after the given node in an in-order traversal
# (left, root, right) of the tree. If the node has no in-order successor, the function
# should return `None`. Assume each node has a link to its parent node, making it easier
# to traverse upwards in the tree.

# Theory and Execution of Solution:

# 1. Class Definition - BinaryTree:
#    - A class `BinaryTree` is defined to represent a node within the binary tree.
#    - Each node contains:
#      - `value`: The value stored in the node.
#      - `left`: A pointer to the left child.
#      - `right`: A pointer to the right child.
#      - `parent`: A pointer to the parent of the node, enabling upward traversal.
#    - By including a parent pointer, the tree enables easier traversal in the upward
#      direction when finding a successor.

# 2. Main Function - findSuccessor:
#    - The function `findSuccessor` takes in two arguments: `tree`, which is the root of
#      the binary tree, and `node`, which is the node for which we want to find the successor.
#    - The function uses two helper functions, `getLeftMostChild` and `getRightMostParent`,
#      to determine the successor based on the node's structure and parent relationships.
#
#    - Steps in `findSuccessor`:
#      - **Check Right Subtree**: If the `node` has a right child, then its successor will
#        be the leftmost node in its right subtree. The `getLeftMostChild` helper function
#        is used here.
#      - **No Right Child**: If there is no right child, the successor lies somewhere
#        upwards in the tree. The function then calls `getRightMostParent` to find the
#        closest ancestor where the node would be in the left subtree of an ancestor.

# 3. Helper Function - getLeftMostChild:
#    - This helper function finds the leftmost child of a given node.
#    - It begins with the `node` passed to it and traverses down the left child
#      of each node until it reaches a node with no left child.
#    - The leftmost node in the subtree is then returned as the successor.
#    - This is efficient for finding the smallest node in any subtree, commonly
#      the in-order successor in the right subtree.

# 4. Helper Function - getRightMostParent:
#    - This helper function finds the nearest ancestor where the given node is
#      part of its left subtree.
#    - Starting with the given `node`, it traverses upward until it finds a parent
#      node that has the `node` in its left subtree.
#    - If a node is the right child of its parent, the function continues moving
#      upward until it finds a node that is the left child of its parent or reaches
#      the root. The parent of that left child is the in-order successor.
#    - If it reaches the root with no left alignment, there is no successor, and
#      the function returns `None`.


# Time Complexity Analysis:
# - The `findSuccessor` function has a time complexity of O(h), where h is the height
#   of the tree, as it may traverse from a node downwards in the case of `getLeftMostChild`
#   or upwards in the case of `getRightMostParent`. Both functions operate within
#   a single traversal path from the node to a leaf or root, resulting in linear
#   performance relative to the tree height.
# - The space complexity is O(1) as it requires only a constant amount of extra space.


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        # Initialize a binary tree node with value, left, right, and parent
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # If node has a right child, successor is the leftmost node in right subtree
    if node.right is not None:
        return getLeftMostChild(node.right)
    # If no right child, find the rightmost parent
    return getRightMostParent(node)


def getLeftMostChild(node):
    # Traverse to the leftmost child node
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode


def getRightMostParent(node):
    # Traverse upwards to find the nearest ancestor that is a left child
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent


# Creating dummy data for testing
root = BinaryTree(20)
node10 = BinaryTree(10, parent=root)
node30 = BinaryTree(30, parent=root)
node5 = BinaryTree(5, parent=node10)
node15 = BinaryTree(15, parent=node10)
node25 = BinaryTree(25, parent=node30)
node35 = BinaryTree(35, parent=node30)

# Linking nodes to form the tree structure
root.left = node10
root.right = node30
node10.left = node5
node10.right = node15
node30.left = node25
node30.right = node35

# Testing the findSuccessor function
test_node = node10
successor = findSuccessor(root, test_node)
if successor:
    print(f"The successor of node {test_node.value} is {successor.value}")
else:
    print(f"The node {test_node.value} has no successor.")


# Execution Flow Example with Dummy Data:
# - Example Tree Structure:
#         20
#       /    \
#     10      30
#    /   \    /  \
#   5    15  25   35
#
# - Execution for finding successor of node 10:
#   - Node 10 has a right child (node 15).
#   - `findSuccessor` calls `getLeftMostChild` on node 15.
#   - `getLeftMostChild` traverses node 15's left subtree and finds that node 15 has
#     no left child, so it is returned as the successor.
#   - Thus, the in-order successor of node 10 is node 15.
#
# - Execution for finding successor of node 30:
#   - Node 30 has a right child (node 35).
#   - `findSuccessor` calls `getLeftMostChild` on node 35.
#   - `getLeftMostChild` finds that node 35 has no left child, so it is returned as
#     the successor.
#   - The in-order successor of node 30 is node 35.
#
# - Execution for finding successor of node 15:
#   - Node 15 has no right child.
#   - `findSuccessor` calls `getRightMostParent` on node 15.
#   - `getRightMostParent` finds that node 10 is the first ancestor where node 15
#     is a right child.
#   - The function continues up to node 20, where node 10 is the left child, so
#     node 20 is returned as the successor.
#   - The in-order successor of node 15 is node 20.
#
