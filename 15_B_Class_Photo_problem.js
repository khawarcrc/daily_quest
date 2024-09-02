function classPhotos(redShirtsHeight, blueShirtsHeight) {
    // Sort both arrays in descending order
    redShirtsHeight.sort((a, b) => b - a);
    blueShirtsHeight.sort((a, b) => b - a);
    
    console.log("Sorted Red Shirts:", redShirtsHeight);
    console.log("Sorted Blue Shirts:", blueShirtsHeight);
    
    // Determine which shirt color will be in the first row
    const shirtInFirstRow = redShirtsHeight[0] < blueShirtsHeight[0] ? 'Red' : 'Blue';
    console.log("Shirts in First Row:", shirtInFirstRow);
    
    // Compare heights to ensure the correct row is taller
    for (let idx = 0; idx < redShirtsHeight.length; idx++) {
        const redShirtHeight = redShirtsHeight[idx];
        const blueShirtHeight = blueShirtsHeight[idx];
        
        console.log(`Comparing heights: Red(${redShirtHeight}) vs Blue(${blueShirtHeight})`);
        
        if (shirtInFirstRow === 'Red') {
            if (redShirtHeight >= blueShirtHeight) {
                console.log("Failed: Red shirt is not shorter");
                return false;
            }
        } else {
            if (blueShirtHeight >= redShirtHeight) {
                console.log("Failed: Blue shirt is not shorter");
                return false;
            }
        }
    }
    
    console.log("Passed all checks");
    return true;
}

const redShirtsHeight = [5, 8, 1, 3, 4];
const blueShirtsHeight = [6, 9, 2, 4, 5];

console.log(classPhotos(redShirtsHeight, blueShirtsHeight));  // Expected Output: true
