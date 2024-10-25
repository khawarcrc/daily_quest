# """
# Problem Statement:
# The goal is to implement a function called `findSuccessor` that finds the in-order successor of a given node in a binary tree.
# The in-order successor of a node in a binary tree is the next node that would be visited in an in-order traversal.
# In an in-order traversal, nodes are visited in the following order: left subtree, root, then right subtree. 
# The function should return the in-order successor if it exists, or `None` 
# if the node has no successor (i.e., it is the last node in the traversal).

# To achieve this, a helper function `getInOrderTraversalOrder` is used to traverse the binary tree and collect nodes in in-order sequence.
# This function helps identify the exact in-order position of the target node, enabling the determination of its successor.

# Theory and Execution Flow:
# 1. BinaryTree Class Initialization:
#     - Each node in the binary tree has a `value` to store the data, `left` and `right` pointers for child nodes,
#     and a `parent` pointer for tracking its parent node. The `parent` pointer enables upward traversal,
#     which can be useful in some binary tree operations.

# 2. findSuccessor Function:
#    - Purpose: Determines the in-order successor of a given node.
#    - Process:
#         - Calls the helper function `getInOrderTraversalOrder`, which performs an in-order traversal of the tree, creating an ordered list of nodes.
#         - The function then iterates through this list to locate the specified node.
#         - If the node is found, it checks if this node is the last node in the traversal list. If so, the function returns `None` as there is no successor.
#         - Otherwise, it returns the next node in the list as the in-order successor.
#     - Expected Output: The function outputs the successor node if it exists, or `None` if there is no successor 
#     (i.e., the node is the last one in in-order traversal).

# 3. getInOrderTraversalOrder Function:
#     - Purpose: Performs an in-order traversal of the binary tree and records the nodes in a list in ascending order.
#     - Process:
#         - This function accepts the root of the binary tree and an optional list (`order`) to hold nodes in in-order sequence.
#         - Traversal Steps:
#             1. It first recursively traverses the left subtree to reach the leftmost node.
#             2. Then, it appends the current node to the `order` list.
#             3. Finally, it recursively traverses the right subtree.
#         - This recursive approach ensures nodes are stored in an ordered sequence: left subtree, root, and right subtree.
#     - Expected Output: A list of nodes ordered by in-order traversal. This list is critical for finding the position of the given node
#     and determining its successor.

# """





class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        # Initialize the Binary Tree node with value and optional left, right, and parent nodes
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    """
    Finds the in-order successor of a given node in a binary tree.
    
    Parameters:
    - tree: The root node of the binary tree.
    - node: The node for which the successor is to be found.
    
    Returns:
    - The in-order successor node if it exists, otherwise None.
    """
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)

    # Traverse through the list of nodes to find the given node and its successor
    for index, currentNode in enumerate(inOrderTraversalOrder):
        if currentNode != node:
            continue
        
        # If the node is the last in the traversal, there's no successor
        if index == len(inOrderTraversalOrder) - 1:
            return None

        # Return the next node in the traversal order as the successor
        return inOrderTraversalOrder[index + 1]


def getInOrderTraversalOrder(node, order=None):
    """
    Traverses the binary tree in in-order and records the nodes in a list.
    
    Parameters:
    - node: The current node being traversed.
    - order: A list to store the nodes in in-order sequence.
    
    Returns:
    - A list of nodes in in-order sequence.
    """
    if order is None:
        order = []
    
    if node is None:
        return order

    # Recursively traverse the left subtree
    getInOrderTraversalOrder(node.left, order)
    
    # Visit the current node
    order.append(node)
    
    # Recursively traverse the right subtree
    getInOrderTraversalOrder(node.right, order)
    
    return order


# Creating dummy data for testing
# Structure:
#       10
#      /  \
#     5    15
#    / \   / \
#   2   5 13  22
#            /
#           14

root = BinaryTree(10)
root.left = BinaryTree(5, parent=root)
root.right = BinaryTree(15, parent=root)
root.left.left = BinaryTree(2, parent=root.left)
root.left.right = BinaryTree(5, parent=root.left)
root.right.left = BinaryTree(13, parent=root.right)
root.right.right = BinaryTree(22, parent=root.right)
root.right.left.right = BinaryTree(14, parent=root.right.left)

# Test the findSuccessor function
# Find the successor of the node with value 13
node = root.right.left  # Node with value 13
successor = findSuccessor(root, node)

# Print the value of the successor if it exists
if successor:
    print(f"The successor of node with value {node.value} is {successor.value}.")
else:
    print(f"The node with value {node.value} has no successor.")
