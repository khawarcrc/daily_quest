function arrayOfProducts(array) {
    // Initialize products array with 1s
    let products = new Array(array.length).fill(1);

    // Outer loop to go through each element in the array
    for (let i = 0; i < array.length; i++) {
        let runningProduct = 1;  // Initialize runningProduct for each element
        
        // Inner loop to calculate the product of all elements except the one at index i
        for (let j = 0; j < array.length; j++) {
            if (i !== j) {  // Only multiply elements other than the one at index i
                runningProduct *= array[j];
            }
        }
        
        // Store the result in products[i]
        products[i] = runningProduct;
    }
    
    // Return the final products array
    return products;
}

// Dummy data
let array = [1, 2, 3, 4];

// Call the function and print the final result
let result = arrayOfProducts(array);
console.log("Final result:", result);
