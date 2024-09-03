function optimalFreelancing(jobs) {
    const LENGTH_OF_WEEK = 7;  // Define the number of days in a week
    let profit = 0;  // Initialize the total profit to 0
    
    // Sort the jobs in descending order by payment to prioritize higher paying jobs first
    jobs.sort((a, b) => b.payment - a.payment);
    console.log("Sorted Jobs by Payment:", jobs);  // Print the sorted jobs

    // Create an array representing each day of the week, initialized to false (indicating each day is free)
    const timeline = Array(LENGTH_OF_WEEK).fill(false);
    console.log("Initial Timeline:", timeline);  // Print the initial timeline

    // Iterate through each job in the sorted list
    for (const job of jobs) {
        // Determine the latest possible day for scheduling the job
        let maxTime = Math.min(job.deadline, LENGTH_OF_WEEK);
        console.log(`Processing Job: ${JSON.stringify(job)} (Deadline: ${job.deadline}, Payment: ${job.payment})`);

        // Find the latest available day before or on the deadline
        for (let time = maxTime - 1; time >= 0; time--) {
            if (!timeline[time]) {  // Check if the current day is free
                timeline[time] = true;  // Mark this day as occupied
                profit += job.payment;  // Add the job's payment to the total profit
                console.log(`Scheduled Job on Day ${time}: ${JSON.stringify(job)}`);  // Print which day the job is scheduled on
                console.log("Updated Timeline:", timeline);  // Print the updated timeline
                console.log("Current Profit:", profit);  // Print the current profit
                break;  // Exit the loop once the job is scheduled
            }
        }
    }
    
    return profit;  // Return the total profit after scheduling all possible jobs
}

// Dummy data to test the function
const jobs = [
    { deadline: 2, payment: 50 },  // Job 1: Can be completed within 2 days, pays 50
    { deadline: 1, payment: 20 },  // Job 2: Can be completed within 1 day, pays 20
    { deadline: 2, payment: 100 }, // Job 3: Can be completed within 2 days, pays 100
    { deadline: 3, payment: 30 },  // Job 4: Can be completed within 3 days, pays 30
    { deadline: 5, payment: 60 },  // Job 5: Can be completed within 5 days, pays 60
];

// Call the function with the dummy data and print the result
console.log("Total Profit:", optimalFreelancing(jobs));  // Output should be 210 (100 + 50 + 60)
