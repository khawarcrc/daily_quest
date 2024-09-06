// Define the ListNode class in JavaScript
class ListNode {
    constructor(value = 0, next = null) {
        this.value = value;  // Value of the node
        this.next = next;    // Pointer to the next node
    }
}

// Function to find the middle node using slow and fast pointer
function middleNode(linkedList) {
    let slowNode = linkedList;  // slowNode moves one step at a time
    let fastNode = linkedList;  // fastNode moves two steps at a time

    // Traverse the list with the slow and fast pointers
    while (fastNode !== null && fastNode.next !== null) {
        slowNode = slowNode.next;          // Move slowNode one step forward
        fastNode = fastNode.next.next;     // Move fastNode two steps forward

        // Print the current values of the pointers for debugging
        console.log(`slowNode value: ${slowNode.value}`);
        if (fastNode !== null) {
            console.log(`fastNode value: ${fastNode.value}`);
        } else {
            console.log("fastNode has reached the end of the list");
        }
    }

    // When fastNode reaches the end, slowNode will be at the middle
    return slowNode;
}

// Creating nodes for the linked list
const node5 = new ListNode(5);
const node4 = new ListNode(4, node5);
const node3 = new ListNode(3, node4);
const node2 = new ListNode(2, node3);
const node1 = new ListNode(1, node2);  // Head of the list

// Calling the middleNode function
const middle = middleNode(node1);  // Pass the head (node1) to the function

// Output the middle node's value
console.log(`Middle node value is: ${middle.value}`);
