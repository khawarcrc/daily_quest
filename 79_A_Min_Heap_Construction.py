class MinHeap:
    def __init__(self, array):
        """
        Initializes the MinHeap with the given array.
        The array is transformed into a valid MinHeap using the buildHeap method.
        """
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        """
        Builds a MinHeap from an unordered array.
        Starts from the first parent node and sifts down each node to ensure the heap property.
        """
        # Find the index of the first parent node (last non-leaf node)
        firstParentIdx = (len(array) - 2) // 2
        # Sift down each node starting from the first parent node to the root
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        """
        Sifts a node down the heap to maintain the MinHeap property.
        Compares the current node with its children and swaps with the smaller child if necessary.
        """
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
        """
        Sifts a node up the heap to maintain the MinHeap property.
        Compares the current node with its parent and swaps if necessary.
        """
        parentIdx = (currentIdx - 1) // 2  # Index of the parent node
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            # Swap the current node with its parent
            self.swap(currentIdx, parentIdx, heap)
            # Update the current index to the parent's index
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def swap(self, i, j, heap):
        """
        Swaps two elements in the heap.
        """
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
    minHeap.siftUp(len(minHeap.heap) - 1, minHeap.heap)  # Sift it up to maintain the heap property
    print("Heap after inserting 0:", minHeap.heap)

    # Example of removing the minimum value (root of the heap)
    minHeap.heap[0] = minHeap.heap[-1]  # Replace the root with the last element
    minHeap.heap.pop()  # Remove the last element
    minHeap.siftDown(0, len(minHeap.heap) - 1, minHeap.heap)  # Sift down to maintain the heap property
    print("Heap after removing the minimum value:", minHeap.heap)