function moveElementToEnd(array, toMove) {
    let pointerOne = 0;  // Start of the array
    let pointerTwo = array.length - 1;  // End of the array

    while (pointerOne < pointerTwo) {
        // If the element at pointerTwo is equal to toMove, move pointerTwo left
        if (array[pointerTwo] === toMove) {
            pointerTwo--;
        } 
        // If the element at pointerOne is toMove, swap with pointerTwo
        else if (array[pointerOne] === toMove) {
            [array[pointerOne], array[pointerTwo]] = [array[pointerTwo], array[pointerOne]];
            pointerOne++;
        } 
        // If pointerOne is not toMove, simply move it right
        else {
            pointerOne++;
        }
    }
    
    return array;
}

// Example usage
let array = [2, 1, 2, 2, 3, 4, 2];
let toMove = 2;

let result = moveElementToEnd(array, toMove);
console.log(result);  // Output: [4, 1, 3, 2, 2, 2, 2]
