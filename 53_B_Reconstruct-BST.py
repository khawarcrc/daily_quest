
# Problem Statement:
# ------------------
# You are given an array that represents the preorder traversal of a binary search tree (BST).
# Your task is to reconstruct the original BST from this preorder traversal.
# Preorder traversal visits nodes in the order: root, left subtree, right subtree.
# Given the preorder traversal values, construct the BST and verify its structure by printing the in-order traversal of the tree.

# Execution Flow with Deeper Concepts:
# ----------------------------------------------
# 1. Class Definitions:
#    - **BST Class**: Represents a single node in the BST with three attributes:
#      - `value`: The value of the node.
#      - `left`: A reference to the left child node.
#      - `right`: A reference to the right child node.
#    - **TreeInfo Class**: Used to encapsulate the current index of the root in the preorder array.
#      - It acts as a mutable container, allowing tracking across recursive calls without needing to return or pass the index explicitly.

# 2. Initialization:
#    - In `reconstructBst`, an instance of `TreeInfo` is created, initialized with a `rootIndex` of `0`.
#    - This instance will be modified throughout the recursive reconstruction process to point to the next node to be processed in the preorder array.

# 3. Recursive Tree Construction:
#    - **Function Call Structure**: 
#      - The main function (`reconstructBst`) calls the recursive helper function (`reconstructBstFromRange`) 
#        with initial bounds set to negative and positive infinity.
#    - **Base Case**: 
#      - The base case checks if the current index (`rootIndex`) has reached the length of the preorder array.
#        If it has, the function returns `None`, indicating that there are no more nodes to process.
#    - **Value Extraction**:
#      - The root value for the current subtree is extracted from `preOrderTraversalValues` using `currentSubtreeInfo.rootIndex`.
#    - **Bounds Checking**: 
#      - Before proceeding to create a node, the code checks if the root value is within the specified bounds.
#        If not, it returns `None` to signify that this path in the tree cannot be constructed.

# 4. Recursive Subtree Construction:
#    - If the root value is valid:
#      - The `rootIndex` is incremented to move to the next value in the preorder array for subsequent recursive calls.
#      - **Left Subtree**: A recursive call is made to construct the left subtree, 
#        with updated bounds (the left bound stays the same, and the upper bound is the current root value).
#      - **Right Subtree**: Another recursive call is made for the right subtree, 
#        where the lower bound is updated to the current root value, and the upper bound remains the same.
#    - Each recursive call returns a `BST` node that becomes the child of the current node being constructed.

# 5. Completion and Verification:
#    - After reconstructing the tree, the `printInOrder` function is called to traverse the tree in-order:
#      - This traversal method recursively visits the left subtree, then the current node, and finally the right subtree.
#      - Since the values of the BST are organized based on the properties of binary search trees, 
#        this traversal will print the node values in sorted order.

# Key Execution Concepts:
# -----------------------
# - **Mutability of Object Instances**:
#   - The `TreeInfo` instance is passed by reference, allowing its `rootIndex` to be modified across recursive calls without losing state.

# - **Recursion and Call Stack**:
#   - Each call to `reconstructBstFromRange` adds a new layer to the call stack, which helps manage the current state of `rootIndex`, bounds, and the reconstructed subtree.

# - **Tree Structure**:
#   - Understanding how the left and right subtrees are constructed and how they relate back to the parent node is crucial for grasping the overall structure of the reconstructed BST.


# Big O Complexity:
# -----------------
# Time Complexity: O(n), where n is the number of nodes (or the length of the preorder array).
# This is because each node is processed once during the recursive reconstruction.
#
# Space Complexity: O(n), due to the recursion stack and the storage of the BST nodes.
# In the worst case, the recursion stack depth will be equal to the height of the tree, which can be O(n) in the case of a skewed tree.

class BST:
    # Constructor for each node of the BST
    def __init__(self, value, left=None, right=None):
        self.value = value  # Value of the node
        self.left = left    # Left child of the node
        self.right = right  # Right child of the node


class TreeInfo:
    # Class to keep track of the root index while reconstructing the tree
    def __init__(self, rootIndex):
        self.rootIndex = rootIndex  # Index of the root in the preorder traversal


def reconstructBst(preOrderTraversalValues):
    # Initializes the TreeInfo object and calls the recursive function to reconstruct the tree
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(
        float("-inf"),  # Lower bound for the first root (smallest possible value)
        float("inf"),   # Upper bound for the first root (largest possible value)
        preOrderTraversalValues, 
        treeInfo
    )


def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    # Base case: If all elements from the preorder array are processed, return None
    if currentSubtreeInfo.rootIndex == len(preOrderTraversalValues):
        return None

    # Get the value of the current root
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIndex]
    
    # If the value is out of the current bounds, return None (invalid subtree)
    if rootValue <= lowerBound or rootValue >= upperBound:
        return None

    # Move to the next root value in the preorder array
    currentSubtreeInfo.rootIndex += 1

    # Recursively construct the left and right subtrees
    leftSubtree = reconstructBstFromRange(
        lowerBound,      # Lower bound stays the same for left subtree
        rootValue,       # Upper bound for left subtree is the current root value
        preOrderTraversalValues, 
        currentSubtreeInfo
    )
    
    rightSubtree = reconstructBstFromRange(
        rootValue,       # Lower bound for the right subtree is the current root value
        upperBound,      # Upper bound stays the same for the right subtree
        preOrderTraversalValues, 
        currentSubtreeInfo
    )

    # Return the constructed BST with the current root, left subtree, and right subtree
    return BST(rootValue, leftSubtree, rightSubtree)


# Dummy data: Preorder traversal of a BST
preOrderTraversalValues = [10, 5, 2, 7, 15, 12, 20]

# Call the function to reconstruct the BST
bst = reconstructBst(preOrderTraversalValues)

# Function to print the tree in-order (helper to verify the tree structure)
def printInOrder(node):
    if node is None:
        return
    printInOrder(node.left)
    print(node.value, end=" ")
    printInOrder(node.right)

# Print the reconstructed tree in-order to verify
print("In-order traversal of the reconstructed BST:")
printInOrder(bst)
