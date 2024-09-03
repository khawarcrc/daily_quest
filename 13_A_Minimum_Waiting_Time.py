# Problem Explanation
# Objective: Calculate the minimum total waiting time for a set of queries, where each query has a specific duration.

# Conditions:
# - Each query must wait for all the queries that come after it to complete.
# - We aim to minimize the total waiting time by optimizing the order of the queries.

# Approach to Solve the Problem

# Step 1: Sort the Queries
# - Sort the list of queries in ascending order of their durations.
# - This ensures that shorter queries are processed first, minimizing the waiting time for longer queries.

# Step 2: Calculate Waiting Time
# - Iterate through the sorted list of queries.
# - For each query, calculate how many queries will still need to be processed after it.
# - Multiply the duration of the current query by the number of remaining queries to determine its contribution to the total waiting time.
# - Sum these contributions to get the total minimum waiting time.

def minnimumWaitingTime(quries):
    quries.sort()
    print(f"Sorted Quries : {quries}")
    totalWaitingTime = 0

    for idx, duration in enumerate(quries):

        # calculate the number of quries left after the current one
        quriesLeft = len(quries) - (idx + 1)
        print(
            f"Query {idx + 1} with duration {duration}: Quries left after this = {quriesLeft}"
        )
        totalWaitingTime += duration * quriesLeft
        print(f"current total waiting time: {totalWaitingTime}")

    return totalWaitingTime


quries = [3, 2, 1, 2, 6]
print(f"Minimum waiting time for quries {quries}: {minnimumWaitingTime(quries)}")
