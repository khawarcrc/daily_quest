// Node class represents a single node in the doubly linked list
class Node {
    constructor(value) {
        this.value = value; // Value stored in the node
        this.prev = null;   // Pointer to the previous node
        this.next = null;   // Pointer to the next node
    }
}

// DoublyLinkedList class represents the entire doubly linked list
class DoublyLinkedList {
    constructor() {
        this.head = null; // Reference to the head (first node) of the list
        this.tail = null; // Reference to the tail (last node) of the list
    }

    // Set the given node as the head of the list
    setHead(node) {
        if (this.head === null) {
            this.head = node;
            this.tail = node;
            return;
        }
        this.insertBefore(this.head, node);
    }

    // Set the given node as the tail of the list
    setTail(node) {
        if (this.tail === null) {
            this.setHead(node);
            return;
        }
        this.insertAfter(this.tail, node);
    }

    // Insert a node before a given node
    insertBefore(node, nodeToInsert) {
        if (nodeToInsert === this.head && nodeToInsert === this.tail) {
            return; // Prevent redundant operations
        }
        this.remove(nodeToInsert);
        nodeToInsert.prev = node.prev;
        nodeToInsert.next = node;

        if (node.prev === null) {
            this.head = nodeToInsert;
        } else {
            node.prev.next = nodeToInsert;
        }
        node.prev = nodeToInsert;
    }

    // Insert a node after a given node
    insertAfter(node, nodeToInsert) {
        if (nodeToInsert === this.head && nodeToInsert === this.tail) {
            return; // Prevent redundant operations
        }
        this.remove(nodeToInsert);
        nodeToInsert.prev = node;
        nodeToInsert.next = node.next;

        if (node.next === null) {
            this.tail = nodeToInsert;
        } else {
            node.next.prev = nodeToInsert;
        }
        node.next = nodeToInsert;
    }

    // Insert a node at a specific position (1-indexed)
    insertAtPosition(position, nodeToInsert) {
        if (position === 1) {
            this.setHead(nodeToInsert);
            return;
        }

        let currentNode = this.head;
        let currentPosition = 1;

        while (currentNode !== null && currentPosition !== position) {
            currentNode = currentNode.next;
            currentPosition++;
        }

        if (currentNode !== null) {
            this.insertBefore(currentNode, nodeToInsert);
        } else {
            this.setTail(nodeToInsert);
        }
    }

    // Remove all nodes with a specific value
    removeNodesWithValue(value) {
        let currentNode = this.head;
        while (currentNode !== null) {
            const nodeToRemove = currentNode;
            currentNode = currentNode.next;
            if (nodeToRemove.value === value) {
                this.remove(nodeToRemove);
            }
        }
    }

    // Remove a specific node from the list
    remove(node) {
        if (node === this.head) {
            this.head = this.head.next;
            if (this.head !== null) {
                this.head.prev = null;
            }
        }
        if (node === this.tail) {
            this.tail = this.tail.prev;
            if (this.tail !== null) {
                this.tail.next = null;
            }
        }
        if (node === this.head && node === this.tail) {
            this.head = null;
            this.tail = null;
        }
        this.removeNodeBindings(node);
    }

    // Check if a node with a specific value exists in the list
    containsNodeWithValue(value) {
        let currentNode = this.head;
        while (currentNode !== null && currentNode.value !== value) {
            currentNode = currentNode.next;
        }
        return currentNode !== null;
    }

    // Remove all bindings (pointers) of a node
    removeNodeBindings(node) {
        if (node.prev !== null) {
            node.prev.next = node.next;
        }
        if (node.next !== null) {
            node.next.prev = node.prev;
        }
        node.prev = null;
        node.next = null;
    }
}

// Dummy data and testing the doubly linked list
const dll = new DoublyLinkedList();

// Creating nodes
const node1 = new Node(1);
const node2 = new Node(2);
const node3 = new Node(3);
const node4 = new Node(4);
const node5 = new Node(5);

// Setting head and tail
dll.setHead(node1);
dll.setTail(node5);

// Inserting nodes
dll.insertAfter(node1, node2);
dll.insertAfter(node2, node3);
dll.insertBefore(node5, node4);

// Removing a node with a specific value
dll.removeNodesWithValue(3);

// Checking if a value exists
console.log(dll.containsNodeWithValue(3)); // Should print false
console.log(dll.containsNodeWithValue(2)); // Should print true
