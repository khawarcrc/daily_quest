
# # Problem Statement:

# You are required to implement a Binary Search Tree (BST) data structure in Python that supports the following operations:
# 1. Insertion of a new key into the BST.
# 2. Checking whether a specific key exists in the BST.
# 3. Deletion of a specified key from the BST.
# 4. Traversing the BST in inorder to return a sorted list of keys.

# The BST must handle edge cases, including preventing duplicate key insertions,
# handling deletion from an empty tree, and dealing with nodes that have one or two children. 
# The implementation should ensure correct time complexity for each operation and prepare for future improvements like tree balancing.


# # Complete Theory of the Code:

# 1. **TreeNode Class**:
#    - The `TreeNode` class represents each node of the Binary Search Tree (BST).
#    - It contains the following attributes:
#      - `key`: Stores the value of the node, which is used for comparisons.
#      - `left`: Points to the left child of the node, initialized as `None` (indicating no left child).
#      - `right`: Points to the right child of the node, initialized as `None` (indicating no right child).
#    - Each node is part of the BST and maintains the tree's structure, where the left child holds smaller 
#       values than the node’s key, and the right child holds larger values.

# 2. **BinarySearchTree Class**:
#    - The `BinarySearchTree` class manages the overall tree, starting with the `root`, which represents the top node of the BST.
#    - The `root` is initialized as `None` to indicate an empty tree when the object is first created.
#    - The class includes methods for inserting keys, searching for keys, deleting keys, and traversing the tree in order.

# 3. **Insert Operation**:
#    - The `insert` method allows the insertion of new keys into the BST, maintaining the binary search tree property:
#      - All keys in the left subtree of a node are smaller than the node’s key.
#      - All keys in the right subtree of a node are larger than the node’s key.
#    - The insertion begins by checking if the tree is empty:
#      - If `root` is `None`, the new node becomes the root.
#      - If the tree is not empty, the method recursively traverses down the tree to find the correct position for the new node.
#    - The method compares the new key with the current node's key:
#      - If the new key is smaller, it proceeds to the left subtree.
#      - If the new key is larger, it proceeds to the right subtree.
#      - Duplicate keys are not inserted to maintain the uniqueness of keys in the tree.

# 4. **Contains (Search) Operation**:
#    - The `contains` method checks whether a specific key exists in the BST.
#    - It follows a binary search approach, starting from the root and recursively moving through the tree:
#      - If the key matches the current node’s key, the method returns `True`, indicating that the key exists in the tree.
#      - If the key is smaller than the current node’s key, the method moves to the left subtree.
#      - If the key is larger, it moves to the right subtree.
#    - If the method reaches a `None` node (i.e., a leaf node with no children), it returns `False`, indicating that the key is not present in the tree.

# 5. **Delete Operation**:
#    - The `delete` method removes a specified key from the BST while preserving its structure.
#    - The deletion process handles three cases:
#      1. **Node is a Leaf**: If the node to be deleted has no children, it is simply removed by returning `None` from the recursive call.
#      2. **Node has One Child**: If the node has only one child, the node is replaced by its child.
#      3. **Node has Two Children**: If the node has two children, the method finds the inorder successor (the smallest node in the right subtree)
#         - replaces the node’s key with the successor’s key, and then deletes the successor node. This ensures that the tree remains valid after deletion.
#    - The method checks for an empty tree (`root` is `None`) before attempting deletion, and if the key is not found, the tree remains unchanged.

# 6. **Inorder Traversal**:
#    - The `inorder_traversal` method returns the keys of the BST in ascending order.
#    - This method performs an inorder traversal, which is a depth-first traversal method:
#      - First, the left subtree is visited recursively.
#      - Then the current node’s key is added to the result list.
#      - Finally, the right subtree is visited recursively.
#    - This traversal ensures that the keys are returned in sorted order because of the BST's structure, where left nodes are smaller, and right nodes are larger.

