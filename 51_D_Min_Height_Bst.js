class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    // Method to insert a value into the BST
    insert(value) {
        if (value < this.value) {
            // If the value is less than the current node's value
            if (this.left === null) {
                this.left = new BST(value);
            } else {
                // Recursively insert into the left subtree
                this.left.insert(value);
            }
        } else {
            // If the value is greater or equal, insert into the right subtree
            if (this.right === null) {
                this.right = new BST(value);
            } else {
                // Recursively insert into the right subtree
                this.right.insert(value);
            }
        }
    }
}

function minHeightBst(array) {
    return constructMinHeightBst(array, null, 0, array.length - 1);
}

function constructMinHeightBst(array, bst, startIdx, endIdx) {
    // Base case: if end index is less than start index, stop the recursion
    if (endIdx < startIdx) return null;

    const midIdx = Math.floor((startIdx + endIdx) / 2);
    bst = new BST(array[midIdx]);

    // Recursively construct the left and right subtrees
    bst.left = constructMinHeightBst(array, bst.left, startIdx, midIdx - 1);
    bst.right = constructMinHeightBst(array, bst.right, midIdx + 1, endIdx);

    return bst;
}

// Dummy data to test the function
const array = [1, 2, 5, 7, 10, 13, 14, 15, 22];

// Creating the minimal height BST from the sorted array
const bst = minHeightBst(array);

// The resulting BST will have a balanced structure with minimal height
console.log(bst);
