# Problem Statement:
# Implement a doubly linked list data structure in Python.
# A doubly linked list is a type of linked list in which each node contains a value 
# and two pointers: one pointing to the next node and another pointing to the previous node. 
# This allows traversal of the list in both forward and backward directions.

# Theory:
# 1. **Node Structure:**
#    - Each node in the doubly linked list contains three attributes:
#      - `value`: Stores the data of the node.
#      - `next`: Points to the next node in the list.
#      - `prev`: Points to the previous node in the list.
#    - The `next` pointer of the last node is set to `None`.
#    - The `prev` pointer of the first node is set to `None`.

# 2. **Doubly Linked List Structure:**
#    - The doubly linked list contains two attributes:
#      - `head`: Points to the first node in the list.
#      - `tail`: Points to the last node in the list.
#    - If the list is empty, both `head` and `tail` are `None`.

# 3. **Operations on Doubly Linked List:**
#    - **Insertion**:
#      - At the beginning: Add a new node before the current `head` and update the `head`.
#      - At the end: Add a new node after the current `tail` and update the `tail`.
#      - At a specific position: Traverse to the desired position, update pointers to insert the new node.

#    - **Deletion**:
#      - From the beginning: Remove the `head` node and update the `head` to the next node.
#      - From the end: Remove the `tail` node and update the `tail` to the previous node.
#      - From a specific position: Traverse to the desired position and update pointers to remove the node.

#    - **Traversal**:
#      - Forward Traversal: Start from the `head` and move through the `next` pointers until `None`.
#      - Backward Traversal: Start from the `tail` and move through the `prev` pointers until `None`.

#    - **Search**:
#      - Traverse the list to find a node with a specific value.
#      - Return the position of the node or indicate that it is not found.

#    - **Update**:
#      - Traverse the list to find a node with a specific value.
#      - Update the value of the node.

# 4. **Edge Cases**:
#    - Insertion into an empty list.
#    - Deletion from an empty list.
#    - Deleting a node that doesn’t exist.
#    - Traversing an empty list.
#    - Handling `None` values for `next` and `prev` pointers during insertion and deletion.

# 5. **Time Complexity Analysis**:
#    - **Insertion**:
#      - At the beginning: O(1)
#      - At the end: O(1)
#      - At a specific position: O(n) in the worst case due to traversal.
#    - **Deletion**:
#      - From the beginning: O(1)
#      - From the end: O(1)
#      - From a specific position: O(n) in the worst case due to traversal.
#    - **Traversal**: O(n) for both forward and backward traversal.
#    - **Search**: O(n) in the worst case as it requires traversal of the list.
#    - **Update**: O(n) in the worst case due to traversal.


class Node:
    def __init__(self, value):
        """
        Initialize a Node with a given value.
        Each Node has pointers to the previous and next nodes in the list.
        """
        self.value = value  # Value of the Node
        self.prev = None  # Pointer to the previous Node
        self.next = None  # Pointer to the next Node

# DoublyLinkedList class to manage the entire list
class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty Doubly Linked List.
        The list starts with no head or tail.
        """
        self.head = None  # Head of the list
        self.tail = None  # Tail of the list

    def insert_at_head(self, value):
        """
        Insert a new Node with the given value at the head of the list.
        """
        new_node = Node(value)  # Create a new Node
        if not self.head:
            # If the list is empty, head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  # Update the head to the new node

    def insert_at_tail(self, value):
        """
        Insert a new Node with the given value at the tail of the list.
        """
        new_node = Node(value)  # Create a new Node
        if not self.tail:
            # If the list is empty, head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node to the current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node  # Update the tail to the new node

    def delete(self, value):
        """
        Delete the first Node with the given value from the list.
        """
        current = self.head  # Start from the head
        while current:
            if current.value == value:
                # If the node to delete is the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                # If the node to delete is the tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                # If the node is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Node found and deleted, exit
            current = current.next  # Move to the next node

    def traverse_forward(self):
        """
        Traverse the list from head to tail and print the values.
        """
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """
        Traverse the list from tail to head and print the values.
        """
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_tail(20)
dll.insert_at_tail(30)
dll.traverse_forward()  # Output: 10 <-> 20 <-> 30 <-> None
dll.traverse_backward()  # Output: 30 <-> 20 <-> 10 <-> None
dll.delete(20)
dll.traverse_forward()  # Output: 10 <-> 30 <-> None
