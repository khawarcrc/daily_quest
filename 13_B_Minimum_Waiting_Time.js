function minimumWaitingTime(queries) {
    // Sort the queries in ascending order
    queries.sort((a, b) => a - b);
    console.log(`Sorted Queries: ${queries}`);
    
    let totalWaitingTime = 0;
  
    // Loop through each query
    for (let idx = 0; idx < queries.length; idx++) {
      let duration = queries[idx];
  
      // Calculate the number of queries left after the current one
      let queriesLeft = queries.length - (idx + 1);
      console.log(
        `Query ${idx + 1} with duration ${duration}: Queries left after this = ${queriesLeft}`
      );
  
      // Calculate the total waiting time
      totalWaitingTime += duration * queriesLeft;
      console.log(`Current total waiting time: ${totalWaitingTime}`);
    }
  
    return totalWaitingTime;
  }
  
  // Example usage
  const queries = [3, 2, 1, 2, 6];
  console.log(`Minimum waiting time for queries ${queries}: ${minimumWaitingTime(queries)}`);
  