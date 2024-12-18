# Problem Statement:
# You are given two singly linked lists that may or may not merge at some point. 
# Your task is to determine the merging point of the two linked lists, 
# i.e., the node at which both linked lists intersect. If there is no merging point, return None.

# Explanation of the Problem:
# 1. A singly linked list consists of nodes, where each node contains a value and a pointer to the next node.
# 2. Two linked lists can either:
#    - Have no intersection, meaning they remain independent throughout.
#    - Merge at a specific node, after which they share the same subsequent nodes.
# 3. The merging node is the first common node in both linked lists if they merge.
# 4. The goal is to identify this merging node efficiently.

# Execution Theory:
# 1. Create a set to store nodes of the first linked list.
#    - This allows quick lookup to check whether a node from the second linked list exists in the first one.
# 2. Traverse the first linked list:
#    - Add each node encountered to the set.
#    - Continue until the end of the list.
# 3. Traverse the second linked list:
#    - Check each node to see if it exists in the set created from the first linked list.
#    - If a match is found, it means the node is the merging point.
# 4. Return the merging node as soon as a match is found.
# 5. If no merging node is found after traversing the second list, return None.

class LinkedList:
    # Constructor to initialize a node in the linked list
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None  # Pointer to the next node in the list


def mergingLinkedLists(linkedListOne, linkedListTwo):
    """
    This function finds the intersection point of two linked lists.
    If the lists merge, it returns the node where they merge;
    otherwise, it returns None.
    """
    # Create a set to store nodes from the first linked list
    listOneNodes = set()

    # Traverse the first linked list and add each node to the set
    currentNodeOne = linkedListOne
    while currentNodeOne is not None:
        listOneNodes.add(currentNodeOne)  # Add the current node to the set
        currentNodeOne = currentNodeOne.next  # Move to the next node

    # Traverse the second linked list
    currentNodeTwo = linkedListTwo
    while currentNodeTwo is not None:
        # Check if the current node of the second list is in the set
        if currentNodeTwo in listOneNodes:
            return currentNodeTwo  # Return the merging node
        currentNodeTwo = currentNodeTwo.next  # Move to the next node

    # If no merging point is found, return None
    return None


# Create dummy data to demonstrate the function

# Linked List 1: 1 -> 2 -> 3 -> 4 -> 5
headOne = LinkedList(1)
headOne.next = LinkedList(2)
headOne.next.next = LinkedList(3)
headOne.next.next.next = LinkedList(4)
headOne.next.next.next.next = LinkedList(5)

# Linked List 2: 9 -> 10 -> (merges at 4)
headTwo = LinkedList(9)
headTwo.next = LinkedList(10)
headTwo.next.next = headOne.next.next.next  # Merge point at node with value 4

# Find the merging point
mergingNode = mergingLinkedLists(headOne, headTwo)

# Display the result
if mergingNode:
    print(f"The merging node is: {mergingNode.value}")
else:
    print("No merging node found.")
