# Problem Statement:
# Given an ancestral tree where each node has a single parent, we need to find the youngest common ancestor
# (closest shared ancestor) of two given descendants in the tree. Each descendant node has a link to its ancestor,
# but no node has direct access to its descendants. The top ancestor is the root of the tree, and every other node
# traces back to it.

# Explanation:
# 1. The tree is structured in such a way that each node has exactly one ancestor (parent).
# 2. For any two given descendant nodes, the youngest common ancestor is the lowest (or closest) ancestor
#    node they both share in their lineage.
# 3. The problem is similar to finding the Lowest Common Ancestor (LCA) in a tree, but here we only have links
#    from a descendant to its ancestor, so we cannot traverse directly to children nodes.

# Approach:
# 1. **Calculate Depths**: First, calculate the "depth" (distance from the top ancestor) for both descendants.
#    This helps in determining which descendant is deeper in the tree.
# 2. **Align Descendants**: If the depths differ, "move up" the deeper descendant until both are at the same level.
#    This ensures that the descendants can traverse in sync towards the common ancestor.
# 3. **Backtrack Upwards**: Starting from the aligned depths, move both descendants upwards until they point to the
#    same ancestor node, which will be the youngest common ancestor.

# Execution Theory:
# 1. `getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo)`:
#    - This is the main function that coordinates finding the youngest common ancestor.
#    - It first calculates the depths of each descendant and aligns them if they are at different levels.
#    - Finally, it backtracks both nodes in sync until they converge at the common ancestor.
# 2. `getDescendantDepth(descendant, topAncestor)`:
#    - This helper function calculates the depth of a given descendant from the top ancestor by counting the steps
#      it takes to reach the top ancestor. Each step moves one ancestor up in the lineage.
# 3. `backTrackAncestralTree(lowerDescendant, higherDescendant, diff)`:
#    # Backtracking Explanation:
# 1. Aligning Depth Levels:
#    - The two descendants may be at different depths in the ancestral tree.
#    - If one descendant is deeper than the other, we need to "move up" the deeper descendant
#      until both descendants are at the same depth level.
#    - This step allows us to position both descendants equally in the tree, ensuring a fair
#      comparison as we continue backtracking.
#
# 2. Tracing Common Lineage:
#    - Once both descendants are at the same depth, we start moving both nodes upwards,
#      one level at a time, simultaneously.
#    - This synchronized backtracking traces each descendant's path toward the root
#      of the tree, checking for a match at each level.
#    - The first common node encountered by both descendants during this process is
#      identified as their youngest common ancestor.
#
# 3. Minimizing Distance to Common Ancestor:
#    - By backtracking from the descendants upwards, we ensure that we find the closest
#      shared ancestor as soon as possible.
#    - Moving from the root downwards instead would be inefficient, as it would require
#      traversing the entire tree or having access to child nodes (which we don't in this structure).
#    - This approach provides an efficient, minimal path to find the youngest shared ancestor.


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Get depths of both descendants from the top ancestor
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)

    # Align the descendants at the same level in the ancestral tree
    if depthOne > depthTwo:
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
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
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1

    # Traverse upwards until both descendants meet at the common ancestor
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor

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
print("Youngest Common Ancestor:", youngestCommonAncestor.name)  # Output should be "D"


# Example Ancestral Tree:
# Consider the following simple ancestral tree structure, where `A` is the top ancestor:
#
#         A
#        / \
#       B   C
#      / \ / \
#     D  E F  G
#    / \
#   H   I
#
# Explanation of Relationships:
# - `A` is the top ancestor, and every other node in the tree has `A` as an ultimate ancestor.
# - `B` and `C` are children of `A`.
# - `D` and `E` are children of `B`, while `F` and `G` are children of `C`.
# - `H` and `I` are children of `D`.
#
# Sample Queries for Youngest Common Ancestor:
# 1. Youngest Common Ancestor of `H` and `I`: Since both are children of `D`, the youngest common ancestor is `D`.
# 2. Youngest Common Ancestor of `H` and `E`: `H` traces back to `D`, and `E` is directly under `B`. Therefore,
#    the youngest common ancestor is `B`.
# 3. Youngest Common Ancestor of `H` and `G`: `H` traces back to `A` through `D` and `B`, while `G` traces back
#    to `A` through `C`. Thus, the youngest common ancestor of `H` and `G` is `A`.
#
# This example shows how different descendant pairs may share ancestors at different levels of the tree.
# The function should determine the lowest shared ancestor for any two given descendants.
