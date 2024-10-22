# """
# Problem Statement:
# ------------------
# You are given a list of integers representing the pre-order traversal of a Binary Search Tree (BST).
# Your task is to reconstruct the BST from this pre-order traversal and return the root of the constructed tree.

# Pre-order traversal follows the order:
# 1. Visit the root node.
# 2. Recursively visit the left subtree.
# 3. Recursively visit the right subtree.

# Theory to Solve the Problem:
# ----------------------------
# 1. **Base Case**:
#    - If the list of pre-order values is empty, the function should return `None`, indicating the current subtree is empty.

# 2. **Identify the Root**:
#    - The first element in the pre-order traversal is always the root of the current subtree.

# 3. **Finding the Boundary Between Subtrees**:
#    - Traverse through the list to find the first value greater than or equal to the root. This marks the start of the right subtree.
#    - The elements before this value form the left subtree, while the elements from this point form the right subtree.

# 4. **Recursive Subtree Construction**:
#    - Use recursion to construct the left and right subtrees:
#      a) The left subtree is built using the values smaller than the root.
#      b) The right subtree is built using the values greater than or equal to the root.

# 5. **Recursion Breakdown**:
#    - The function recursively builds the left and right subtrees until all subtrees are constructed, combining them into the final BST.

# 6. **Time and Space Complexity**:
#    - Worst-case time complexity is O(n^2) when the tree is skewed, and O(n log n) for a balanced tree.
#    - Space complexity is O(n) due to the recursion stack used during construction.
# """


class BST:
    def __init__(self, value, left=None, right=None):
        # Initialize a node with value, left child, and right child
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Base case: if the list is empty, return None (no subtree)
    if len(preOrderTraversalValues) == 0:
        return None

    # The first value in the preorder list is the root of the BST
    currentValue = preOrderTraversalValues[0]
    
    # Index for the start of the right subtree; assume it starts at the end of the list
    rightSubtreeRootIdx = len(preOrderTraversalValues)

    # Find the index where the right subtree begins (where values are >= current root value)
    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubtreeRootIdx = idx
            break

    # Recursively reconstruct the left subtree from values before rightSubtreeRootIdx
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    
    # Recursively reconstruct the right subtree from values starting at rightSubtreeRootIdx
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])

    # Return the constructed BST node with left and right subtrees
    return BST(currentValue, leftSubtree, rightSubtree)


# Dummy data: pre-order traversal of a BST
preOrderTraversalValues = [10, 5, 2, 5, 13, 11, 15]

# Reconstruct BST from the pre-order traversal values
bst = reconstructBst(preOrderTraversalValues)

# Helper function to print BST in-order for checking correctness
def printInOrder(node):
    if node is not None:
        printInOrder(node.left)
        print(node.value, end=" ")
        printInOrder(node.right)

# Print the BST in in-order to verify the result
printInOrder(bst)
