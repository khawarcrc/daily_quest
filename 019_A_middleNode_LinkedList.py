class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # Value of the node
        self.next = next  # Pointer to the next node


def middleNode(linkedList):
    # Initialize counter to count total nodes
    count = 0
    # Set the current node to the head of the list
    currentNode = linkedList

    # Traverse the linked list to count total nodes
    while currentNode is not None:
        count += 1  # Increment the count for each node
        print(
            f"Node {count}: {currentNode.value}"
        )  # Print current node's value (assuming it has a 'value' attribute)
        currentNode = currentNode.next  # Move to the next node

 

    # Reset middleNode to the head of the list
    middleNode = linkedList

    # Traverse the first half of the list to reach the middle node
    for i in range(count // 2):
        middleNode = middleNode.next  # Move to the next node
        print(
            f"Step {i + 1}: Middle node value is now {middleNode.value}"
        )  # Print the current middle node's value

    # Return the middle node
    print(f"Middle node found with value: {middleNode.value}")
    return middleNode


# Creating nodes for the linked list
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)  # Head of the list

# Calling the middleNode function
middle = middleNode(node1)  # Pass the head (node1) to the function

# Output the middle node's value
print(f"Middle node value is: {middle.value}")
