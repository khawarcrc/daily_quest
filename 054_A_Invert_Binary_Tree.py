# Problem Statement:
# The function 'invertBinaryTree' is designed to invert a given binary tree.
# Inverting a binary tree means swapping the left and right children of all nodes in the tree.
# The function processes the tree using a breadth-first search (BFS) approach (using a queue).
# Each node's left and right child are swapped.
# The function 'swapLeftAndRight' performs the actual swapping of left and right children.
# The tree is traversed level by level (BFS), and the nodes are inverted at each level.

# Steps of Execution:
# 1. Initialize a queue with the root node.
# 2. Loop while there are nodes in the queue:
#    a. Pop the first node from the queue (current node).
#    b. If the current node is not None, swap its left and right children.
#    c. Add the left and right children of the current node to the queue (if they exist).
# 3. Continue until the queue is empty, and the tree is fully inverted.
# 4. The function terminates when all nodes have been processed, resulting in an inverted tree.

# Time Complexity: O(n) where n is the number of nodes in the tree (since each node is visited once).
# Space Complexity: O(n) for storing nodes in the queue.


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to invert the binary tree using BFS
def invertBinaryTree(tree):
    # Initialize the queue with the root node
    queue = [tree]

    # Continue while there are nodes in the queue
    while len(queue):
        # Pop the first node in the queue
        current = queue.pop(0)

        # If the current node is None, skip to the next iteration
        if current is None:
            continue

        # Swap the left and right children of the current node
        swapLeftAndRight(current)

        # Append the left and right children (if they exist) to the queue
        queue.append(current.left)
        queue.append(current.right)


# Function to swap the left and right child of a node
def swapLeftAndRight(tree):
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

# Print original binary tree (before inversion)
print("Original Binary Tree (Level-Order):")
printLevelOrder(root)
print("\n")

# Invert the binary tree
invertBinaryTree(root)

# Print the inverted binary tree (after inversion)
print("Inverted Binary Tree (Level-Order):")
printLevelOrder(root)

# Expected Inverted Binary Tree:
#         1
#       /   \
#      3     2
#     / \   / \
#    7   6 5   4