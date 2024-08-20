# Overall Process Explained in Points:

# 1. Initialize at the Root Node:
#    - Start the traversal from the root node of the BST.
#    - Set an initial closest value to infinity (float("inf")).

# 2. Traverse the Tree:
#    - Compare the target value with the current node's value.
#    - If the current node's value is closer to the target than the previously recorded closest value, update the closest value.

# 3. Decide the Direction of Traversal:
#    - Move to the left child if the target is smaller than the current node's value (since left child values are smaller).
#    - Move to the right child if the target is larger than the current node's value (since right child values are larger).

# 4. Handle Exact Match:
#    - If the current node's value matches the target exactly, it is the closest possible value, so terminate the search.

# 5. Return the Closest Value:
#    - After the traversal, return the closest value found during the search.



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
