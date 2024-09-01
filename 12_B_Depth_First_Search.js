class Node {
    constructor(name) {
        // Initialize the node with a name and an empty array of children
        this.children = [];
        this.name = name;
    }

    addChild(name) {
        // Add a new child node with the given name to the current node
        this.children.push(new Node(name));
    }

    depthFirstSearch(array) {
        // Print statement to indicate the function has started executing for a specific node
        console.log(`Visiting node: ${this.name}`);

        // Append the current node's name to the traversal array
        array.push(this.name);

        // Print the current state of the array
        console.log(`Current DFS array: ${array}`);
        
        // Recursively call depthFirstSearch on all children
        for (const child of this.children) {
            console.log(`Going deeper into child: ${child.name} of parent: ${this.name}`);
            child.depthFirstSearch(array);
        }

        // Print statement to indicate backtracking from a node
        console.log(`Backtracking from node: ${this.name}`);
        
        // Return the array after traversing all nodes
        return array;
    }
}

// Creating a root node
const root = new Node("A");

// Adding children to the root node
root.addChild("B");
root.addChild("C");
root.addChild("D");

// Adding children to the "B" node
root.children[0].addChild("E");
root.children[0].addChild("F");

// Adding children to the "D" node
root.children[2].addChild("G");
root.children[2].addChild("H");

// Perform depth-first search starting from the root node
const result = root.depthFirstSearch([]);

// Print the final result of depth-first search
console.log(`Final DFS result: ${result}`);
