// Problem Statement:
// Given a sorted linked list, write a function to remove all duplicates such that
// each element appears only once. The function should modify the linked list in-place
// and return the head of the modified linked list.

class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  // Start with the head of the linked list
  let currentNode = linkedList;

  // Iterate through the linked list until the end is reached
  while (currentNode !== null) {
    console.log(`Current Node: ${currentNode.value}`);

    // Find the next distinct node
    let nextDistinctNode = currentNode.next;
    while (
      nextDistinctNode !== null &&
      nextDistinctNode.value === currentNode.value
    ) {
      console.log(`Duplicate detected: ${nextDistinctNode.value}`);
      nextDistinctNode = nextDistinctNode.next;
    }

    // Update the next pointer of the current node to the next distinct node
    currentNode.next = nextDistinctNode;
    console.log(
      `Linking ${currentNode.value} to ${
        nextDistinctNode ? nextDistinctNode.value : "None"
      }`
    );

    // Move to the next distinct node
    currentNode = nextDistinctNode;
  }

  // Return the head of the modified linked list
  return linkedList;
}

// Helper function to print the linked list
function printLinkedList(linkedList) {
  let currentNode = linkedList;
  let result = "";
  while (currentNode !== null) {
    result += currentNode.value + " -> ";
    currentNode = currentNode.next;
  }
  result += "None";
  console.log(result);
}

// Dummy data to test the function
// Creating a linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 5
const linkedList = new LinkedList(1);
linkedList.next = new LinkedList(1);
linkedList.next.next = new LinkedList(2);
linkedList.next.next.next = new LinkedList(3);
linkedList.next.next.next.next = new LinkedList(3);
linkedList.next.next.next.next.next = new LinkedList(4);
linkedList.next.next.next.next.next.next = new LinkedList(4);
linkedList.next.next.next.next.next.next.next = new LinkedList(4);
linkedList.next.next.next.next.next.next.next.next = new LinkedList(5);

console.log("Original Linked List:");
printLinkedList(linkedList);

// Remove duplicates from the linked list
removeDuplicatesFromLinkedList(linkedList);

console.log("\nLinked List after removing duplicates:");
printLinkedList(linkedList);
