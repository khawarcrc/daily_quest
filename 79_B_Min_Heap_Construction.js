class MinHeap {
    constructor(array) {
        console.log("Initializing MinHeap with array:", array);
        this.heap = this.buildHeap(array);
        console.log("Heap built:", this.heap);
    }

    buildHeap(array) {
        console.log("Building MinHeap from array:", array);
        const firstParentIdx = Math.floor((array.length - 2) / 2);
        for (let currentIdx = firstParentIdx; currentIdx >= 0; currentIdx--) {
            console.log(`Sifting down node at index ${currentIdx}`);
            this.siftDown(currentIdx, array.length - 1, array);
            console.log("Heap after sifting down:", array);
        }
        return array;
    }

    siftDown(currentIdx, endIdx, heap) {
        let childOneIdx = currentIdx * 2 + 1;
        while (childOneIdx <= endIdx) {
            const childTwoIdx = currentIdx * 2 + 2 <= endIdx ? currentIdx * 2 + 2 : -1;
            let idxToSwap;

            if (childTwoIdx !== -1 && heap[childTwoIdx] < heap[childOneIdx]) {
                idxToSwap = childTwoIdx;
            } else {
                idxToSwap = childOneIdx;
            }

            if (heap[idxToSwap] < heap[currentIdx]) {
                console.log(`Swapping ${heap[currentIdx]} with ${heap[idxToSwap]}`);
                this.swap(currentIdx, idxToSwap, heap);
                currentIdx = idxToSwap;
                childOneIdx = currentIdx * 2 + 1;
            } else {
                return;
            }
        }
    }

    siftUp(currentIdx, heap) {
        let parentIdx = Math.floor((currentIdx - 1) / 2);
        while (currentIdx > 0 && heap[currentIdx] < heap[parentIdx]) {
            console.log(`Sifting up: Swapping ${heap[currentIdx]} with ${heap[parentIdx]}`);
            this.swap(currentIdx, parentIdx, heap);
            currentIdx = parentIdx;
            parentIdx = Math.floor((currentIdx - 1) / 2);
        }
    }

    peek() {
        console.log("Peek called: Current minimum value is:", this.heap[0]);
        return this.heap[0];
    }

    remove() {
        console.log("Removing minimum value:", this.heap[0]);
        this.swap(0, this.heap.length - 1, this.heap);
        const valueToRemove = this.heap.pop();
        console.log("Heap after removing root and before sifting down:", this.heap);
        this.siftDown(0, this.heap.length - 1, this.heap);
        console.log("Heap after sifting down:", this.heap);
        return valueToRemove;
    }

    insert(value) {
        console.log(`Inserting value: ${value}`);
        this.heap.push(value);
        console.log("Heap after adding value and before sifting up:", this.heap);
        this.siftUp(this.heap.length - 1, this.heap);
        console.log("Heap after sifting up:", this.heap);
    }

    swap(i, j, heap) {
        [heap[i], heap[j]] = [heap[j], heap[i]];
    }
}

// Example usage
const array = [9, 5, 6, 2, 3, 8, 7, 1, 4];

// Create a MinHeap from the array
const minHeap = new MinHeap(array);

console.log("Heapified array (MinHeap):", minHeap.heap);

// Insert a new value into the heap
minHeap.insert(0);
console.log("Heap after inserting 0:", minHeap.heap);

// Peek at the minimum value
minHeap.peek();

// Remove the minimum value from the heap
const removedValue = minHeap.remove();
console.log("Removed value:", removedValue);
console.log("Heap after removing the minimum value:", minHeap.heap);
