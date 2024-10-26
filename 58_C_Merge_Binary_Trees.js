class BinaryTree {
    constructor(value, left = null, right = null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}

function mergeBinaryTrees(tree1, tree2) {
    if (tree1 === null) {
        return tree2;
    }

    const tree1Stack = [tree1];
    const tree2Stack = [tree2];

    while (tree1Stack.length > 0) {
        const tree1Node = tree1Stack.pop();
        const tree2Node = tree2Stack.pop();

        if (tree2Node === null) {
            continue;
        }

        tree1Node.value += tree2Node.value;

        if (tree1Node.left === null) {
            tree1Node.left = tree2Node.left;
        } else {
            tree1Stack.push(tree1Node.left);
            tree2Stack.push(tree2Node.left);
        }

        if (tree1Node.right === null) {
            tree1Node.right = tree2Node.right;
        } else {
            tree1Stack.push(tree1Node.right);
            tree2Stack.push(tree2Node.right);
        }
    }

    return tree1;
}

// Helper function to convert the tree structure to an object format
function treeToObject(node) {
    if (node === null) {
        return null;
    }

    return {
        value: node.value,
        left: treeToObject(node.left),
        right: treeToObject(node.right)
    };
}

// Dummy data to demonstrate the merge function
const tree1 = new BinaryTree(1);
tree1.left = new BinaryTree(3);
tree1.right = new BinaryTree(2);
tree1.left.left = new BinaryTree(5);

const tree2 = new BinaryTree(2);
tree2.left = new BinaryTree(1);
tree2.right = new BinaryTree(3);
tree2.left.right = new BinaryTree(4);
tree2.right.right = new BinaryTree(7);

// Merge trees
const mergedTree = mergeBinaryTrees(tree1, tree2);

// Convert merged tree to an object format
const mergedTreeObject = treeToObject(mergedTree);
console.log("Merged Tree in Object Format:", JSON.stringify(mergedTreeObject, null, 4));
