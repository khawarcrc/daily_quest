class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # Value of the node
        self.next = next    # Pointer to the next node


def middleNode(linkedList): 
    # Initialize two pointers: slowNode and fastNode
    slowNode = linkedList  # slowNode moves one step at a time
    fastNode = linkedList  # fastNode moves two steps at a time
    
    # Traverse the list with the slow and fast pointers
    while fastNode is not None and fastNode.next is not None: 
        # Move slowNode one step forward
        slowNode = slowNode.next  
        # Move fastNode two steps forward
        fastNode = fastNode.next.next  
    
        # Print the current values of the pointers for debugging
        print(f"slowNode value: {slowNode.value}")
        if fastNode is not None:
            print(f"fastNode value: {fastNode.value}")
        else:
            print("fastNode has reached the end of the list")
    
    # When the fastNode reaches the end, slowNode will be at the middle
    return slowNode    


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
