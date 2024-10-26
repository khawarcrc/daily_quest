
# Problem Statement:
# Given a binary tree, the task is to determine if the tree is symmetrical around its center.
# A binary tree is considered symmetrical if the left subtree is a mirror reflection of the right subtree.

# Code Execution Theory:
# - The function uses two stacks to compare nodes from the left and right subtrees.
# - It pops nodes from both stacks and checks for their values.
# - If both nodes are None, it continues to the next iteration.
# - If one node is None or the values of the nodes don't match, the function returns False.
# - The children of the left node are added in the order of left and right, 
#   while the children of the right node are added in reverse order (right and left) to maintain symmetry.
# - If the loop completes without returning False, the function returns True, indicating that the tree is symmetrical.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def symmetricalTree(tree):
    # Initialize two stacks for left and right subtrees
    stackLeft = [tree.left]
    stackRight = [tree.right]
    
    # Loop until there are no nodes left in the left stack
    while len(stackLeft) > 0:
        left = stackLeft.pop()  # Pop the left node from the stack
        right = stackRight.pop()  # Pop the right node from the stack
        
        # Check if both nodes are None (base case)
        if left is None and right is None:
            continue
        
        # If one node is None or their values don't match, return False
        if left is None or right is None or left.value != right.value:
            return False
        
        # Add left and right children of the left node to the stack
        stackLeft.append(left.left)
        stackLeft.append(left.right)
        # Add right and left children of the right node to the stack (note the order)
        stackRight.append(right.right)
        stackRight.append(right.left)
    
    return True  # Return True if the tree is symmetrical


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

