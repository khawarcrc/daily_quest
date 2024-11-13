class AncestralTree {
    constructor(name) {
        this.name = name;
        this.ancestor = null;
    }
}

function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
    console.log(`Finding youngest common ancestor of ${descendantOne.name} and ${descendantTwo.name} with top ancestor ${topAncestor.name}`);

    // Get depths of both descendants from the top ancestor
    const depthOne = getDescendantDepth(descendantOne, topAncestor);
    const depthTwo = getDescendantDepth(descendantTwo, topAncestor);

    console.log(`${descendantOne.name} is at depth ${depthOne} and ${descendantTwo.name} is at depth ${depthTwo}`);

    // Align the descendants at the same level in the ancestral tree
    if (depthOne > depthTwo) {
        console.log(`${descendantOne.name} is deeper, moving it up by ${depthOne - depthTwo} levels`);
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo);
    } else {
        console.log(`${descendantTwo.name} is deeper, moving it up by ${depthTwo - depthOne} levels`);
        return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne);
    }
}

function getDescendantDepth(descendant, topAncestor) {
    // Calculate the depth of the descendant relative to the top ancestor
    let depth = 0;
    console.log(`Calculating depth for ${descendant.name} from top ancestor ${topAncestor.name}`);
    while (descendant !== topAncestor) {
        depth += 1;
        descendant = descendant.ancestor;
        console.log(`Moving up to ancestor ${descendant ? descendant.name : "none"}; Current depth: ${depth}`);
    }
    console.log(`Final depth of ${descendant.name} from ${topAncestor.name}: ${depth}`);
    return depth;
}

function backTrackAncestralTree(lowerDescendant, higherDescendant, diff) {
    console.log(`Backtracking to align ${lowerDescendant.name} with ${higherDescendant.name} by moving up ${diff} levels`);
    
    // Move the lower descendant up by the depth difference
    while (diff > 0) {
        lowerDescendant = lowerDescendant.ancestor;
        diff -= 1;
        console.log(`Moved up ${lowerDescendant.name}; Remaining difference: ${diff}`);
    }

    // Traverse upwards until both descendants meet at the common ancestor
    while (lowerDescendant !== higherDescendant) {
        console.log(`Current ancestors - ${lowerDescendant.name} and ${higherDescendant.name}; moving up one level`);
        lowerDescendant = lowerDescendant.ancestor;
        higherDescendant = higherDescendant.ancestor;
    }

    console.log(`Found youngest common ancestor: ${lowerDescendant.name}`);
    return lowerDescendant;
}

// Dummy data setup
// Creating nodes for the ancestral tree
const A = new AncestralTree("A");  // Top ancestor
const B = new AncestralTree("B");
const C = new AncestralTree("C");
const D = new AncestralTree("D");
const E = new AncestralTree("E");
const F = new AncestralTree("F");
const G = new AncestralTree("G");
const H = new AncestralTree("H");
const I = new AncestralTree("I");

// Setting up ancestor relationships
B.ancestor = A;
C.ancestor = A;
D.ancestor = B;
E.ancestor = B;
F.ancestor = C;
G.ancestor = C;
H.ancestor = D;
I.ancestor = D;

// Testing the function with descendants H and I
const youngestCommonAncestor = getYoungestCommonAncestor(A, H, I);
console.log("Youngest Common Ancestor:", youngestCommonAncestor.name);  // Output should be "D"
