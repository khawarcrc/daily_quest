# Class definition for a binary search tree (BST) node

# Problem Statement:
# Given a binary tree, determine if it is a valid Binary Search Tree (BST).
# A BST must satisfy the following conditions:
# 1. The left subtree of a node contains only nodes with values less than the node's value.
# 2. The right subtree of a node contains only nodes with values greater than the node's value.
# 3. Both the left and right subtrees must also be binary search trees.

# Complete theory of the code in steps:

# 1. **Binary Search Tree Definition**:
#    - A binary search tree (BST) is a binary tree in which each node has:
#      a) A value.
#      b) A left child (left subtree) where all the node values are smaller than the parent node's value.
#      c) A right child (right subtree) where all the node values are greater than the parent node's value.
#    - The task is to check whether a given binary tree follows these properties.

# 2. **Initial Setup**:
#    - We start by writing a function `validateBst(tree)` that takes the root of the tree as input.
#    - This function calls a helper function `validateBstHelper(tree, minValue, maxValue)` 
#      to recursively verify if the tree is valid.
#    - The initial valid range of the tree's values is set to negative infinity (-∞) and positive infinity (+∞).

# 3. **Recursive Validation**:
#    - The helper function `validateBstHelper` will perform the recursive check.
#    - The process involves the following key steps:
#      a) **Base Case**: If the node is `None` (i.e., a leaf node), we return `True` because an empty tree is valid.
#      b) **Check for BST Violation**: 
#         - If the current node's value is less than or equal to the minimum allowed value or 
#           greater than or equal to the maximum allowed value, it violates the BST property, 
#           so we return `False`.
#      c) **Recursive Case**: 
#         - First, we recursively check the left subtree by updating the maximum valid value to the 
#           current node's value (since the left subtree must contain values smaller than the node).
#         - Then, we recursively check the right subtree by updating the minimum valid value to the 
#           current node's value (since the right subtree must contain values greater than the node).
#      d) **Final Decision**: 
#         - Both left and right subtrees must be valid. If both recursive calls return `True`, 
#           the current subtree is a valid BST, and we return `True`.

# 4. **Edge Cases**:
#    - **Empty Tree**: If the tree is empty (`None`), it is considered a valid BST.
#    - **Single Node Tree**: A tree with just one node is always valid.
#    - **Duplicate Values**: BSTs typically do not allow duplicate values, but if duplicate values are allowed, 
#      they must appear on either the left or right subtree based on the defined constraint (left < node < right).

# 5. **Time Complexity**:
#    - The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
#    - This is because we need to visit each node exactly once to verify the BST property.

# 6. **Space Complexity**:
#    - The space complexity is O(h), where h is the height of the tree.
#    - This comes from the recursive call stack, which depends on the height of the tree. In the worst case, 
#      for a completely unbalanced tree, the height could be O(n), leading to O(n) space complexity.
#      For a balanced tree, the height is O(log n), leading to O(log n) space complexity.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to validate if a given binary tree is a binary search tree (BST)
def validateBst(tree):
    # Start the recursive check from the root of the tree
    # The tree must follow the condition: minValue < node.value < maxValue
    return validateBstHelper(tree, float("-inf"), float("inf"))

# Recursive helper function to validate the BST
def validateBstHelper(tree, minValue, maxValue):
    # Base case: if we reach a leaf node (None), it's valid by default
    if tree is None:
        return True
    
    # Check if the current node's value violates the BST property
    # Node's value must be strictly greater than minValue and less than maxValue
    if tree.value < minValue or tree.value >= maxValue:
        return False
    
    # Recursively validate the left subtree (all values should be < current node's value)
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    
    # Recursively validate the right subtree (all values should be > current node's value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


# Dummy data to test the function
# Constructing a valid BST:
#        10
#       /  \
#      5   15
#     / \   \
#    2   5  22

bst = BST(10)
bst.left = BST(5)
bst.right = BST(15)
bst.left.left = BST(2)
bst.left.right = BST(5)
bst.right.right = BST(22)

# Test the function
print(validateBst(bst))  # Output should be True since it's a valid BST
