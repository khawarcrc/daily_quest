/**
 * Function to assign tasks into pairs such that the sum of their durations is minimized.
 * @param {number} k - Number of pairs required.
 * @param {number[]} tasks - List of task durations.
 * @returns {number[][]} - A list of `k` pairs of indices representing the paired tasks.
 */
function taskAssignment(k, tasks) {
    // Initialize a list to store the pairs of task indices
    const pairedTasks = [];

    // Create a mapping of task durations to their indices
    const taskDurationsToIndices = getTaskDurationsToIndices(tasks);

    // Sort the task durations to allow pairing from smallest to largest
    const sortedTasks = [...tasks].sort((a, b) => a - b);

    // Iterate over the first k tasks to create pairs
    for (let idx = 0; idx < k; idx++) {
        // Get the smallest duration task (task1) and its index
        const task1Duration = sortedTasks[idx];
        const task1Index = taskDurationsToIndices[task1Duration].pop();

        // Get the largest duration task (task2) and its index
        const task2Duration = sortedTasks[sortedTasks.length - 1 - idx];
        const task2Index = taskDurationsToIndices[task2Duration].pop();

        // Add the pair of indices to the result
        pairedTasks.push([task1Index, task2Index]);
    }

    // Return the list of paired task indices
    return pairedTasks;
}

/**
 * Helper function to create a mapping of task durations to their indices.
 * @param {number[]} tasks - List of task durations.
 * @returns {Object} - A dictionary mapping each task duration to a list of its indices.
 */
function getTaskDurationsToIndices(tasks) {
    const tasksDurationsToIndices = {};

    // Loop through each task and its index
    tasks.forEach((taskDuration, idx) => {
        // If the duration is already in the dictionary, add the index to the list
        if (tasksDurationsToIndices[taskDuration]) {
            tasksDurationsToIndices[taskDuration].push(idx);
        } else {
            // Otherwise, create a new entry with the index in a list
            tasksDurationsToIndices[taskDuration] = [idx];
        }
    });

    return tasksDurationsToIndices;
}

// Dummy data for testing the function
const tasks = [4, 2, 8, 1, 7, 3];
const k = tasks.length / 2; // Number of pairs needed (half the number of tasks)

// Call the function and print the result
const result = taskAssignment(k, tasks);
console.log("Paired tasks:", result);
