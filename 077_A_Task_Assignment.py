# Problem Statement:
# ------------------
# You are given `k` pairs of tasks, and each task has a specific duration. 
# The goal is to assign the tasks into pairs such that each pair consists of two tasks 
# and the sum of their durations is minimized. 
# Your task is to return the indices of the paired tasks.

# Input:
# - An integer `k` representing the number of pairs of tasks.
# - A list `tasks` containing integers, where each integer represents the duration of a task.

# Output:
# - A list of `k` pairs, where each pair contains the indices of the two tasks that are paired together.

# Problem Explanation:
# ---------------------
# 1. Tasks with the smallest duration should be paired with tasks having the largest duration 
#    to balance the sum of the durations for each pair.
# 2. Sorting the task durations allows efficient pairing:
#    - The smallest duration is paired with the largest.
#    - The second smallest is paired with the second largest, and so on.
# 3. To keep track of the original indices of the tasks after sorting:
#    - A dictionary maps each task duration to its list of indices.
#    - When a task duration is used for pairing, its corresponding index is removed from the dictionary.

# Code Execution Theory:
# -----------------------
# 1. Create a dictionary `taskDurationsToIndices`:
#    - Map each task duration to a list of its indices in the original `tasks` list.
#    - This helps retrieve the indices even after the `tasks` list is sorted.
# 2. Sort the `tasks` list to prepare for optimal pairing of durations.
# 3. Initialize an empty list `pairedTasks` to store the pairs of task indices.
# 4. Iterate `k` times to form `k` pairs:
#    - In each iteration, select the smallest unpaired task (from the sorted list) 
#      and retrieve its index from `taskDurationsToIndices`.
#    - Select the largest unpaired task (from the sorted list) and retrieve its index.
#    - Add the pair of indices to `pairedTasks`.
# 5. Return the `pairedTasks` list as the final result.

# Example:
# --------
# Input:
# - `tasks = [4, 2, 8, 1, 7, 3]`
# - `k = 3` (since there are 6 tasks, 3 pairs are required).
# 
# Execution Steps:
# - Create a dictionary mapping task durations to indices: `{4: [0], 2: [1], 8: [2], 1: [3], 7: [4], 3: [5]}`
# - Sort the `tasks` list: `[1, 2, 3, 4, 7, 8]`
# - Form pairs by iterating:
#    - Pair smallest (1) with largest (8), record indices `[3, 2]`.
#    - Pair next smallest (2) with next largest (7), record indices `[1, 4]`.
#    - Pair next smallest (3) with next largest (4), record indices `[5, 0]`.
# - Return the pairs: `[[3, 2], [1, 4], [5, 0]]`.

# Complexity Analysis:
# ---------------------
# 1. Time Complexity:
#    - Sorting the tasks: O(n log n), where `n` is the length of `tasks`.
#    - Iterating `k` times to form pairs: O(k).
#    - Overall: O(n log n) (since sorting dominates).
# 2. Space Complexity:
#    - The dictionary `taskDurationsToIndices` and the result list `pairedTasks` require O(n) space.



def taskAssignment(k, tasks):
    # Initialize a list to store the pairs of task indices
    pairedTasks = []

    # Create a dictionary to map task durations to their indices
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    # Sort the task durations to allow pairing from smallest to largest
    sortedTasks = sorted(tasks)

    # Iterate over the first k tasks to create pairs
    for idx in range(k):
        # Get the smallest duration task (task1) and its index
        task1Duration = sortedTasks[idx]
        indicesWithTask1Duration = taskDurationsToIndices[task1Duration]
        task1Index = indicesWithTask1Duration.pop()

        # Get the largest duration task (task2) and its index
        task2SortedIndex = len(tasks) - 1 - idx  # Get the index of the largest unpaired task
        task2Duration = sortedTasks[task2SortedIndex]
        indicesWithTask2Duration = taskDurationsToIndices[task2Duration]
        task2Index = indicesWithTask2Duration.pop()

        # Add the pair of indices to the result
        pairedTasks.append([task1Index, task2Index])

    # Return the list of paired task indices
    return pairedTasks

# Helper function to create a dictionary mapping task durations to indices
def getTaskDurationsToIndices(tasks):
    # Initialize an empty dictionary
    tasksDurationsToIndices = {}

    # Loop through each task and its index
    for idx, taskDuration in enumerate(tasks):
        # If the duration is already in the dictionary, add the index to the list
        if taskDuration in tasksDurationsToIndices:
            tasksDurationsToIndices[taskDuration].append(idx)
        else:
            # Otherwise, create a new entry with the index in a list
            tasksDurationsToIndices[taskDuration] = [idx]

    # Return the dictionary
    return tasksDurationsToIndices


# Dummy data for testing the function
tasks = [4, 2, 8, 1, 7, 3]
k = len(tasks) // 2  # Number of pairs needed (half the number of tasks)

# Call the function and print the result
result = taskAssignment(k, tasks)
print("Paired tasks:", result)
