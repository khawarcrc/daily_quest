"""
======================================================================
DATA STRUCTURES & ALGORITHMIC PATTERNS – COMPLETE REFERENCE (PYTHON)
======================================================================

Role: Expert Technical Writer & Senior Software Engineer

----------------------------------------------------------------------
EXECUTIVE SUMMARY
----------------------------------------------------------------------

This document consolidates  of the most important algorithmic patterns
commonly used in LeetCode, coding interviews, and large-scale system design.
Each pattern is explained from both a technical and practical perspective.

Structure of Each Section:
A) Technical Explanation — theoretical and algorithmic depth.
B) Simple Explanation — plain-English understanding.
C) Python Implementation — fully runnable with line-by-line comments.

These patterns collectively enable one to recognize and efficiently solve
complex problems in arrays, strings, linked lists, trees, graphs, and dynamic
programming by applying reusable mental models.

----------------------------------------------------------------------
ASSUMPTIONS
----------------------------------------------------------------------

1. All problems are considered with valid inputs unless otherwise stated.
2. Time complexity analysis uses Big-O notation and assumes standard data structures.
3. "LeetCode problems" refer to canonical examples aligned with these patterns.
4. Code focuses on algorithm demonstration — not on edge-case validation or input I/O.
5. Each snippet runs independently (you can execute each separately in a REPL).

----------------------------------------------------------------------
TABLE OF CONTENTS
----------------------------------------------------------------------

1. Prefix Sum Pattern
2. Two Pointers Pattern
3. Sliding Window Pattern
4. Fast and Slow Pointers Pattern
5. Linked List In-place Reversal
6. Monotonic Stack Pattern
7. Top-K Elements Pattern

----------------------------------------------------------------------
1. PREFIX SUM PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Prefix Sum is a technique for quickly computing range-based queries
(e.g., subarray sums). It involves creating an auxiliary array `prefix`
where prefix[i] stores the sum of elements from index 0 to i.
This allows O(1) time range-sum queries using:
    sum(i, j) = prefix[j] - prefix[i-1]
Construction takes O(n) time and O(n) space.
It’s widely used in problems like “Range Sum Query,” “Subarray Sums,”
and “Equilibrium Index.” Edge cases include index 0 (handled by initializing prefix[0]=arr[0]).

B) SIMPLE EXPLANATION:
Imagine you’re adding up expenses each day. If you know the total at every day,
you can quickly find how much you spent between any two days by subtraction,
without recalculating from scratch. That’s prefix sum.

C) CODE:
"""

from collections import deque
import heapq


def prefix_sum(arr, i, j):
    # Initialize prefix array
    prefix = [0] * len(arr)
    # Set first prefix value equal to first element
    prefix[0] = arr[0]
    # Build cumulative sums
    for k in range(1, len(arr)):
        prefix[k] = prefix[k - 1] + arr[k]
    # Handle case when i == 0 separately
    return prefix[j] if i == 0 else prefix[j] - prefix[i - 1]


# Example:
print("Prefix Sum Example:", prefix_sum([2, 3, 5, 1, 6], 1, 3))  # Output: 9


"""
----------------------------------------------------------------------
2. TWO POINTERS PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Two pointers technique involves maintaining two indices that move toward 
each other or in parallel to reduce complexity in searching or sorting problems. 
Common use cases: sorted array problems, palindrome checks, removing duplicates, etc.
Time complexity is typically O(n), compared to O(n²) for brute force.

B) SIMPLE EXPLANATION:
It’s like checking if a string reads the same backward and forward — 
you start from both ends and move toward the middle, comparing as you go.

C) CODE:
"""


def is_palindrome(s):
    # Define two pointers at start and end
    left, right = 0, len(s) - 1
    # Loop until pointers meet
    while left < right:
        # If characters differ, not palindrome
        if s[left] != s[right]:
            return False
        # Move pointers closer
        left += 1
        right -= 1
    return True


# Example:
print("Two Pointers Example:", is_palindrome("level"))  # Output: True


"""
----------------------------------------------------------------------
3. SLIDING WINDOW PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Sliding window is used when finding optimal subarrays (sum, average, max, etc.).
We keep a fixed-size window and slide it across the array, updating results
incrementally instead of recalculating everything each time.
Time complexity O(n), space O(1).

B) SIMPLE EXPLANATION:
Imagine a window moving across a line of houses, 
and you only care about the sum of houses visible in that window.

C) CODE:
"""


def max_sum_subarray(arr, k):
    # Compute initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    # Slide the window
    for i in range(k, len(arr)):
        # Subtract element leaving window, add element entering
        window_sum += arr[i] - arr[i - k]
        # Track max sum
        max_sum = max(max_sum, window_sum)
    return max_sum


# Example:
print("Sliding Window Example:", max_sum_subarray([1, 2, 3, 4, 5], 3))  # Output: 12


"""
----------------------------------------------------------------------
4. FAST AND SLOW POINTERS PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Used to detect cycles or find middle nodes in linked lists or arrays.
Two pointers move at different speeds; if they meet, a cycle exists.
Time complexity O(n), space O(1).

B) SIMPLE EXPLANATION:
Think of two runners on a circular track — 
if one is faster, they’ll eventually meet if the track loops.

C) CODE:
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    # Initialize both pointers
    slow = fast = head
    # Move fast twice as quickly as slow
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # If they meet, a cycle exists
        if slow == fast:
            return True
    return False


"""
----------------------------------------------------------------------
5. LINKED LIST IN-PLACE REVERSAL
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Reverse the direction of pointers in a singly linked list using O(1) space.
Maintain three pointers: prev, curr, next.
Time complexity O(n), space O(1).

B) SIMPLE EXPLANATION:
Imagine flipping a chain of paperclips one by one so the direction reverses.

C) CODE:
"""


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


"""
----------------------------------------------------------------------
6. MONOTONIC STACK PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Used for finding next greater/smaller elements efficiently.
The stack maintains elements in a monotonic order.
Time complexity O(n).

B) SIMPLE EXPLANATION:
Think of stacking boxes in decreasing height order, 
and whenever a taller one appears, you remove smaller ones.

C) CODE:
"""


def next_greater_elements(nums):
    res = [-1] * len(nums)
    stack = []
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        stack.append(i)
    return res


# Example:
print(
    "Monotonic Stack Example:", next_greater_elements([2, 1, 5, 3])
)  # Output: [5, 5, -1, -1]


"""
----------------------------------------------------------------------
7. TOP-K ELEMENTS PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Find the top k largest or smallest elements using a heap.
Min-heap tracks the k largest; max-heap tracks the k smallest.
Time complexity O(n log k).

B) SIMPLE EXPLANATION:
Think of maintaining a scoreboard of top 3 players — 
you only keep the best few at any time.

C) CODE:
"""


def top_k_elements(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heappushpop(heap, n)
    return heap


# Example:
print(
    "Top-K Elements Example:", top_k_elements([3, 1, 5, 12, 2, 11], 3)
)  # Output: [5, 11, 12]

