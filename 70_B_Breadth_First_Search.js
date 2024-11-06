class Node {
    // Constructor to initialize the node with a name and empty list of children
    constructor(name) {
        this.children = [];
        this.name = name;
    }

    // Method to add a child node by name
    addChild(name) {
        // Append a new Node object with the given name to the children list
        this.children.push(new Node(name));
        return this;  // Return self to allow method chaining
    }

    // Method to perform breadth-first search and populate the array with node names
    breadthFirstSearch(array) {
        let queue = [this];  // Initialize the queue with the root node
        while (queue.length > 0) {  // Loop until the queue is empty
            let current = queue.shift();  // Remove the first element from the queue
            array.push(current.name);  // Append the current node's name to the result array
            // Add all children of the current node to the queue for further exploration
            for (let child of current.children) {
                queue.push(child);
            }
        }
        return array;  // Return the array containing node names in BFS order
    }
}

// Dummy data to test the breadthFirstSearch function
// Creating a root node and adding children
const root = new Node("A");
root.addChild("B").addChild("C").addChild("D");
root.children[0].addChild("E").addChild("F");
root.children[2].addChild("G").addChild("H");

// Performing breadth-first search on the tree and storing the result
const result = root.breadthFirstSearch([]);  // Expected order: ["A", "B", "C", "D", "E", "F", "G", "H"]

console.log(result);  // Output the BFS traversal order
