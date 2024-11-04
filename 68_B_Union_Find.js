// Problem Statement:
// The Union-Find data structure, also known as Disjoint Set Union (DSU), is used to manage 
// and merge disjoint sets. It supports two primary operations:
// 1. `find`: Determine the root representative of the set to which a particular element belongs.
// 2. `union`: Merge two sets containing different elements, uniting them into a single set.
//
// In this code, `createSet` initializes a new set for a single element. `find` uses path compression 
// to keep the tree structure flat, speeding up future find operations. `union` uses union by rank 
// to attach the smaller tree under the larger tree, optimizing the overall structure.
//
// Code Execution Theory:
// 1. We first initialize an instance of `UnionFind`, which sets up empty dictionaries for `parents` 
//    and `rank`.
// 2. Using `createSet`, we create individual sets for elements 1, 2, 3, and 4. Each element is 
//    its own parent, representing a unique set.
// 3. Calling `union(1, 2)` merges the sets containing elements 1 and 2, making one the parent of 
//    the other based on their ranks.
// 4. `union(3, 4)` performs a similar operation for elements 3 and 4.
// 5. Finally, `union(2, 4)` merges the sets containing 1, 2, 3, and 4 into one set.
// 6. Using `find`, we confirm the representative of any element’s set, checking if elements 
//    belong to the same group and retrieving the set root.

class UnionFind {
    constructor() {
        // Initialize dictionaries for parent pointers and rank (used for balancing)
        this.parents = {};
        this.rank = {};
    }

    createSet(value) {
        // Creates a new set containing a single element 'value'
        // Initially, each element is its own parent, and rank is set to 0
        this.parents[value] = value;
        this.rank[value] = 0;
    }

    find(value) {
        // Returns the root representative of the set containing 'value'
        // Path compression is used to make future finds faster
        if (!(value in this.parents)) {
            return null;
        }
        if (value !== this.parents[value]) {
            this.parents[value] = this.find(this.parents[value]);  // Path compression
        }
        return this.parents[value];
    }

    union(valueOne, valueTwo) {
        // Merges the sets containing 'valueOne' and 'valueTwo' if they are disjoint
        // Uses union by rank to keep the tree flat
        if (!(valueOne in this.parents) || !(valueTwo in this.parents)) {
            return;
        }
        let valueOneRoot = this.find(valueOne);
        let valueTwoRoot = this.find(valueTwo);
        
        // If they are in the same set, no need to union
        if (valueOneRoot === valueTwoRoot) {
            return;
        }
        
        // Union by rank
        if (this.rank[valueOneRoot] < this.rank[valueTwoRoot]) {
            this.parents[valueOneRoot] = valueTwoRoot;
        } else if (this.rank[valueOneRoot] > this.rank[valueTwoRoot]) {
            this.parents[valueTwoRoot] = valueOneRoot;
        } else {
            this.parents[valueTwoRoot] = valueOneRoot;
            this.rank[valueOneRoot] += 1;
        }
    }
}

// Dummy data and usage example
const uf = new UnionFind();
uf.createSet(1);
uf.createSet(2);
uf.createSet(3);
uf.createSet(4);

uf.union(1, 2);  // Union sets containing 1 and 2
uf.union(3, 4);  // Union sets containing 3 and 4
uf.union(2, 4);  // Union sets containing 2 and 4 (connects 1, 2, 3, and 4 into one set)

// Check the root parent of each element
console.log(uf.find(1));  // Should return the representative of the set containing 1
console.log(uf.find(3));  // Should return the representative of the set containing 3
