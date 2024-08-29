# Evaluate Expression Tree
# 1. **Tree Node Definition:
# ** The `BinaryTree` class defines a node in the binary tree, where each node has a value and optional left and right children.

# 2. **Base Case Evaluation:
# ** In the `evaluateExpressionTree` function, if the node's value is non-negative, it is a leaf node representing a number, so the function returns that number directly.

# 3. **Recursive Evaluation:
# ** For nodes with negative values, the function recursively evaluates the left and right subtrees to compute their results.

# 4. **Operation Execution:
# ** Depending on the node's value, the function performs a specific mathematical operation (addition, subtraction, division, or multiplication) on the results from the left and right subtrees.

# 5. **Expression Evaluation:
# ** The function evaluates the entire binary tree from the bottom up, using recursion to combine the results of sub-expressions until the full expression's result is computed and printed.

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        # Initialize the binary tree node with value and optional left and right children
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Base case: If the value is non-negative, it's a number; return it directly
    if tree.value >= 0:
        print(f"Reached leaf node with value: {tree.value}")
        return tree.value

    # Recursively evaluate the left and right subtrees
    print(f"Evaluating left subtree of node with value {tree.value}")
    leftValue = evaluateExpressionTree(tree.left)
    
    print(f"Evaluating right subtree of node with value {tree.value}")
    rightValue = evaluateExpressionTree(tree.right)

    # Perform the operation based on the current node's value
    if tree.value == -1:  # Addition
        result = leftValue + rightValue
        print(f"Performing addition: {leftValue} + {rightValue} = {result}")
        return result
    if tree.value == -2:  # Subtraction
        result = leftValue - rightValue
        print(f"Performing subtraction: {leftValue} - {rightValue} = {result}")
        return result
    if tree.value == -3:  # Division
        result = int(leftValue / rightValue)  # Using int() for integer division
        print(f"Performing division: {leftValue} / {rightValue} = {result}")
        return result
    if tree.value == -4:  # Multiplication
        result = leftValue * rightValue
        print(f"Performing multiplication: {leftValue} * {rightValue} = {result}")
        return result

# Dummy data for code execution

# Example expression: (((2 * 3) - 2) + (8 / 3))
# Binary Tree representation:
#            -1
#          /     \
#        -2       -3
#       /  \     /  \
#     -4    2   8    3
#    /  \
#   2    3

# Constructing the tree
tree = BinaryTree(
    -1,  # Addition
    BinaryTree(
        -2,  # Subtraction
        BinaryTree(
            -4,  # Multiplication
            BinaryTree(2),  # Left child (2)
            BinaryTree(3)   # Right child (3)
        ),
        BinaryTree(2)  # Subtraction right child (2)
    ),
    BinaryTree(
        -3,  # Division
        BinaryTree(8),  # Left child (8)
        BinaryTree(3)   # Right child (3)
    )
)

# Evaluate the expression tree
result = evaluateExpressionTree(tree)
print(f"\nFinal result of expression tree evaluation: {result}")
