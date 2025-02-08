class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    print(f"Starting search for the youngest common ancestor of {descendantOne.name} and {descendantTwo.name}.")
    
    # Get depths of both descendants from the top ancestor
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    print(f"Depth of {descendantOne.name} from {topAncestor.name}: {depthOne}")
    print(f"Depth of {descendantTwo.name} from {topAncestor.name}: {depthTwo}")
    
    # Align the descendants at the same level in the ancestral tree
    if depthOne > depthTwo:
        print(f"{descendantOne.name} is deeper than {descendantTwo.name}. Moving {descendantOne.name} up by {depthOne - depthTwo} levels.")
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        print(f"{descendantTwo.name} is deeper than {descendantOne.name}. Moving {descendantTwo.name} up by {depthTwo - depthOne} levels.")
        return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
    # Calculate the depth of the descendant relative to the top ancestor
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backTrackAncestralTree(lowerDescendant, higherDescendant, diff):
    # Move the lower descendant up by the depth difference
    while diff > 0:
        print(f"Moving {lowerDescendant.name} up to its ancestor {lowerDescendant.ancestor.name}")
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    
    # Traverse upwards until both descendants meet at the common ancestor
    while lowerDescendant != higherDescendant:
        print(f"Current descendants: {lowerDescendant.name} and {higherDescendant.name}")
        print(f"Moving both {lowerDescendant.name} and {higherDescendant.name} up to their ancestors.")
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    
    print(f"Youngest common ancestor found: {lowerDescendant.name}")
    return lowerDescendant

# Dummy data setup
# Creating nodes for the ancestral tree
A = AncestralTree("A")  # Top ancestor
B = AncestralTree("B")
C = AncestralTree("C")
D = AncestralTree("D")
E = AncestralTree("E")
F = AncestralTree("F")
G = AncestralTree("G")
H = AncestralTree("H")
I = AncestralTree("I")

# Setting up ancestor relationships
B.ancestor = A
C.ancestor = A
D.ancestor = B
E.ancestor = B
F.ancestor = C
G.ancestor = C
H.ancestor = D
I.ancestor = D

# Testing the function with descendants H and I
youngestCommonAncestor = getYoungestCommonAncestor(A, H, I)
print("Youngest Common Ancestor:", youngestCommonAncestor.name)  # Expected Output: "D"
