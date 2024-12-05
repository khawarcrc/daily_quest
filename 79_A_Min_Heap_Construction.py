# # Problem Statement:
# The goal is to implement a MinHeap data structure in Python. A MinHeap is a binary tree where:
# 1. The value of each parent node is less than or equal to the values of its child nodes.
# 2. The tree is a complete binary tree, meaning all levels are fully filled except possibly the last,
#    which is filled from left to right.

# The MinHeap should support the following operations:
# - Build a MinHeap from an unordered array.
# - Shift a node down the heap to maintain the MinHeap property.
# - Shift a node up the heap to maintain the MinHeap property.
# - Swap two elements in the heap.


# Explanation of the Problem with an Example:

# 1. **Heap Property**:
#    - In a MinHeap, the smallest element is always at the root (index 0 in an array representation).
#    - Each parent node must be smaller than or equal to its child nodes.
#    - Example:
#      Consider the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`.
#      After converting it into a MinHeap, the array will look like `[1, 2, 6, 3, 5, 8, 7, 9, 4]`.
#      Here, the smallest element `1` is at the root, and every parent node is smaller than its children.

# 2. **Array Representation of a Heap**:
#    - A binary tree can be represented as an array:
#      - The parent of a node at index `i` is at index `(i - 1) // 2`.
#      - The left child of a node at index `i` is at index `2 * i + 1`.
#      - The right child of a node at index `i` is at index `2 * i + 2`.
#    - Example:
#      For the array `[1, 2, 6, 3, 5, 8, 7, 9, 4]`:
#        - The parent of the node at index `3` (value `3`) is at index `(3 - 1) // 2 = 1` (value `2`).
#        - The left child of the node at index `1` (value `2`) is at index `2 * 1 + 1 = 3` (value `3`).
#        - The right child of the node at index `1` (value `2`) is at index `2 * 1 + 2 = 4` (value `5`).

# 3. **Building a MinHeap**:
#    - Start with an unordered array.
#    - Identify the last non-leaf node (first parent node) and sift it down.
#    - Repeat the process for all parent nodes in reverse order (from bottom to top).
#    - Example:
#      For the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`:
#        - The last non-leaf node is at index `(len(array) - 2) // 2 = 3` (value `2`).
#        - Sift down each parent node starting from index `3` to index `0` to build the MinHeap.
#        - Final MinHeap: `[1, 2, 6, 3, 5, 8, 7, 9, 4]`.

# 4. **Sift Down**:
#    - Used to maintain the MinHeap property when a node is larger than its children.
#    - Compare the current node with its children and swap it with the smaller child if necessary.
#    - Continue the process until the node is in the correct position or it has no children.
#    - Example:
#      For the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`:
#        - Start at index `3` (value `2`), compare it with its children at indices `7` (value `1`) and `8` (value `4`).
#        - Swap `2` with `1` (smaller child).
#        - Continue the process for the next parent nodes until the heap property is satisfied.

# 5. **Sift Up**:
#    - Used to maintain the MinHeap property when a new node is added to the heap.
#    - Compare the current node with its parent and swap if the current node is smaller.
#    - Continue the process until the node is in the correct position or it becomes the root.
#    - Example:
#      If we insert `0` into the MinHeap `[1, 2, 6, 3, 5, 8, 7, 9, 4]`:
#        - Append `0` to the end of the array: `[1, 2, 6, 3, 5, 8, 7, 9, 4, 0]`.
#        - Compare `0` with its parent at index `4` (value `5`) and swap.
#        - Continue comparing and swapping until `0` becomes the root.
#        - Final MinHeap: `[0, 1, 6, 3, 2, 8, 7, 9, 4, 5]`.

# 6. **Swap**:
#    - A utility function to exchange two elements in the heap.
#    - Example:
#      If we need to swap elements at indices `0` and `1` in the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`:
#        - After swapping, the array becomes `[5, 9, 6, 2, 3, 8, 7, 1, 4]`.

# # Time Compexity:
# The MinHeap class provides an efficient way to manage a collection of elements where the smallest element is always accessible in O(1) time.
# The operations of building the heap, inserting an element, and removing the minimum element are all efficient, with time complexities of O(n)
# for building the heap and O(log(n)) for insertion and removal.
# """


