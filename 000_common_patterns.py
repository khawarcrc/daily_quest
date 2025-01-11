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


