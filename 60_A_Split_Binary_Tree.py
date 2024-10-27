# Problem Statement:
# ------------------
# Given a binary tree, the goal is to determine if it can be split into two subtrees
# with equal sums. If such a split is possible, return the sum of each resulting subtree;
# otherwise, return 0. A "split" in this context means that one of the subtrees has a sum
# equal to exactly half the total sum of the entire tree.
#
# Approach:
# ---------
# 1. First, calculate the total sum of all nodes in the tree using a helper function (`getTreeSum`).
#    If this sum is odd, it's impossible to split the tree into two equal parts, so return 0 immediately.
# 2. If the sum is even, we proceed with a target split sum, which is half the total.
# 3. The `trySubTrees` function is used to traverse the tree recursively, calculating the sum of each subtree
#    to see if any subtree’s sum equals the target split sum.
# 4. During traversal, each node's subtree sum (including itself) is calculated, and a check is performed
#    to see if it matches the target split sum.
# 5. If such a subtree is found, the function returns `True` indicating the tree can be split, and
#    the main function returns the target split sum. Otherwise, it returns 0, meaning no equal split is possible.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    # """
    # Attempts to split the binary tree into two subtrees with equal sums.
    # - Calculates the total sum of the tree.
    # - Checks if there exists a subtree that sums to half of the total.
    # - Returns the half sum if such a split is possible, otherwise returns 0.
    # """
    totalSum = getTreeSum(tree)  # Calculate total sum of tree
    # If the total sum is odd, it cannot be split equally
    if totalSum % 2 != 0:
        return 0

    # Set the target sum for a subtree to achieve an equal split
    desiredSubTreeSum = totalSum / 2

    # Use trySubTrees to recursively check each subtree.
    # This will return two values:
    #   - The sum of each subtree explored
    #   - A boolean (canBeSplit) indicating if any subtree matches the target split sum
    _, canBeSplit = trySubTrees(tree, desiredSubTreeSum)

    return desiredSubTreeSum if canBeSplit else 0


def trySubTrees(tree, desiredSubTreeSum):
    # """
    # Recursive function to calculate the sum of each subtree and check if any subtree
    # matches the desired split sum.
    # - Returns the sum of the current subtree and a boolean indicating if a split is found.
    # """
    if tree is None:
        return 0, False

    leftSum, leftCanBeSplit = trySubTrees(
        tree.left, desiredSubTreeSum
    )  # Left subtree sum
    rightSum, rightCanBeSplit = trySubTrees(
        tree.right, desiredSubTreeSum
    )  # Right subtree sum

    # Calculate the sum of the current tree including left and right subtrees
    currentTreeSum = tree.value + leftSum + rightSum
    # Check if this tree can be split at the desired sum
    canBeSplit = (
        leftCanBeSplit or rightCanBeSplit or (currentTreeSum == desiredSubTreeSum)
    )
    return currentTreeSum, canBeSplit


def getTreeSum(tree):
    # """
    # Helper function to calculate the total sum of the tree recursively.
    # """
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)


# Dummy Data
# Creating a binary tree:
#       10
#      /   \
#     5     15
#    / \    /
#   2   3  7
root = BinaryTree(10)
root.left = BinaryTree(5, BinaryTree(2), BinaryTree(3))
root.right = BinaryTree(15, BinaryTree(7))

# Testing splitBinaryTree function
result = splitBinaryTree(root)
print("The sum of the split subtree is:", result)
