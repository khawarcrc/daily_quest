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
# 1. A Binary Search Tree (BST) class is defined with an initializer method (__init__) to represent each node.
#    Each node contains a value, a left child (left subtree), and a right child (right subtree).

# 2. The 'reconstructBst' function is defined, which takes a list of pre-order traversal values as input.
#    This function is responsible for reconstructing a BST from the given pre-order traversal values.

# 3. The base case for recursion is set: if the input list is empty, return None, indicating no subtree to be constructed.

# 4. The first value in the list represents the root node of the BST, as per the pre-order traversal definition
#    (Root -> Left Subtree -> Right Subtree). This value becomes the current root node of the BST.

# 5. A variable 'rightSubtreeRootIndex' is initialized, assuming that the right subtree starts at the end of the list by default.
#    This variable will be used to determine the starting index of the right subtree.

# 6. The function iterates over the remaining values in the list (after the root node) to find the first value greater than or 
#    equal to the root node. This marks the start of the right subtree (since values in the right subtree are always greater 
#    than or equal to the root in a BST).

# 7. Once the index for the right subtree is found, the function recursively calls itself to construct the left subtree using
#    the values before 'rightSubtreeRootIndex'. These values represent the left subtree in the pre-order traversal.

# 8. Similarly, the function recursively calls itself to construct the right subtree using the values starting from 
#    'rightSubtreeRootIndex'. These values represent the right subtree in the pre-order traversal.

# 9. Once both the left and right subtrees are reconstructed, the function returns the root node with the reconstructed left 
#    and right subtrees attached.

# 10. Several test cases are created with predefined pre-order traversal values (preOrderTraversalValues1, 
#    preOrderTraversalValues2, preOrderTraversalValues3) to test the reconstruction function.

# 11. The 'reconstructBst' function is called for each test case to reconstruct the respective BSTs, which are stored in 
#    variables (bst1, bst2, bst3).

# 12. A helper function 'printInOrder' is defined to print the BST in in-order traversal (Left Subtree -> Root -> Right Subtree)
#    for verifying correctness. This function recursively traverses the tree and prints node values in ascending order.

# 13. The 'printInOrder' function is called for each reconstructed BST (bst1, bst2, bst3) to print their in-order traversal.
#    This helps in verifying that the BSTs were correctly reconstructed based on the given pre-order traversal input.


class BST:
    def __init__(self, value, left=None, right=None):
        # Initialize a node with value, left child, and right child
        self.value = value
        self.left = left
        self.right = right

# Function to reconstruct the BST from the preorder traversal values
def reconstructBst(preOrderTraversalValues):
    # Base case: if the list is empty, return None (no subtree)
    if len(preOrderTraversalValues) == 0:
        return None

    # The first value in the preorder list is the root of the BST
    currentValue = preOrderTraversalValues[0]
    
    # Index for the start of the right subtree; assume it starts at the end of the list
    rightSubtreeRootIndex = len(preOrderTraversalValues)

    # Find the index where the right subtree begins (where values are >= current root value)
    for index in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[index]
        if value >= currentValue:
            rightSubtreeRootIndex = index
            break

    # Recursively reconstruct the left subtree from values before rightSubtreeRootIndex
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIndex])
    
    # Recursively reconstruct the right subtree from values starting at rightSubtreeRootIndex
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIndex:])

    # Return the constructed BST node with left and right subtrees
    return BST(currentValue, leftSubtree, rightSubtree)

# Helper function to print the BST structure in a readable format
def printBst(node, level=0, side="root"):
    if node is not None:
        print("    " * level + f"{side}: {node.value}")
        printBst(node.left, level + 1, "left")
        printBst(node.right, level + 1, "right")

# Dummy data: Preorder traversal values of a BST
preOrderTraversalValues = [10, 5, 2, 1, 5, 13, 14, 12]

# Reconstruct the BST from the preorder traversal
constructedBst = reconstructBst(preOrderTraversalValues)

# Print the constructed BST
printBst(constructedBst)




