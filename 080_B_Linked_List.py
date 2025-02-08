# Node class represents a single node in the doubly linked list
# Problem Statement:
# Implement a **Doubly Linked List (DLL)** data structure to efficiently manage a collection of nodes,
# where each node contains a value and two pointers: one pointing to the previous node and one to the next node.
# The goal is to provide functionality for common operations such as setting the head and tail of the list,
# inserting nodes at specific positions, inserting nodes before or after existing nodes, 
# removing nodes with specific values, and checking for the existence of a node with a given value.

# Complete Theory:
# 1. **Doubly Linked List Structure**:
#    - Each node in a DLL contains:
#      - A `value` representing the data stored in the node.
#      - A `prev` pointer referencing the previous node.
#      - A `next` pointer referencing the next node.
#    - The DLL maintains a reference to its `head` (first node) and `tail` (last node).

# 2. **Functional Requirements**:
#    - **setHead(node)**: Set a given node as the head of the list. If the list is empty, this node becomes both the head and tail.
#    - **setTail(node)**: Set a given node as the tail of the list. If the list is empty, this node becomes both the head and tail.
#    - **insertBefore(existingNode, newNode)**: Insert a new node before an existing node in the list.
#    - **insertAfter(existingNode, newNode)**: Insert a new node after an existing node in the list.
#    - **insertAtPosition(position, newNode)**: Insert a new node at a specified position (1-indexed) in the list.
#    - **removeNodesWithValue(value)**: Remove all nodes from the list that contain a specified value.
#    - **remove(node)**: Remove a specific node from the list and adjust pointers accordingly.
#    - **containsNodeWithValue(value)**: Check if any node in the list contains a specified value.

# 7. **Practical Use**:
#    - Doubly linked lists are ideal for scenarios requiring efficient bidirectional traversal and frequent insertions or deletions at arbitrary positions.
#    - Common use cases include managing navigation history, LRU caches, and dynamic data structures like deques.

class Node:
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.prev = None    # Pointer to the previous node
        self.next = None    # Pointer to the next node


# DoublyLinkedList class represents the entire doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Reference to the head (first node) of the list
        self.tail = None  # Reference to the tail (last node) of the list

    # Set the given node as the head of the list
    def setHead(self, node):
        if self.head is None:  # If the list is empty, set both head and tail
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)  # Otherwise, insert the node before the current head

    # Set the given node as the tail of the list
    def setTail(self, node):
        if self.tail is None:  # If the list is empty, set the head (which also sets the tail)
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)  # Otherwise, insert the node after the current tail

    # Insert a node before a given node
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return  # Prevent redundant operations
        self.remove(nodeToInsert)  # Remove the node if it already exists in the list
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert  # Update head if inserting at the start
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # Insert a node after a given node
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return  # Prevent redundant operations
        self.remove(nodeToInsert)  # Remove the node if it already exists in the list
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert  # Update tail if inserting at the end
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # Insert a node at a specific position
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)  # Insert at the head if position is 1
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)  # Insert before the node at the position
        else:
            self.setTail(nodeToInsert)  # If position is beyond the tail, set the node as tail

    # Remove all nodes with a specific value
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:  # Remove nodes matching the value
                self.remove(nodeToRemove)

    # Remove a specific node from the list
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next  # Update head if removing the first node
            if self.head is not None:
                self.head.prev = None
        if node == self.tail:
            self.tail = self.tail.prev  # Update tail if removing the last node
            if self.tail is not None:
                self.tail.next = None
        if node == self.head and node == self.tail:  # If the list becomes empty
            self.head = None
            self.tail = None
        self.removeNodeBindings(node)  # Remove all bindings of the node

    # Check if a node with a specific value exists in the list
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None  # Return True if the value is found, False otherwise

    # Remove all bindings (pointers) of a node
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


# Dummy data and testing the doubly linked list
dll = DoublyLinkedList()

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Setting head and tail
dll.setHead(node1)
dll.setTail(node5)

