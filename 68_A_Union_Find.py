# Problem Statement:
# The Union-Find data structure, also known as Disjoint Set Union (DSU), is used to manage 
# and merge disjoint sets. It supports two primary operations:
# 1. `find`: Determine the root representative of the set to which a particular element belongs.
# 2. `union`: Merge two sets containing different elements, uniting them into a single set.
# 
# In this code, `createSet` initializes a new set for a single element. `find` uses path compression 
# to keep the tree structure flat, speeding up future find operations. `union` uses union by rank 
# to attach the smaller tree under the larger tree, optimizing the overall structure.
#
# Code Execution Theory:
# 1. We first initialize an instance of `UnionFind`, which sets up empty dictionaries for `parents` 
#    and `rank`.
# 2. Using `createSet`, we create individual sets for elements 1, 2, 3, and 4. Each element is 
#    its own parent, representing a unique set.
# 3. Calling `union(1, 2)` merges the sets containing elements 1 and 2, making one the parent of 
#    the other based on their ranks.
# 4. `union(3, 4)` performs a similar operation for elements 3 and 4.
# 5. Finally, `union(2, 4)` merges the sets containing 1, 2, 3, and 4 into one set.
# 6. Using `find`, we confirm the representative of any element’s set, checking if elements 
#    belong to the same group and retrieving the set root.



class UnionFind:
    def __init__(self):
        # Initialize dictionaries for parent pointers and rank (used for balancing)
        self.parents = {}
        self.rank = {}

    def createSet(self, value):
        # Creates a new set containing a single element 'value'
        # Initially, each element is its own parent, and rank is set to 0
        self.parents[value] = value
        self.rank[value] = 0

    def find(self, value):
        # Returns the root representative of the set containing 'value'
        # Path compression is used to make future finds faster
        if value not in self.parents:
            return None
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])  # Path compression
        return self.parents[value]

    def union(self, valueOne, valueTwo):
        # Merges the sets containing 'valueOne' and 'valueTwo' if they are disjoint
        # Uses union by rank to keep the tree flat
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        
        # If they are in the same set, no need to union
        if valueOneRoot == valueTwoRoot:
            return
        
        # Union by rank
        if self.rank[valueOneRoot] < self.rank[valueTwoRoot]:
            self.parents[valueOneRoot] = valueTwoRoot
        elif self.rank[valueOneRoot] > self.rank[valueTwoRoot]:
            self.parents[valueTwoRoot] = valueOneRoot
        else:
            self.parents[valueTwoRoot] = valueOneRoot
            self.rank[valueOneRoot] += 1

# Dummy data and usage example
uf = UnionFind()
uf.createSet(1)
uf.createSet(2)
uf.createSet(3)
uf.createSet(4)

uf.union(1, 2)  # Union sets containing 1 and 2
uf.union(3, 4)  # Union sets containing 3 and 4
uf.union(2, 4)  # Union sets containing 2 and 4 (connects 1, 2, 3, and 4 into one set)

# Check the root parent of each element
print(uf.find(1))  # Should return the representative of the set containing 1
print(uf.find(3))  # Should return the representative of the set containing 3




# Step-by-Step Code Execution Example:

# 1. **Initialization**
#    - We create an instance of the `UnionFind` class, initializing it with empty dictionaries
#      for `parents` and `rank`. These dictionaries will store the parent pointers and ranks
#      for each element in the sets we create.

# 2. **Creating Sets**
#    - We call `createSet(1)`, `createSet(2)`, `createSet(3)`, and `createSet(4)` to initialize
#      sets for elements 1, 2, 3, and 4.
#    - After each call, each element is its own parent, meaning each forms an individual set:
#         - `parents` will be: `{1: 1, 2: 2, 3: 3, 4: 4}`
#         - `rank` will be: `{1: 0, 2: 0, 3: 0, 4: 0}`
#    - Each element's rank is initialized to 0 since they are individual sets.

# 3. **Union Operation: union(1, 2)**
#    - We want to unite the sets containing elements 1 and 2.
#    - The `find` operation is called on both elements:
#         - `find(1)` returns 1 as the root for element 1.
#         - `find(2)` returns 2 as the root for element 2.
#    - Since 1 and 2 are in different sets (different roots), we perform a union.
#    - Both have the same rank, so we choose 1 to become the parent of 2 and increase the rank of 1:
#         - `parents` becomes `{1: 1, 2: 1, 3: 3, 4: 4}`
#         - `rank` becomes `{1: 1, 2: 0, 3: 0, 4: 0}`
#    - Now, 1 is the root representative for both elements 1 and 2.

# 4. **Union Operation: union(3, 4)**
#    - We now unite the sets containing elements 3 and 4.
#    - `find(3)` returns 3, and `find(4)` returns 4 as their roots.
#    - Since they are in different sets, we perform a union.
#    - Both have the same rank, so we choose 3 to be the parent of 4 and increase the rank of 3:
#         - `parents` becomes `{1: 1, 2: 1, 3: 3, 4: 3}`
#         - `rank` becomes `{1: 1, 2: 0, 3: 1, 4: 0}`
#    - Now, 3 is the root representative for both elements 3 and 4.

# 5. **Union Operation: union(2, 4)**
#    - We attempt to unite the sets containing elements 2 and 4, which indirectly connects all
#      elements into a single set.
#    - We first find the roots of both elements using the `find` operation with path compression:
#         - `find(2)` traces up to 1 as the root (path compression sets `parents[2] = 1`).
#         - `find(4)` traces up to 3 as the root (path compression sets `parents[4] = 3`).
#    - The roots (1 and 3) are different, so we perform a union.
#    - Since both roots have the same rank (1), we choose 1 to become the parent of 3 and increase its rank:
#         - `parents` becomes `{1: 1, 2: 1, 3: 1, 4: 3}`
#         - `rank` becomes `{1: 2, 2: 0, 3: 1, 4: 0}`
#    - All elements (1, 2, 3, and 4) are now connected under a single root, with 1 as their root representative.

# 6. **Find Operation: find(1) and find(3)**
#    - We use the `find` operation to verify that all elements belong to the same set.
#         - `find(1)` directly returns 1 as the root for element 1.
#         - `find(3)` traces up to 1 (after path compression sets `parents[3] = 1`).
#    - Since both `find(1)` and `find(3)` return the same root (1), we confirm that all elements are in the same set.

# **Summary of Final Structure:**
#    - After all operations, the Union-Find structure connects all elements in a single set
#      with element 1 as the root representative.
#    - The `parents` dictionary is `{1: 1, 2: 1, 3: 1, 4: 1}`, indicating a single set.
#    - The `rank` dictionary shows `{1: 2, 2: 0, 3: 1, 4: 0}`, reflecting the height of each subtree
#      (though rank is mainly used for balancing during unions).
