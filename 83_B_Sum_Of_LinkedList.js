// Define the LinkedList class to represent a node in the linked list
class LinkedList {
    constructor(value) {
      // Initialize the node with a value and set the next pointer to null
      this.value = value;
      this.next = null;
    }
  }
  
  // Function to calculate the sum of two linked lists representing numbers
  function sumOfLinkedLists(linkedListOne, linkedListTwo) {
    // Create a dummy head node to help build the resulting linked list
    const newLinkedListHeadPointer = new LinkedList(0);
    // Pointer to traverse the new linked list
    let currentNode = newLinkedListHeadPointer;
    // Carry variable to handle sums greater than 9
    let carry = 0;
  
    // Pointers to traverse the input linked lists
    let nodeOne = linkedListOne;
    let nodeTwo = linkedListTwo;
  
    // Continue until both lists are fully traversed and there is no carry
    while (nodeOne !== null || nodeTwo !== null || carry !== 0) {
      // Get the value of the current node from linked list one, or 0 if null
      const valueOne = nodeOne !== null ? nodeOne.value : 0;
      // Get the value of the current node from linked list two, or 0 if null
      const valueTwo = nodeTwo !== null ? nodeTwo.value : 0;
  
      // Calculate the sum of values and the carry
      const sumOfValues = valueOne + valueTwo + carry;
  
      // Compute the new digit to be added to the resulting list
      const newValue = sumOfValues % 10;
      // Create a new node with the computed value
      const newNode = new LinkedList(newValue);
      // Link the new node to the current node of the result linked list
      currentNode.next = newNode;
      // Move the pointer to the new node
      currentNode = newNode;
  
      // Update the carry for the next iteration
      carry = Math.floor(sumOfValues / 10);
      // Move to the next node in the first linked list, if available
      nodeOne = nodeOne !== null ? nodeOne.next : null;
      // Move to the next node in the second linked list, if available
      nodeTwo = nodeTwo !== null ? nodeTwo.next : null;
    }
  
    // Return the resulting linked list, skipping the dummy head node
    return newLinkedListHeadPointer.next;
  }
  
  // Helper function to create a linked list from an array of integers
  function createLinkedList(values) {
    const head = new LinkedList(values[0]);
    let current = head;
    for (let i = 1; i < values.length; i++) {
      current.next = new LinkedList(values[i]);
      current = current.next;
    }
    return head;
  }
  
  // Helper function to print a linked list
  function printLinkedList(head) {
    const values = [];
    while (head !== null) {
      values.push(head.value);
      head = head.next;
    }
    console.log(values.join(" -> "));
  }
  
  // Dummy data for testing
  // Representing the numbers 617 (7 -> 1 -> 6) and 295 (5 -> 9 -> 2)
  const linkedListOne = createLinkedList([7, 1, 6]);
  const linkedListTwo = createLinkedList([5, 9, 2]);
  
  // Calculate the sum of the two linked lists
  const result = sumOfLinkedLists(linkedListOne, linkedListTwo);
  
  // Print the resulting linked list
  console.log("Resulting Linked List:");
  printLinkedList(result);
  