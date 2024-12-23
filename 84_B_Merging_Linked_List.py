
# Problem Statement:
# Given two singly linked lists, determine the node at which the two linked lists merge.
# If the two linked lists do not merge, return None.
# The merging point is the first node that is common between the two lists.

# Problem Explanation:
# - Linked lists can merge at a node where they share the same reference to the rest of the list.
# - Once merged, both lists have identical subsequent nodes.
# - The task is to find the first such node or determine if no merging point exists.
# 
# Example:
# Linked List 1: 1 -> 2 -> 3 -> 4 -> 5
# Linked List 2: 9 -> 10 -> 4 -> 5 (Merge at node with value 4)
# Expected Output: Node with value 4
# 
# Constraints:
# - The input linked lists are not guaranteed to have the same length.
# - The merge point, if it exists, must be determined using constant space.
# - The solution must work for any two valid singly linked lists.

# Code Execution Theory:
# 1. Initialize two pointers, `currentNodeOne` and `currentNodeTwo`, pointing to the heads of the two linked lists.
# 2. Traverse both lists simultaneously:
#    - If a pointer reaches the end of its list, move it to the head of the other list.
#    - If a pointer is not at the end, move it to the next node.
# 3. Continue traversing until both pointers meet:
#    - If the pointers meet at a node, it is the merging point.
#    - If the pointers meet at None, the lists do not merge.
# 4. Return the node where the two pointers meet.
# 
# Why This Works:
# - By switching the pointers between the two lists, the total traversal for each pointer
#   is equal to the combined length of both lists.
# - If there is a merging point, the pointers will meet at that node after equalizing the traversal lengths.
# - If there is no merging point, the pointers will both eventually reach the end (None).
# 
# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
# Space Complexity: O(1), as the solution uses only two pointers for traversal.


class LinkedList:
    def __init__(self, value):
        # Initialize a node with a value and a reference to the next node (initially None)
        self.value = value
        self.next = None

def mergingLinkedLists(linkedListOne, linkedListTwo):
    """
    Function to find the merging point of two linked lists.
    If the two linked lists merge at a certain node, this function returns that node.
    If they do not merge, it returns None.
    """
    # Start traversing both linked lists
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    # Loop until both pointers point to the same node (or None if no merge point exists)
    while currentNodeOne is not currentNodeTwo:
        # If pointer 1 reaches the end, start it at the beginning of the other list
        currentNodeOne = currentNodeOne.next if currentNodeOne else linkedListTwo
        # If pointer 2 reaches the end, start it at the beginning of the first list
        currentNodeTwo = currentNodeTwo.next if currentNodeTwo else linkedListOne

    # Return the merge point (or None if no merge point exists)
    return currentNodeOne

# Creating dummy data for testing
# Linked list 1: 1 -> 2 -> 3 -> 4 -> 5
# Linked list 2: 9 -> 10 -> (merge at 4) -> 5
# Common merging point: 4
linkedListOne = LinkedList(1)
linkedListOne.next = LinkedList(2)
linkedListOne.next.next = LinkedList(3)
linkedListOne.next.next.next = LinkedList(4)
linkedListOne.next.next.next.next = LinkedList(5)

linkedListTwo = LinkedList(9)
linkedListTwo.next = LinkedList(10)
linkedListTwo.next.next = linkedListOne.next.next.next  # Merge at node with value 4

# Finding the merging point
mergePoint = mergingLinkedLists(linkedListOne, linkedListTwo)

# Output the result
if mergePoint:
    print(f"The merging point is at node with value: {mergePoint.value}")
else:
    print("The two linked lists do not merge.")
