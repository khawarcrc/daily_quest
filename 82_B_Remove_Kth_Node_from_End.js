// # LinkedList Class Theory:
// # - A linked list is a data structure consisting of nodes where each node contains a value and a reference to the next node.
// # - The `LinkedList` class is designed to initialize a node with a given value and a `next` pointer that defaults to `None`.

// # Function to Remove kth Node from End Theory:
// # - This function removes the kth node from the end of a linked list.
// # - The approach uses two-pointer technique (often called the fast-slow pointer approach).

// # Step 1: Initialize Pointers and Counter
// # - Two pointers (`first` and `second`) are initialized at the head of the list.
// # - A counter is used to track the movement of the `second` pointer.

// # Step 2: Move the 'Second' Pointer k Steps Ahead
// # - The `second` pointer is moved k steps ahead to ensure that there is a gap of k nodes between the `first` and `second` pointers.
// # - If the `second` pointer becomes `None` during this process, it indicates that the list has fewer than k nodes, and an exception is raised.

// # Step 3: Handle Edge Case for Head Removal
// # - If the `second` pointer is `None` after moving k steps, it means the head of the linked list is the kth node from the end.
// # - To remove the head, its value is replaced with the value of the next node, and the `next` pointer is updated to skip the next node.

// # Step 4: Move Both Pointers Until the 'Second' Pointer Reaches the End
// # - Both `first` and `second` pointers are moved one step at a time until the `second` pointer reaches the last node.
// # - This ensures that the `first` pointer stops at the node just before the kth node from the end.

// # Step 5: Remove the kth Node from the End
// # - The `first.next` pointer is updated to skip the kth node, effectively removing it from the list.

// # Helper Function to Print the Linked List
// # - A utility function is used to traverse the linked list from the head node to the end.
// # - It prints the value of each node in a readable format (e.g., `1 -> 2 -> 3 -> None`).



class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// Function to remove the kth node from the end of the linked list
function removeKthNodeFromEnd(head, k) {
    console.log(`Removing the ${k}th node from the end of the list...`);
    
    // Step 1: Initialize pointers and counter
    let counter = 1;
    let first = head;
    let second = head;

    console.log("Moving the 'second' pointer k steps ahead...");
    // Step 2: Move the 'second' pointer k steps ahead
    while (counter <= k) {
        // Ensure the list has at least k nodes
        if (second === null) {
            throw new Error("The list is shorter than k nodes.");
        }
        second = second.next;
        console.log(`Step ${counter}: Moved 'second' pointer to node with value: ${second ? second.value : 'None'}`);
        counter++;
    }

    // Step 3: Handle the edge case where the head needs to be removed
    if (second === null) {
        console.log("Edge case detected: The head node needs to be removed.");
        console.log(`Head value before removal: ${head.value}`);
        head.value = head.next.value; // Copy value from the next node
        head.next = head.next.next; // Skip the next node
        console.log(`Head value after removal: ${head.value}`);
        return;
    }

    console.log("Moving both 'first' and 'second' pointers until 'second' reaches the end...");
    // Step 4: Move both pointers until 'second' reaches the last node
    while (second.next !== null) {
        second = second.next;
        first = first.next;
        console.log(`Moved 'first' to node with value: ${first.value}, 'second' to node with value: ${second.value}`);
    }

    // Step 5: Remove the kth node from the end by skipping it
    console.log(`Node to be removed: ${first.next.value}`);
    first.next = first.next.next;
    console.log("Node removed successfully.");
}

// Helper function to print the linked list
function printLinkedList(head) {
    let current = head;
    let result = "";
    while (current !== null) {
        result += current.value + " -> ";
        current = current.next;
    }
    result += "None";
    console.log(result);
}

// Create a dummy linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
let head = new LinkedList(1);
head.next = new LinkedList(2);
head.next.next = new LinkedList(3);
head.next.next.next = new LinkedList(4);
head.next.next.next.next = new LinkedList(5);

console.log("Original Linked List:");
printLinkedList(head);

// Remove the 2nd node from the end
let k = 2;
removeKthNodeFromEnd(head, k);

console.log(`Linked List after removing the ${k}th node from the end:`);
printLinkedList(head);
