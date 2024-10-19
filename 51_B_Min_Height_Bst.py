# Problem Statement:
# Given a sorted array, construct a Binary Search Tree (BST) such that the tree has minimal height. 
# A BST is a binary tree where the value of each node is greater than all the nodes in its left subtree 
# and smaller than all the nodes in its right subtree. The goal is to maintain balance in the tree by 
# ensuring that the tree’s height is as small as possible. This is done by always inserting the middle 
# element of the current (sub)array as the root or subtree root to divide the array into two parts 
# (left and right subtree).

# The algorithm should:
# 1. Find the middle element of the current array/subarray.
# 2. Add it as the root (or subtree root) of the current BST.
# 3. Recursively perform the same operation for the left half of the array (for the left subtree).
# 4. Recursively perform the same operation for the right half of the array (for the right subtree).
# 5. Continue this process until all elements are added to the BST.

# Execution Theory:
# 1. The `minHeightBst` function initializes the process by calling `constructMinHeightBst` 
#    with the full array and indices that cover the entire array (0 to len(array) - 1).
# 
# 2. The `constructMinHeightBst` function is where recursion occurs. This function takes the current 
#    subarray defined by `startIdx` and `endIdx`. It calculates the middle index of this subarray using 
#    (startIdx + endIdx) // 2. The middle element is the "best choice" to become the current root or 
#    subtree root to minimize height.
# 
# 3. Once the middle element is selected, it is inserted into the BST:
#    - If the `bst` is `None` (initial root), the middle element becomes the root of the tree.
#    - Otherwise, the new element is attached to either the left or right subtree of the current BST node 
#      based on comparison with the current node's value.
# 
# 4. After the current node is inserted, the function recursively processes the left and right halves of the 
#    array:
#    - The left subtree is constructed by calling `constructMinHeightBst` with the left half of the array 
#      (`startIdx` to `midIdx - 1`).
#    - The right subtree is constructed by calling `constructMinHeightBst` with the right half of the array 
#      (`midIdx + 1` to `endIdx`).
# 
# 5. Recursion continues until the base case is reached: when `startIdx > endIdx`, meaning the subarray is 
#    empty, at which point the function returns, ending that branch of recursion.
# 
# 6. The recursion follows a depth-first approach, always selecting the middle element, inserting it into the 
#    tree, and then recursively building the left and right subtrees. The result is a balanced BST with minimal 
#    height, where the root is the middle element of the original array, and each subtree is similarly balanced.
# 
# Example Execution Flow:
# - For the array [1, 2, 5, 7, 10, 13, 14, 15, 22]:
#   1. The middle element is `10`, which becomes the root of the tree.
#   2. The left subtree is built from [1, 2, 5, 7]. The middle element `5` becomes the left child of `10`.
#   3. The right subtree is built from [13, 14, 15, 22]. The middle element `14` becomes the right child of `10`.
#   4. For the left subtree of `5`:
#      - The middle of [1, 2] is `2`, which becomes the left child of `5`.
#      - The middle of [7] is `7`, which becomes the right child of `5`.
#   5. For the right subtree of `14`:
#      - The middle of [13] is `13`, which becomes the left child of `14`.
#      - The middle of [15, 22] is `15`, which becomes the right child of `14`.
#   6. This recursive process builds the entire tree, ensuring that the height is minimized.


# this Approach:

# Direct Node Assignment: 
# Nodes are directly assigned to the left or right children of the current node 
# within the recursive function, avoiding the use of the insert() method.

# Explicit Recursion Control: 
# Recursion is managed manually in the constructMinHeightBst function, 
# with explicit left and right subtree construction.

# Manual BST Reference Update: 
# The bst reference is manually updated to the left or right child before each recursive call 
# to control subtree insertions.



def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)


def constructMinHeightBst(array, bst, startIdx, endIdx):
    # Base case: if end index is less than start index, stop the recursion
    if endIdx < startIdx:
        return

    # Calculate the middle index of the current array/subarray
    midIdx = (startIdx + endIdx) // 2

    # Create a new node with the middle element of the array
    newBstNode = BST(array[midIdx])

    # If this is the first node (bst is None), make this node the root of the BST
    if bst is None:
        bst = newBstNode
    else:
        # Attach the new node either to the left or right of the current BST node
        if array[midIdx] < bst.value:
            # If the mid element is smaller than the current BST node, attach it to the left
            bst.left = newBstNode
            # Move to the left subtree to continue building it
            bst = bst.left
        else:
            # If the mid element is larger, attach it to the right
            bst.right = newBstNode
            # Move to the right subtree to continue building it
            bst = bst.right

    # Recursively build the left subtree using the left half of the array
    constructMinHeightBst(array, bst, startIdx, midIdx - 1)

    # Recursively build the right subtree using the right half of the array
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)


# Class to represent a node in the Binary Search Tree (BST)
class BST:
    def __init__(self, value):
        # Initialize the node with the given value and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    # Method to insert a value into the BST
    def insert(self, value):
        # If the value to be inserted is less than the current node's value
        if value < self.value:
            # If left child is empty, insert the new value here
            if self.left is None:
                self.left = BST(value)
            else:
                # Otherwise, recursively insert it into the left subtree
                self.left.insert(value)
        else:
            # If the value is greater or equal, insert into the right subtree
            if self.right is None:
                self.right = BST(value)
            else:
                # Recursively insert it into the right subtree
                self.right.insert(value)


# Dummy data to test the function
# Sorted array
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

# Creating the minimal height BST from the sorted array
bst = minHeightBst(array)

# The resulting BST will have a balanced structure with minimal height
