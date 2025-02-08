# Problem Statement:
# Given two non-empty linked lists that represent two non-negative integers in reverse order, 
# each node contains a single digit. The task is to add these two numbers and return the sum 
# as a linked list. The digits are stored in reverse order, meaning the 1's digit is at the head 
# of the list. Each of the numbers does not contain any leading zeros, except the number 0 itself.

# Example:
# Input: LinkedListOne = 2 -> 4 -> 3 (represents 342)
#        LinkedListTwo = 5 -> 6 -> 4 (represents 465)
# Output: 7 -> 0 -> 8 (represents 807)

# Problem Explanation:
# 1. Each linked list represents a number in reverse order. For example:
#    - LinkedListOne: 2 -> 4 -> 3 represents the number 342.
#    - LinkedListTwo: 5 -> 6 -> 4 represents the number 465.
# 2. We need to compute the sum of these two numbers (342 + 465 = 807).
# 3. The result should also be represented as a linked list in reverse order, 
#    i.e., 7 -> 0 -> 8, which represents the number 807.

# Code Execution Theory:
# 1. Create a dummy node to act as the head of the new linked list to store the result.
# 2. Use a pointer `currentNode` to keep track of the current position in the result linked list.
# 3. Initialize a `carry` variable to store the carry-over value when the sum of digits exceeds 9.
# 4. Traverse both input linked lists simultaneously:
#    - Add the values of the corresponding nodes from both lists.
#    - Include the `carry` from the previous calculation in the sum.
#    - Compute the new digit to add to the result linked list as `sum % 10`.
#    - Update the carry as `sum // 10`.
# 5. If a linked list is shorter than the other, assume missing values as 0.
# 6. If there is any remaining carry after processing all nodes, add it as a new node.
# 7. The final result linked list starts from the node following the dummy node.
# 8. Return the resulting linked list as the sum of the two input numbers.



# Define the LinkedList class to represent a node in the linked list
class LinkedList:
    def __init__(self, value):
        # Initialize the node with a value and set the next pointer to None
        self.value = value
        self.next = None

# Function to calculate the sum of two linked lists representing numbers
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Create a dummy head node to help build the resulting linked list
    newLinkedListHeadPointer = LinkedList(0)
    # Pointer to traverse the new linked list
    currentNode = newLinkedListHeadPointer
    # Carry variable to handle sums greater than 9
    carry = 0

    # Pointers to traverse the input linked lists
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    # Continue until both lists are fully traversed and there is no carry
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        # Get the value of the current node from linked list one, or 0 if None
        valueOne = nodeOne.value if nodeOne is not None else 0
        # Get the value of the current node from linked list two, or 0 if None
        valueTwo = nodeTwo.value if nodeTwo is not None else 0

        # Calculate the sum of values and the carry
        sumOfValues = valueOne + valueTwo + carry

        # Compute the new digit to be added to the resulting list
        newValue = sumOfValues % 10
        # Create a new node with the computed value
        newNode = LinkedList(newValue)
        # Link the new node to the current node of the result linked list
        currentNode.next = newNode
        # Move the pointer to the new node
        currentNode = newNode

        # Update the carry for the next iteration
        carry = sumOfValues // 10
        # Move to the next node in the first linked list, if available
        nodeOne = nodeOne.next if nodeOne is not None else None
        # Move to the next node in the second linked list, if available
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    # Return the resulting linked list, skipping the dummy head node
    return newLinkedListHeadPointer.next

# Helper function to create a linked list from a list of integers
def createLinkedList(values):
    head = LinkedList(values[0])
    current = head
    for value in values[1:]:
        current.next = LinkedList(value)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    values = []
    while head is not None:
        values.append(str(head.value))
        head = head.next
    print(" -> ".join(values))

# Dummy data for testing
# Representing the numbers 617 (7 -> 1 -> 6) and 295 (5 -> 9 -> 2)
linkedListOne = createLinkedList([7, 1, 6])
linkedListTwo = createLinkedList([5, 9, 2])

# Calculate the sum of the two linked lists
result = sumOfLinkedLists(linkedListOne, linkedListTwo)

# Print the resulting linked list
print("Resulting Linked List:")
printLinkedList(result)
