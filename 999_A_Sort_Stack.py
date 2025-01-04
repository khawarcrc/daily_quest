# ------------------------------------------------------------
# PROBLEM STATEMENT:
# ------------------------------------------------------------
# You are given a stack (implemented as a Python list), where
# elements follow the "Last In, First Out (LIFO)" principle.
#
# Task:
# Sort the stack in ascending order (smallest at the bottom,
# largest at the top) using ONLY stack operations and recursion.
#
# Restrictions:
# - You cannot use extra data structures like arrays or queues
#   for sorting.
# - You can only use stack operations: push, pop, peek, isEmpty.
#
# Goal:
# Implement a recursive algorithm that sorts the stack.
# ------------------------------------------------------------


# ------------------------------------------------------------
# EXPLANATION OF THE PROBLEM:
# ------------------------------------------------------------
# Normally, sorting can be done with built-in functions or 
# algorithms like merge sort, quick sort, etc. But here, the
# challenge is to do sorting ONLY with stack operations and
# recursion.
#
# Intuition:
# - Recursively remove elements from the stack until it is empty.
# - While returning from recursion, insert each element back into
#   the stack in its correct sorted position.
#
# Example:
# Input:  [3, 1, 4, 2]
# Output: [1, 2, 3, 4]
#
# Stack flow:
# Step 1: Remove 2 -> remove 4 -> remove 1 -> remove 3 (stack empty)
# Step 2: Insert 3 -> stack = [3]
# Step 3: Insert 1 -> stack = [1, 3]
# Step 4: Insert 4 -> stack = [1, 3, 4]
# Step 5: Insert 2 -> stack = [1, 2, 3, 4]
# ------------------------------------------------------------


# ------------------------------------------------------------
# FUNCTION: Sort Stack Recursively
# ------------------------------------------------------------
def sortStack(stack): 
    # Base condition: If stack is empty, return
    if len(stack) == 0: 
        return stack 
    
    # Pop the top element
    top = stack.pop()
    
    # Recursively sort the remaining stack
    sortStack(stack)
    
    # Insert the popped element in its correct sorted position
    insertInSortedOrder(stack, top)
    
    # Return the sorted stack
    return stack 


# ------------------------------------------------------------
# FUNCTION: Insert in Sorted Order
# ------------------------------------------------------------
def insertInSortedOrder(stack, value): 
    # If stack is empty OR top of stack <= value, push value
    if len(stack) == 0 or stack[-1] <= value: 
        stack.append(value)
        return 
    
    # Otherwise, remove the top element
    top = stack.pop()
    
    # Recursively call to find correct position
    insertInSortedOrder(stack, value)
    
    # Put the removed element back
    stack.append(top)


# ------------------------------------------------------------
# EXECUTION THEORY (STEP BY STEP):
# ------------------------------------------------------------
# Suppose we call: sortStack([3, 1, 4, 2])
#
# 1. sortStack([3, 1, 4, 2])
#    - Pops 2, calls sortStack([3, 1, 4])
#
# 2. sortStack([3, 1, 4])
#    - Pops 4, calls sortStack([3, 1])
#
# 3. sortStack([3, 1])
#    - Pops 1, calls sortStack([3])
#
# 4. sortStack([3])
#    - Pops 3, calls sortStack([])
#
# 5. sortStack([]) returns []
#
# Backtracking begins:
# - Insert 3 → [3]
# - Insert 1 → [1, 3]
# - Insert 4 → [1, 3, 4]
# - Insert 2 → [1, 2, 3, 4]
#
# Final stack = [1, 2, 3, 4]
# ------------------------------------------------------------


# ------------------------------------------------------------
# DUMMY DATA (Testing)
# ------------------------------------------------------------
stack = [3, 1, 4, 2]
print("Original Stack:", stack)
sorted_stack = sortStack(stack)
print("Sorted Stack:", sorted_stack)


# ------------------------------------------------------------
# INDUSTRY EQUIVALENT SCENARIO:
# ------------------------------------------------------------
# This type of problem appears in situations where:
#
# 1. Limited Resources / Constraints:
#    - You cannot use advanced data structures or external memory,
#      and must rely only on recursion + stack operations.
#
# 2. Real-time Processing:
#    - Suppose you are processing incoming requests or tasks that
#      must be sorted by priority before execution. The tasks are
#      held in a stack-like buffer, and you must reorder them
#      without moving them to another storage.
#
# 3. Embedded Systems / Memory-Constrained Devices:
#    - In small devices (like routers, IoT devices), you may only
#      have stack-based storage and need recursive logic for sorting
#      because external sorting libraries cannot be used.
#
# 4. Compiler Design:
#    - Compilers use stacks internally for parsing and ordering
#      operators by precedence. Recursive stack sorting concepts
#      align with such compiler operations.
#
# In short, this problem demonstrates how recursion and stack 
# manipulation can replace traditional sorting algorithms in 
# constrained environments.
# ------------------------------------------------------------
