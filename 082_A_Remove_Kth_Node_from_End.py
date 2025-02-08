# Problem Statement
# -----------------
# The goal is to remove the kth node from the end of a singly linked list.
# The list is made up of nodes, where each node contains a value and a pointer to the next node.
# The input is the head of the linked list and an integer k, representing the position of the node to remove from the end.
# The function should modify the linked list in place and adjust pointers correctly to maintain the structure.

# Problem Explanation
# --------------------
# Given a linked list, nodes are indexed from 1 to n starting from the head.
# However, when counting from the end, the last node has an index of 1, the second to last node has an index of 2, and so on.
# For example, in a list 1 -> 2 -> 3 -> 4 -> 5, the 2nd node from the end is the node with value 4.
# The task is to identify this node and remove it by updating the pointers in the list.

# Approach to Solve the Problem
# -----------------------------
# 1. Use two pointers, `first` and `second`, both initially pointing to the head of the linked list.
# 2. Move the `second` pointer k steps forward. This ensures that the `first` pointer is k steps behind the `second` pointer.
# 3. If `second` becomes None after these k steps, it means the head node is the one to be removed.
#    - In this case, update the head's value to match the next node's value and adjust the head's pointer to skip the next node.
# 4. If `second` is not None, continue moving both pointers one step at a time until `second` reaches the end of the list.
# 5. At this point, the `first` pointer will be just before the node to be removed.
#    - Adjust the `first` pointer's `next` attribute to skip the target node, effectively removing it.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to remove the kth node from the end of the linked list
def removeKthNodeFromEnd(head, k):
    # Step 1: Initialize pointers and counter
    counter = 1
    first = head
    second = head

    # Step 2: Move the 'second' pointer k steps ahead
    while counter <= k:
        # Ensure the list has at least k nodes
        if second is None:
            raise ValueError("The list is shorter than k nodes.")
        second = second.next
        counter += 1

    # Step 3: Handle the edge case where the head needs to be removed
    if second is None:
        head.value = head.next.value  # Copy value from the next node
        head.next = head.next.next  # Skip the next node
        return

    # Step 4: Move both pointers until 'second' reaches the last node
    while second.next is not None:
        second = second.next
        first = first.next

    # Step 5: Remove the kth node from the end by skipping it
    first.next = first.next.next

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Create a dummy linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)

print("Original Linked List:")
printLinkedList(head)

# Remove the 2nd node from the end
k = 2
removeKthNodeFromEnd(head, k)

print(f"Linked List after removing the {k}th node from the end:")
printLinkedList(head)