# 7. **Edge Case Handling**:
#    - The implementation is designed to handle several edge cases, such as:
#      - **Empty Tree**: If the tree is empty (i.e., `root` is `None`), methods like `delete` and `contains` handle this case gracefully without causing errors.
#      - **Duplicate Keys**: The `insert` method prevents the insertion of duplicate keys to maintain the BST's unique key property.
#      - **Single Node Tree**: The `delete` method handles cases where the root is the only node in the tree, correctly deleting the root and setting the tree back to an empty state.
#      - **Deleting Root Node**: When deleting the root node with two children, the inorder successor is found and the root is replaced, maintaining the tree’s structure.

# 8. **Time Complexity**:
#    - **Insert**: O(log n) on average, assuming the tree is balanced, as the method recursively traverses the tree to find the correct position. However, the time complexity degrades to O(n) in the worst case if the tree becomes unbalanced and degenerates into a linked list.
#    - **Search (Contains)**: O(log n) on average, as the method performs a binary search. In the worst case, it becomes O(n) for an unbalanced tree.
#    - **Delete**: O(log n) on average, similar to insertion and search. The time complexity depends on the height of the tree, which can be O(n) in the worst case for an unbalanced tree.
#    - **Inorder Traversal**: O(n), as the method must visit every node in the tree to return the keys in sorted order.

# 9. **Space Complexity**:
#    - The space complexity of each method is O(h), where `h` is the height of the tree. This is due to the recursive nature of the methods, as each recursive call adds a frame to the call stack. In the worst case, the height can be `n` (for an unbalanced tree), leading to O(n) space complexity.

# 10. **Potential Improvements**:
#    - **Balancing the Tree**: In its current state, the BST is not balanced, which means that operations can degrade to O(n) in the worst case (e.g., if the tree degenerates into a linked list). To improve this, self-balancing mechanisms such as AVL trees or Red-Black trees could be implemented.
#    - **Threaded BST**: To improve traversal performance, a threaded BST could be considered, where null pointers are used to point to inorder successors, thus speeding up traversal operations without recursion.
#    - **Additional Operations**: Future implementations could add more operations such as finding the height of the tree, printing the tree structure, or balancing it on insertion and deletion (e.g., AVL rotations).

# """




class TreeNode:
    def __init__(self, key):
        # Initialize node with key, and left and right children
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        # Initialize root as None
        self.root = None

    def insert(self, key):
        # """
        # Inserts a new key into the BST, avoiding duplicates.
        # Time complexity: O(log n) on average, O(n) in the worst case (unbalanced)
        # """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        # Recursively find the correct place to insert the key
        if key == node.key:
            return  # Prevent duplicate key insertion
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def contains(self, key):
        # """
        # Checks if a key is in the BST.
        # Time complexity: O(log n) on average, O(n) in the worst case (unbalanced)
        # """
        return self._contains(self.root, key)

    def _contains(self, node, key):
        # Recursively search for the key
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else:
            return self._contains(node.right, key)

    def delete(self, key):
        # """
        # Deletes a key from the BST, handling edge cases.
        # Time complexity: O(log n) on average, O(n) in the worst case (unbalanced)
        # """
        if self.root is None:
            return  # Handle deletion from an empty tree
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # Recursively find the node to delete
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        # Find the node with the smallest key (leftmost leaf)
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        # """
        # Returns the inorder traversal of the BST.
        # Time complexity: O(n) where n is the number of nodes
        # """
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        # Inorder traversal (left-root-right)
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result


# Usage example with improvements
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:", bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]
print("Contains 40:", bst.contains(40))  # Output: True
print("Contains 100:", bst.contains(100))  # Output: False

# Deletion operations with edge case handling
bst.delete(20)
print("Inorder Traversal after deleting 20:", bst.inorder_traversal())  # Output: [30, 40, 50, 60, 70, 80]

bst.delete(30)
print("Inorder Traversal after deleting 30:", bst.inorder_traversal())  # Output: [40, 50, 60, 70, 80]

bst.delete(50)
print("Inorder Traversal after deleting 50:", bst.inorder_traversal())  # Output: [40, 60, 70, 80]
