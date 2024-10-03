# Problem Statement:
# Given a Binary Search Tree (BST) and a target value, write a function to find the closest 
# value to the target in the BST. The closest value is defined as the value with the smallest 
# absolute difference from the target. If there are multiple closest values, return any of them.

# Steps to Solve:
# 1. Define a helper function that takes the current node of the tree, the target value, 
#    and the current closest value as parameters.
#
# 2. Initialize the current node to the root of the BST.
#
# 3. Traverse the tree using a while loop until there are no more nodes to check:
#    - If the absolute difference between the target and the current closest value is greater 
#      than the absolute difference between the target and the current node's value, update 
#      the closest value to the current node's value.
#    
#    - If the target is less than the current node's value, move to the left child.
#    
#    - If the target is greater than the current node's value, move to the right child.
#    
#    - If the current node's value equals the target, return it as it is the closest possible value.
#
# 4. Return the closest value found after traversing the tree.




class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target): 
    # Call the helper function with the initial closest value as infinity
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest): 
    currentNode = tree
    # Traverse the tree until there are no nodes left to check
    while currentNode is not None: 
        print(f"Checking node with value: {currentNode.value}")
        # If the current node is closer to the target than the previous closest, update closest
        if abs(target - closest) > abs(target - currentNode.value): 
            closest = currentNode.value
            print(f"Updated closest to: {closest}")
        # Move to the left child if the target is smaller than the current node's value
        if target < currentNode.value: 
            currentNode = currentNode.left 
            print("Moving to the left child")
        # Move to the right child if the target is larger than the current node's value
        elif target > currentNode.value: 
            currentNode = currentNode.right 
            print("Moving to the right child")
        else: 
            # If the current node's value equals the target, it is the closest possible value
            print("Exact match found!")
            break 
    return closest                

# Example BST
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.right = BST(22)

# Example target
target = 12

# Function call to find the closest value in the BST
closest_value = findClosestValueInBst(root, target)
print(f"The closest value to {target} is {closest_value}")
