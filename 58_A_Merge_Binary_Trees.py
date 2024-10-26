# Problem Statement:
# Given two binary trees, we need to merge them by adding the values of nodes 
# that overlap. If a node exists in only one of the trees, it will appear as it is 
# in the resulting tree. The merged tree should have each node's value as the sum 
# of the node values from the input trees wherever they overlap.

# Code Execution Theory:
# The function `mergeBinaryTrees` takes two binary tree nodes, `tree1` and `tree2`.
# - If either tree is None, we return the other tree, as there is nothing to merge.
# - Otherwise, we add the values of the nodes from `tree1` and `tree2`, storing the 
#   result in `tree1`.
# - We recursively call `mergeBinaryTrees` for the left and right child nodes of 
#   `tree1` and `tree2`.
# - The recursion ensures that all overlapping nodes are processed.
# - When the base case of reaching None for both nodes in the same position is met,
#   the recursion returns, building up the final merged tree from the bottom up.

# Complexity:
# - Time Complexity: O(n), where n is the minimum number of nodes in the two trees, 
#   since each node is visited once.
# - Space Complexity: O(h), where h is the height of the taller tree, due to the 
#   recursion stack.

# Define the TreeNode class to construct nodes for binary trees.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Function to merge two binary trees.
def mergeBinaryTrees(tree1, tree2):
    # Base case: if one of the trees is None, return the other tree.
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    # Add the values of tree1 and tree2 nodes.
    tree1.value += tree2.value

    # Recursively merge the left children of both trees.
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    
    # Recursively merge the right children of both trees.
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    
    # Return the merged tree rooted at tree1.
    return tree1

# Dummy data for testing the function.
# Tree 1
#      1
#     / \
#    3   2
#   /
#  5
tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)

# Tree 2
#      2
#     / \
#    1   3
#     \   \
#      4   7
tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)

# Merge the trees
merged_tree = mergeBinaryTrees(tree1, tree2)

# The merged tree should be:
#       3
#      / \
#     4   5
#    / \   \
#   5   4   7
