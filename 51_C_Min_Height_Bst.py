# Problem Statement:
# Given a sorted array, construct a Binary Search Tree (BST) such that the tree has minimal height.
# A BST is a binary tree where the value of each node is greater than all the nodes in its left subtree 
# and smaller than all the nodes in its right subtree. The goal is to maintain balance in the tree by 
# ensuring that the tree’s height is as small as possible.
# This is achieved by selecting the middle element of the current (sub)array as the root or subtree root 
# during each recursive step to divide the array into two halves: left and right subtrees.

# Approach for Current Code:
# 1. The `minHeightBst` function initializes the process by calling the `constructMinHeightBst` function 
#    with the entire array and appropriate start and end indices.
# 
# 2. In `constructMinHeightBst`, the middle element of the current subarray is selected and becomes the root 
#    (or subtree root) to maintain a balanced tree structure.
# 
# 3. The function recursively constructs the left and right subtrees by assigning the left subtree to 
#    `bst.left` and the right subtree to `bst.right`. This is done by recursively calling 
#    `constructMinHeightBst` for the left and right halves of the array.
#
# 4. The base case occurs when the start index becomes greater than the end index, meaning there are no more 
#    elements to process in that subarray, and the recursion terminates.
#
# 5. The final result is a balanced BST with minimal height, where the root is the middle element of the 
#    array, and each subtree is similarly balanced by recursively selecting middle elements.




def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)


def constructMinHeightBst(array, startIdx, endIdx):
    # Base case: if end index is less than start index, stop the recursion
    if endIdx < startIdx:
        return None

    midIdx = (startIdx + endIdx) // 2
    # Create a new BST node for the middle element
    bst = BST(array[midIdx])

    # Recursively construct the left and right subtrees
    bst.left = constructMinHeightBst(array, startIdx, midIdx - 1)
    bst.right = constructMinHeightBst(array, midIdx + 1, endIdx)
    
    return bst


# Class to represent a node in the Binary Search Tree (BST)
class BST:
    def __init__(self, value):
        # Initialize the node with the given value and set left and right children to None
        self.value = value
        self.left = None
        self.right = None

    # Method to print the structure of the BST
    def log_structure(self):
        # Log the value of the current node
        print(f"BST {{\n  value: {self.value},")

        # Log the left subtree
        if self.left:
            print(f"  left: ", end="")
            self.left.log_structure()
        else:
            print("  left: null,")

        # Log the right subtree
        if self.right:
            print(f"  right: ", end="")
            self.right.log_structure()
        else:
            print("  right: null")

        # Close the current node structure
        print("}")

    # Method to perform an in-order traversal and return the values
    def in_order_traversal(self):
        elements = []
        # Recursively traverse the left subtree first
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit the current node
        elements.append(self.value)

        # Recursively traverse the right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


# Dummy data to test the function
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

# Creating the minimal height BST from the sorted array
bst = minHeightBst(array)

# Printing the BST structure to log
bst.log_structure()

# Printing the BST in ascending order to verify correctness
print("\nIn-order traversal of the BST:", bst.in_order_traversal())


