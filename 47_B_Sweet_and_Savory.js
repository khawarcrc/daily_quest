// Context:
// You are managing a web application that runs on multiple servers.
// Each server has a different capacity to handle requests, represented as positive values (e.g., 10, 20, 30 requests per second).
// Backup servers, which are temporarily offline, have negative values indicating their load reduction capabilities (e.g., -5, -10, -15).
// The objective is to optimize the total load on the servers, ensuring that the combined request capacity of active servers and the load reduction from backup servers is as close as possible to a defined target load without exceeding it.

// Purpose:
// The purpose of the function is to find a pair of one active server and one backup server 
// such that their combined capability is as close as possible to the target load without exceeding it.
// This helps maintain efficiency in resource allocation, ensuring servers do not become overwhelmed 
// while maximizing system performance and maintaining high availability in a distributed environment.


function optimizeServerLoad(servers, targetLoad) {
    // Separate active servers (positive values) and backup servers (negative values)
    const activeServers = servers.filter(server => server > 0).sort((a, b) => a - b); // Sort in ascending order
    const backupServers = servers.filter(server => server < 0).sort((a, b) => Math.abs(a) - Math.abs(b)); // Sort by absolute values for efficiency

    // Initialize best pair and smallest difference
    let bestPair = [0, 0];
    let bestDifference = Infinity; // Infinite as initial comparison value
    let activeIndex = 0, backupIndex = 0; // Two pointers for active and backup servers

    // Use a two-pointer technique to find the closest sum <= targetLoad
    while (activeIndex < activeServers.length && backupIndex < backupServers.length) {
        const currentLoad = activeServers[activeIndex] + backupServers[backupIndex]; // Sum of the current active and backup server

        // Check if the current load is less than or equal to the target load
        if (currentLoad <= targetLoad) {
            const currentDifference = targetLoad - currentLoad; // Calculate how close the load is to the target

            // If the difference is smaller than the best difference found so far, update best pair
            if (currentDifference < bestDifference) {
                bestDifference = currentDifference; // Update the best difference
                bestPair = [activeServers[activeIndex], backupServers[backupIndex]]; // Update the best pair
            }

            // Move the backup pointer to explore the next server (since currentLoad <= targetLoad)
            backupIndex++;
        } else {
            // If the current load exceeds the target load, move the active pointer to reduce the load
            activeIndex++;
        }
    }

    return bestPair;
}

// Dummy data example
const servers = [10, 20, 30, -5, -10, -15];
const targetLoad = 25;

console.log(optimizeServerLoad(servers, targetLoad));  // Expected output: [20, -10] or any valid pair where the sum is <= 25
