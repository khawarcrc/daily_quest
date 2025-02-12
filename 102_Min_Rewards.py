# ============================================================
# PROBLEM STATEMENT:
# ============================================================
# You are given a list of student scores (not sorted).
# You want to assign rewards to each student such that:
#
# 1. Every student must receive at least 1 reward.
# 2. Any student with a higher score than their adjacent student
#    must receive strictly more rewards than that neighbor.
#
# Goal:
# Return the minimum total number of rewards required.
#
# Example:
# scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
# Output = 25
#
# ------------------------------------------------------------


# ============================================================
# EXECUTION FLOW (STEP-BY-STEP LOGIC):
# ============================================================
# Step 1: Initialize rewards array
# - Give each student 1 reward initially
# - Because every student must get at least one
#
# Step 2: Left → Right Pass
# - Traverse from index 1 to end
# - If current score > previous score:
#     increase reward by 1 compared to previous
#
# Step 3: Right → Left Pass
# - Traverse from second last index to start
# - If current score > next score:
#     ensure reward is greater than next student
#     (use max to avoid overwriting previous correct value)
#
# Step 4: Sum all rewards
# - Return total rewards
#
# ------------------------------------------------------------





# ============================================================
# IMPLEMENTATION:
# ============================================================

def minRewards(scores):
    # Step 1: initialize all rewards = 1
    rewards = [1] * len(scores)

    # Step 2: left to right pass
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    # Step 3: right to left pass
    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    # Step 4: return total rewards
    return sum(rewards)



# ============================================================
# THEORY / CONCEPT:
# ============================================================
# This is a GREEDY ALGORITHM problem.
#
# Why Greedy?
# - We make locally optimal decisions (adjust rewards based on neighbors)
# - These local decisions lead to global optimal solution
#
# Key Idea:
# - Each student depends only on adjacent students
# - We must satisfy BOTH directions:
#     → Left neighbor condition
#     → Right neighbor condition
#
# Why Two Passes?
# - First pass ensures left condition
# - Second pass ensures right condition
# - Single pass is NOT enough because:
#     fixing one side may break the other
#
# Why max() in second pass?
# - To preserve the higher reward if already assigned
#
# Time Complexity:
# - O(n) → two linear traversals
#
# Space Complexity:
# - O(n) → rewards array
#
# ------------------------------------------------------------