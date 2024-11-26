/**
 * Determines the valid starting city for a circular trip.
 * @param {number[]} distances - List of distances between consecutive cities.
 * @param {number[]} fuel - List of fuel available at each city.
 * @param {number} mpg - Car mileage in miles per gallon.
 * @returns {number} Index of the starting city.
 */
function validStartingCity(distances, fuel, mpg) {
    // Total number of cities
    const numberOfCities = distances.length;

    // Tracks the current fuel miles remaining
    let milesRemaining = 0;

    // Tracks the index of the starting city candidate
    let indexOfStartingCityCandidate = 0;

    // Tracks the minimum miles remaining seen so far
    let milesRemainingAtStartingCityCandidate = 0;

    console.log("Starting computation...");
    console.log(`Number of cities: ${numberOfCities}`);

    // Traverse through all cities
    for (let cityIdx = 1; cityIdx < numberOfCities; cityIdx++) {
        // Calculate distance from the previous city
        const distanceFromPreviousCity = distances[cityIdx - 1];

        // Calculate fuel gained at the previous city
        const fuelFromPreviousCity = fuel[cityIdx - 1];

        // Update miles remaining by adding fuel and subtracting distance
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity;

        console.log(`City ${cityIdx}:`);
        console.log(`  Distance from previous city: ${distanceFromPreviousCity}`);
        console.log(`  Fuel from previous city: ${fuelFromPreviousCity}`);
        console.log(`  Miles remaining: ${milesRemaining}`);

        // If milesRemaining is less than the minimum so far, update starting city
        if (milesRemaining < milesRemainingAtStartingCityCandidate) {
            milesRemainingAtStartingCityCandidate = milesRemaining;
            indexOfStartingCityCandidate = cityIdx;

            console.log(`  Updated starting city candidate to City ${cityIdx}`);
            console.log(`  Minimum miles remaining: ${milesRemainingAtStartingCityCandidate}`);
        }
    }

    console.log("Computation complete.");
    console.log(`Starting city index: ${indexOfStartingCityCandidate}`);
    
    // Return the index of the starting city candidate
    return indexOfStartingCityCandidate;
}

// Dummy data for testing
const distances = [5, 25, 15, 10, 20]; // Distances between consecutive cities
const fuel = [1, 2, 1, 0.5, 3]; // Fuel available at each city
const mpg = 10; // Miles per gallon of the car

// Expected output is the index of the valid starting city
console.log("Result:", validStartingCity(distances, fuel, mpg)); // Example output: 4
