// Define the BST class
class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Main function to find the closest value in the BST
function findClosestValueInBst(tree, target) {
    // Call the helper function with the initial closest value as Infinity
    return findClosestValueInBstHelper(tree, target, Infinity);
}

// Helper function to traverse the BST and find the closest value
function findClosestValueInBstHelper(tree, target, closest) {
    let currentNode = tree;

    // Traverse the tree until there are no nodes left to check
    while (currentNode !== null) {
        console.log(`Checking node with value: ${currentNode.value}`);

        // If the current node is closer to the target than the previous closest, update closest
        if (Math.abs(target - closest) > Math.abs(target - currentNode.value)) {
            closest = currentNode.value;
            console.log(`Updated closest to: ${closest}`);
        }

        // Move to the left child if the target is smaller than the current node's value
        if (target < currentNode.value) {
            currentNode = currentNode.left;
            console.log("Moving to the left child");
        }
        // Move to the right child if the target is larger than the current node's value
        else if (target > currentNode.value) {
            currentNode = currentNode.right;
            console.log("Moving to the right child");
        } else {
            // If the current node's value equals the target, it is the closest possible value
            console.log("Exact match found!");
            break;
        }
    }

    // Return the closest value found
    return closest;
}

// Example BST
const root = new BST(10);
root.left = new BST(5);
root.left.left = new BST(2);
root.left.right = new BST(5);
root.right = new BST(15);
root.right.left = new BST(13);
root.right.right = new BST(22);

// Example target
const target = 12;

// Function call to find the closest value in the BST
const closestValue = findClosestValueInBst(root, target);
console.log(`The closest value to ${target} is ${closestValue}`);
