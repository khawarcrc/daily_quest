# Problem Statement:
# Given a sorted linked list, write a function to remove all duplicates such that 
# each element appears only once. The function should modify the linked list in-place 
# and return the head of the modified linked list.

# Initialize Pointers:
# The function starts by initializing currentNode to the head of the list.

# Traverse the List:
# The outer while loop traverses each node in the linked list.

# Skip Duplicates:
# The inner while loop skips over all nodes that have the same value as the currentNode.
# It stops when it finds a distinct value or reaches the end.

# Update Links:
# The currentNode.next is updated to the next distinct node, effectively removing 
# all intermediate duplicate nodes.

# Continue:
# The process repeats until all nodes have been processed.

# Result:
# The modified list with all duplicates removed is returned.

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Start with the head of the linked list
    currentNode = linkedList
    
    # Iterate through the linked list until the end is reached
    while currentNode is not None:
        print(f"Current Node: {currentNode.value}")

        # Find the next distinct node
        nextDistinctNode = currentNode.next
        while (
            nextDistinctNode is not None and nextDistinctNode.value == currentNode.value
        ):
            print(f"Duplicate detected: {nextDistinctNode.value}")
            nextDistinctNode = nextDistinctNode.next

        # Update the next pointer of the current node to the next distinct node
        currentNode.next = nextDistinctNode
        print(f"Linking {currentNode.value} to {nextDistinctNode.value if nextDistinctNode else 'None'}")

        # Move to the next distinct node
        currentNode = nextDistinctNode

    # Return the head of the modified linked list
    return linkedList


# Helper function to print the linked list
def printLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        print(currentNode.value, end=" -> ")
        currentNode = currentNode.next
    print("None")


# Dummy data to test the function
# Creating a linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5
linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(2)
linkedList.next.next.next = LinkedList(3)
linkedList.next.next.next.next = LinkedList(3)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next.next.next = LinkedList(5)

print("Original Linked List:")
printLinkedList(linkedList)

# Remove duplicates from the linked list
linkedList = removeDuplicatesFromLinkedList(linkedList)

print("\nLinked List after removing duplicates:")
printLinkedList(linkedList)