# Inserting nodes
dll.insertAfter(node1, node2)
dll.insertAfter(node2, node3)
dll.insertBefore(node5, node4)

# Removing a node with a specific value
dll.removeNodesWithValue(3)

# Checking if a value exists
print(dll.containsNodeWithValue(3))  # Should print False
print(dll.containsNodeWithValue(2))  # Should print True



# Complete Execution of Code and Functions:

# 1. **Node Class**:
#    - Represents a single node in the doubly linked list.
#    - Each node contains a `value`, and two pointers: `prev` (to the previous node) and `next` (to the next node).
#    - Initialized with a value, and `prev` and `next` set to `None` by default.

# 2. **DoublyLinkedList Class**:
#    - Manages the overall doubly linked list, maintaining references to the `head` (first node) and `tail` (last node).

# 3. **setHead(node)**:
#    - Sets the specified node as the head of the list.
#    - If the list is empty, the node becomes both the `head` and `tail`.
#    - If the list is not empty, it calls `insertBefore` to position the node before the current head.

# 4. **setTail(node)**:
#    - Sets the specified node as the tail of the list.
#    - If the list is empty, the node becomes both the `head` and `tail` by delegating to `setHead`.
#    - If the list is not empty, it calls `insertAfter` to position the node after the current tail.

# 5. **insertBefore(existingNode, nodeToInsert)**:
#    - Inserts `nodeToInsert` before an existing node (`existingNode`).
#    - First removes `nodeToInsert` from its current position to avoid duplication.
#    - Updates pointers:
#      - Sets `nodeToInsert.next` to `existingNode`.
#      - Sets `nodeToInsert.prev` to `existingNode.prev`.
#      - Adjusts the previous node’s `next` pointer and `existingNode`’s `prev` pointer to link the nodes correctly.
#    - If `existingNode` is the head, updates the head pointer to `nodeToInsert`.

# 6. **insertAfter(existingNode, nodeToInsert)**:
#    - Inserts `nodeToInsert` after an existing node (`existingNode`).
#    - First removes `nodeToInsert` from its current position to avoid duplication.
#    - Updates pointers:
#      - Sets `nodeToInsert.prev` to `existingNode`.
#      - Sets `nodeToInsert.next` to `existingNode.next`.
#      - Adjusts the next node’s `prev` pointer and `existingNode`’s `next` pointer to link the nodes correctly.
#    - If `existingNode` is the tail, updates the tail pointer to `nodeToInsert`.

# 7. **insertAtPosition(position, nodeToInsert)**:
#    - Inserts `nodeToInsert` at the specified position in the list (1-indexed).
#    - If the position is 1, sets the node as the head using `setHead`.
#    - Traverses the list until the target position is reached.
#    - Inserts the node before the node at the target position using `insertBefore`.
#    - If the position is beyond the length of the list, appends the node at the tail.

# 8. **removeNodesWithValue(value)**:
#    - Traverses the list and removes all nodes that contain the specified value.
#    - For each matching node, calls the `remove` function to unlink it from the list.
#    - Continues traversal until the end of the list.

# 9. **remove(node)**:
#    - Removes the specified node from the list.
#    - Adjusts the `head` or `tail` pointers if the node is at the start or end of the list:
#      - If removing the head, updates the head to the next node and adjusts its `prev` pointer to `None`.
#      - If removing the tail, updates the tail to the previous node and adjusts its `next` pointer to `None`.
#      - If the node is both the head and tail (single-node list), sets both pointers to `None`.
#    - Calls `removeNodeBindings` to unlink the node from its neighbors.

# 10. **containsNodeWithValue(value)**:
#     - Searches for a node with the specified value.
#     - Traverses the list from the head, checking each node’s value.
#     - Returns `True` if a match is found, otherwise `False`.

# 11. **removeNodeBindings(node)**:
#     - Helper function to unlink a node from the list.
#     - Adjusts the `prev` and `next` pointers of the node’s neighbors to bypass the node.
#     - Sets the node’s own `prev` and `next` pointers to `None`, completely detaching it.

