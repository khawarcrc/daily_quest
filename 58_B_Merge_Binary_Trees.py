# """
# Problem Statement:
# The goal is to merge two binary trees by adding the values of nodes that overlap in the two trees. If a node exists in
# one tree but not in the other, it will be directly added to the merged tree. The merge should be done in-place on the
# first tree (tree1), updating it with the combined values and structure of both trees.

# Code Execution Theory:
# 1. **Initialization**:
#    - We initialize two stacks, `tree1Stack` and `tree2Stack`, to help traverse tree1 and tree2 iteratively. Each stack
#      holds nodes from the respective tree at corresponding positions.
# 2. **Merging Nodes**:
#    - If `tree2` is `None`, return `tree1` as no merging is needed.
#    - Pop nodes from `tree1Stack` and `tree2Stack`.
#    - Add the values from `tree2Node` to `tree1Node`.
# 3. **Handling Left and Right Children**:
#    - For the left and right children of both trees, check if the child in `tree1Node` is `None`. If so, attach the child
#      from `tree2Node`.
#    - If both nodes exist, add them to the stack to process the subtree further.
# 4. **Return**:
#    - The modified `tree1` is returned as the merged tree.

# Example:
# Given:
# tree1 =      1                tree2 =      2
#            /   \                         /   \
#          3       2                     1       3
#         /                                 \       \
#        5                                   4       7

# Merged result:
#                 3
#               /   \
#             4       5
#            /           \
#          5             7
# """


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    # If the first tree node is None, return the second tree node (no merging required)
    if tree1 is None:
        return tree2

    # Initialize stacks to perform iterative tree merging
    tree1Stack = [tree1]
    tree2Stack = [tree2]

    # Loop until there are nodes left to process in tree1Stack
    while len(tree1Stack) > 0:
        # Pop nodes from both stacks for current position merging
        tree1Node = tree1Stack.pop()
        tree2Node = tree2Stack.pop()

        # If tree2Node is None, continue to next iteration (no node to merge)
        if tree2Node is None:
            continue

        # Merge the values of the nodes at the current position
        tree1Node.value += tree2Node.value

        # Check and merge the left child nodes
        if tree1Node.left is None:
            # Attach tree2's left node directly if tree1's left is None
            tree1Node.left = tree2Node.left
        else:
            # Otherwise, push both left nodes to the stack for further processing
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)

        # Check and merge the right child nodes
        if tree1Node.right is None:
            # Attach tree2's right node directly if tree1's right is None
            tree1Node.right = tree2Node.right
        else:
            # Otherwise, push both right nodes to the stack for further processing
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)

    # Return the modified tree1 as the merged tree
    return tree1


# Dummy data to demonstrate the merge function
tree1 = BinaryTree(1)
tree1.left = BinaryTree(3)
tree1.right = BinaryTree(2)
tree1.left.left = BinaryTree(5)

tree2 = BinaryTree(2)
tree2.left = BinaryTree(1)
tree2.right = BinaryTree(3)
tree2.left.right = BinaryTree(4)
tree2.right.right = BinaryTree(7)

# Merge trees and store the merged result in mergedTree
mergedTree = mergeBinaryTrees(tree1, tree2)