class MinHeap:
    def __init__(self, array):
        # """
        # Initializes the MinHeap with the given array.
        # The array is transformed into a valid MinHeap using the buildHeap method.
        # """
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        # """
        # Builds a MinHeap from an unordered array.
        # Starts from the first parent node and sifts down each node to ensure the heap property.
        # """
        # Find the index of the first parent node (last non-leaf node)
        firstParentIdx = (len(array) - 2) // 2
        # Sift down each node starting from the first parent node to the root
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        # """
        # Sifts a node down the heap to maintain the MinHeap property.
        # Compares the current node with its children and swaps with the smaller child if necessary.
        # """
        childOneIdx = currentIdx * 2 + 1  # Index of the first child
        while childOneIdx <= endIdx:
            # Index of the second child (if it exists)
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            # Determine which child to swap with (the smaller one)
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            # Swap if the child is smaller than the current node
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                # Update the current index to the swapped child's index
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        # """
        # Sifts a node up the heap to maintain the MinHeap property.
        # Compares the current node with its parent and swaps if necessary.
        # """
        parentIdx = (currentIdx - 1) // 2  # Index of the parent node
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            # Swap the current node with its parent
            self.swap(currentIdx, parentIdx, heap)
            # Update the current index to the parent's index
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        # """
        # Swaps two elements in the heap.
        # """
        heap[i], heap[j] = heap[j], heap[i]


# Dummy data and usage example
if __name__ == "__main__":
    # Example array (unsorted)
    array = [9, 5, 6, 2, 3, 8, 7, 1, 4]

    # Create a MinHeap from the array
    minHeap = MinHeap(array)

    # Print the heapified array
    print("Heapified array (MinHeap):", minHeap.heap)

    # Example of inserting a new value into the heap
    minHeap.heap.append(0)  # Add the new value to the end of the heap
    minHeap.siftUp(
        len(minHeap.heap) - 1, minHeap.heap
    )  # Sift it up to maintain the heap property
    print("Heap after inserting 0:", minHeap.heap)

    # Example of removing the minimum value (root of the heap)
    minHeap.heap[0] = minHeap.heap[-1]  # Replace the root with the last element
    minHeap.heap.pop()  # Remove the last element
    minHeap.siftDown(
        0, len(minHeap.heap) - 1, minHeap.heap
    )  # Sift down to maintain the heap property
    print("Heap after removing the minimum value:", minHeap.heap)


# # Code Execution Theory with Example:

# 1. **Initialization**:
#    - The MinHeap class is initialized with an array.
#    - The `buildHeap` method is called to transform the array into a valid MinHeap.
#    - Example:
#      Input array: `[9, 5, 6, 2, 3, 8, 7, 1, 4]`.
#      Output MinHeap: `[1, 2, 6, 3, 5, 8, 7, 9, 4]`.

# 2. **Building the Heap**:
#    - The `buildHeap` method identifies the first parent node and sifts down each parent node in reverse order.
#    - This ensures that the entire array satisfies the MinHeap property.
#    - Example:
#      Start with the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`.
#      Sift down each parent node to get the MinHeap `[1, 2, 6, 3, 5, 8, 7, 9, 4]`.

# 3. **Sift Down**:
#    - Starting from a given node, the `siftDown` method compares the node with its children.
#    - If the node is larger than the smaller child, it is swapped with that child.
#    - The process continues until the node is in the correct position or it has no children.
#    - Example:
#      For the array `[9, 5, 6, 2, 3, 8, 7, 1, 4]`, sift down the node at index `3` (value `2`):
#        - Compare `2` with its children at indices `7` (value `1`) and `8` (value `4`).
#        - Swap `2` with `1`.
#        - Continue the process for other parent nodes.

# 4. **Sift Up**:
#    - When a new element is added to the heap, it is appended to the end of the array.
#    - The `siftUp` method compares the new element with its parent and swaps if necessary.
#    - The process continues until the new element is in the correct position or it becomes the root.
#    - Example:
#      Insert `0` into the MinHeap `[1, 2, 6, 3, 5, 8, 7, 9, 4]`:
#        - Append `0` to the end: `[1, 2, 6, 3, 5, 8, 7, 9, 4, 0]`.
#        - Compare `0` with its parent at index `4` (value `5`) and swap.
#        - Continue comparing and swapping until `0` becomes the root.
#        - Final MinHeap: `[0, 1, 6, 3, 2, 8, 7, 9, 4, 5]`.

# 5. **Heap Operations**:
#    - After building the heap, the MinHeap can be used to perform operations like inserting a new element or removing the minimum element (root).
#    - Example:
#      - Insert `0` into `[1, 2, 6, 3, 5, 8, 7, 9, 4]` to get `[0, 1, 6, 3, 2, 8, 7, 9, 4, 5]`.
#      - Remove the minimum element `0` to get `[1, 2, 6, 3, 5, 8, 7, 9, 4]`.
# """
