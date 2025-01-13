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
8. Overlapping Intervals Pattern
9. Modified Binary Search Pattern
10. Binary Tree Traversal Pattern
11. Depth First Search (DFS)
12. Breadth First Search (BFS)
13. Matrix Traversal Pattern
14. Backtracking Pattern
15. Dynamic Programming Pattern


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






"""
----------------------------------------------------------------------
8. OVERLAPPING INTERVALS PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Used for merging or handling overlapping intervals.
Sort by start time, then merge overlapping ones.
Time complexity O(n log n).

B) SIMPLE EXPLANATION:
Imagine merging overlapping meetings in a calendar into single blocks.

C) CODE:
"""


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


# Example:
print("Merged Intervals Example:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))


"""
----------------------------------------------------------------------
9. MODIFIED BINARY SEARCH PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Binary search extended to handle rotated arrays, duplicates, or special conditions.
Time complexity O(log n) for typical cases.

B) SIMPLE EXPLANATION:
Think of searching a word in a rotated dictionary — 
you need to decide which side is sorted before narrowing the search.

C) CODE:
"""


def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# Example:
print("Modified Binary Search Example:", search_rotated([4, 5, 6, 7, 0, 1, 2], 0))


"""
----------------------------------------------------------------------
10. BINARY TREE TRAVERSAL PATTERN
----------------------------------------------------------------------

A) TECHNICAL EXPLANATION:
Traversal orders define how we visit tree nodes: 
Preorder (root-left-right), Inorder (left-root-right), Postorder (left-right-root), Level Order (BFS).
Used in search, copy, and structure-based problems.

B) SIMPLE EXPLANATION:
It’s like exploring rooms in a building in a specific order — 
depth-first or level-by-level.

C) CODE:
"""


# Binary tree traversal example: recursive inorder, preorder, postorder and level-order
from collections import deque                                # import deque for BFS

class TreeNode:                                            # binary tree node definition
    def __init__(self, val=0, left=None, right=None):      # initializer with val and children
        self.val = val                                      # node value
        self.left = left                                    # left child
        self.right = right                                  # right child

def inorder(root, res):                                    # inorder traversal: left, root, right
    if not root:                                           # base case: empty node
        return                                              # nothing to do
    inorder(root.left, res)                                # traverse left subtree
    res.append(root.val)                                    # visit root
    inorder(root.right, res)                               # traverse right subtree

def preorder(root, res):                                   # preorder: root, left, right
    if not root:                                           # base case
        return                                              # nothing to do
    res.append(root.val)                                    # visit root
    preorder(root.left, res)                               # traverse left
    preorder(root.right, res)                              # traverse right

def postorder(root, res):                                  # postorder: left, right, root
    if not root:                                           # base case
        return
    postorder(root.left, res)                              # traverse left
    postorder(root.right, res)                             # traverse right
    res.append(root.val)                                    # visit root after children

def level_order(root):                                     # level-order traversal (BFS)
    if not root:                                           # empty tree edge-case
        return []
    q = deque([root])                                      # queue initialized with root
    out = []                                               # list of values by level (flattened)
    while q:                                               # while there are nodes to process
        node = q.popleft()                                 # dequeue node from left
        out.append(node.val)                               # visit node
        if node.left:                                      # enqueue left child if exists
            q.append(node.left)
        if node.right:                                     # enqueue right child if exists
            q.append(node.right)
    return out                                             # return visited order

# small demo tree
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
ri, rp, rpost = [], [], []
inorder(root, ri); preorder(root, rp); postorder(root, rpost)
print("in", ri, "pre", rp, "post", rpost, "level", level_order(root))



"""
----------------------------------------------------------------------
11. DEPTH FIRST SEARCH (DFS)
----------------------------------------------------------------------

🧩 Definition

Depth-First Search (DFS) is a foundational graph traversal algorithm that explores as far down a branch as possible before backtracking, ensuring a deep, thorough exploration of the graph’s structure. Unlike Breadth-First Search (BFS), which expands outward level by level, DFS dives vertically into a path until no unvisited nodes remain, then retreats to the most recent branching point to continue exploring. This “deep-first” behavior makes DFS highly suitable for problems such as pathfinding, connected component detection, topological sorting, and cycle detection in directed graphs. It forms the backbone of many complex algorithms, such as detecting strongly connected components (Tarjan’s or Kosaraju’s algorithms), generating mazes, and solving puzzles that require exploring multiple decision paths. DFS can be implemented recursively, which mirrors its conceptual depth exploration, or iteratively using an explicit stack, which simulates the recursive call behavior. The algorithm’s essence lies in systematic depth exploration followed by controlled backtracking — a disciplined way of navigating the unknown. With a time complexity of O(V + E) (where V = vertices and E = edges) and space complexity of O(V) for maintaining the visited structure and recursion stack, DFS is both elegant and efficient. It’s especially powerful for uncovering graph structures that require order, hierarchy, or detection of cycles and dependencies.

⚙️ Technical Explanation

From a technical perspective, Depth-First Search (DFS) operates by recursively visiting nodes or using a stack to simulate recursion explicitly. The algorithm begins by marking a starting node as visited and then exploring one of its unvisited neighbors. Each time a new neighbor is visited, the current path is extended deeper until no further unvisited neighbors exist — at which point, the algorithm backtracks to the most recent node with remaining unvisited neighbors. This depth-first progression continues until all nodes reachable from the source have been visited. To prevent infinite loops, especially in graphs with cycles, a visited set or array is maintained to record nodes that have already been explored. When implemented recursively, the call stack inherently keeps track of the traversal path; when implemented iteratively, a stack data structure explicitly handles this process. DFS’s efficiency lies in its O(V + E) complexity, as each node and edge is processed once. Memory usage is typically O(V) due to the visited set and recursion depth. DFS is particularly important in topological sorting, where nodes are pushed to a result stack after all their descendants have been explored (post-order traversal). It’s also central to cycle detection — in directed graphs, if the algorithm encounters a node that is already in the recursion stack, a cycle exists. Furthermore, discovery and finish times recorded during DFS are crucial for advanced analyses, such as identifying articulation points and bridges in networks. However, in very deep graphs, recursive DFS can exceed the call stack limit, requiring either an iterative conversion or increasing the recursion depth limit to maintain reliability.

💡 Simple Explanation

Think of Depth-First Search (DFS) like exploring a cave system. You enter one tunnel and keep walking as far as possible until you hit a dead end — then you backtrack to the last junction and try another tunnel. You repeat this process until every tunnel has been explored. That’s exactly how DFS behaves. It starts at one point, dives deep along one path, and only when it can’t go further does it step back and explore other directions. In programming, this “going deep before stepping back” pattern is implemented using recursion (a function calling itself) or a stack (a structure that remembers where you came from). To avoid getting lost or looping forever, DFS keeps a visited list, marking each place once it’s seen. This ensures that cycles — like roads leading back to the same point — don’t trap the algorithm. In a maze, DFS would follow one corridor until the end, then backtrack to try another route. In social networks, it might explore all friends of one person deeply before checking others. While DFS doesn’t guarantee the shortest path like BFS, it’s amazing for exploring all possible routes, solving puzzles, finding connected groups, and understanding dependencies in data. You can think of it as the algorithm that prefers depth over breadth — curious, focused, and determined to explore every possibility before moving on.
"""

# DFS example: check if path exists between two nodes in adjacency list graph
def dfs_has_path(graph, start, target):                    # graph is adjacency dict: node -> list(neighbors)
    visited = set()                                        # set to track visited nodes
    stack = [start]                                        # stack for iterative DFS starting with start
    while stack:                                           # while there are nodes to explore
        node = stack.pop()                                 # pop a node from stack (LIFO)
        if node == target:                                 # if target reached
            return True                                     # path exists
        if node in visited:                                # if already visited, skip
            continue
        visited.add(node)                                  # mark node visited
        for nei in graph.get(node, []):                     # push unvisited neighbors onto stack
            if nei not in visited:
                stack.append(nei)
    return False                                           # exhausted nodes -> no path

graph_example = {1:[2,3], 2:[4], 3:[], 4:[]}                # sample adjacency list
print(dfs_has_path(graph_example, 1, 4))                    # True



"""
----------------------------------------------------------------------
12. BREADTH FIRST SEARCH (BFS)
----------------------------------------------------------------------

🧩 Definition

Breadth-First Search (BFS) is a fundamental graph traversal algorithm that explores nodes in a graph level by level, moving outward from a chosen starting point (source). It systematically visits all vertices at a given distance (in terms of edges) from the source before moving to vertices further away. This property makes BFS particularly effective for finding the shortest path in unweighted graphs — the first time a node is reached, it’s guaranteed to be via the shortest possible path. BFS is widely used in applications such as shortest path discovery, level-order traversal of trees, network broadcasting, and minimum step problems in implicit graphs like grids or puzzles. Conceptually, BFS works like a ripple spreading from a drop in water — expanding equally in all directions, layer by layer. It’s implemented using a queue, which enforces this first-in, first-out (FIFO) behavior, ensuring nodes discovered earlier are processed before newer ones. The algorithm maintains a visited structure to prevent cycles and redundant processing, making it both systematic and efficient. With a time complexity of O(V + E) (where V is vertices and E is edges), BFS ensures every node and edge is explored once, providing a predictable and complete traversal suitable for a variety of search and mapping problems.


⚙️ Technical Explanation

At its core, BFS operates on the principle of exploring the graph in concentric layers around the source node. Implementation begins by initializing a queue that holds nodes to be processed and a visited set or boolean array to track which nodes have already been discovered. The source node is enqueued and marked as visited. Then, in each iteration, a node is dequeued from the front of the queue, and all its unvisited neighbors are enqueued, marked visited, and optionally assigned a parent pointer to reconstruct paths later. This ensures nodes are visited in increasing order of their distance from the source — the first layer containing nodes at distance 1, the next layer at distance 2, and so on. For shortest path reconstruction, each node stores a reference to the node it was reached from; tracing back from the target node to the source yields the shortest path. BFS’s time complexity, O(V + E), comes from the fact that every vertex and edge is processed once. The space complexity is O(V) because in the worst case, the queue and visited set can hold all vertices simultaneously. In implicit graphs, such as grids or puzzles where edges are not stored but generated dynamically, BFS still applies — neighbor states are computed on the fly (e.g., up, down, left, right moves in a maze). Edge cases include disconnected graphs, where BFS covers only the component containing the source; and large branching factors, where memory can grow rapidly. To optimize in such cases, bidirectional BFS is often used — simultaneously searching from both the source and target and meeting in the middle, effectively halving the search depth and drastically reducing the number of nodes explored.

💡 Simple Explanation

Imagine standing in the middle of a park, shouting your friend’s name. The sound spreads evenly outward in all directions — the people nearest to you hear it first, then those slightly farther, and so on. That’s how Breadth-First Search works. It starts from one point and explores everything nearby before moving further away. In a social network, for example, BFS helps find the shortest chain of connections between two people — first checking your direct friends, then friends of friends, and so on until it finds the target person. The key idea is that BFS always moves level by level, ensuring that the first time you reach a node, it’s through the shortest possible route. In programming terms, BFS uses a queue — like a line at a ticket counter — where the first person in line gets served first. You start by adding the starting point to the queue, explore all its neighbors, and add them to the queue. Then you move to those neighbors and repeat the process. To avoid looping endlessly, you keep a visited list, marking each place once it’s explored. In a maze, BFS would explore all paths one step at a time — if it finds the exit, you know it’s the minimum number of steps. This simple yet powerful logic makes BFS one of the most essential tools in computer science — a perfect example of how exploring systematically can reveal the shortest route to any destination.
"""


# BFS example: shortest path length in unweighted graph (returns number of edges in shortest path)
from collections import deque


def bfs_shortest_path(graph, start, target):  # returns distance or -1 if unreachable
    if start == target:  # immediate check
        return 0  # zero edges needed
    visited = set([start])  # visited set initialized with start
    q = deque([(start, 0)])  # queue stores tuples: (node, distance)
    while q:  # loop while queue not empty
        node, dist = q.popleft()  # dequeue node and its distance
        for nei in graph.get(node, []):  # iterate neighbors
            if nei == target:  # if neighbor is target
                return dist + 1  # return distance+1
            if nei not in visited:  # if neighbor unvisited
                visited.add(nei)  # mark visited
                q.append((nei, dist + 1))  # enqueue neighbor with updated dist
    return -1  # target unreachable


graph_example = {1: [2, 3], 2: [4], 3: [4], 4: []}  # sample graph
print(bfs_shortest_path(graph_example, 1, 4))  # prints 2


"""
----------------------------------------------------------------------
13. MATRIX TRAVERSAL PATTERN
----------------------------------------------------------------------

🧩 Definition

Matrix traversal, also known as grid traversal, is a computational approach that treats a two-dimensional matrix as an implicit graph, where each cell acts as a node and edges connect neighboring cells based on adjacency rules. This interpretation allows us to apply graph traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS) to solve a wide variety of grid-based problems. Typical examples include counting islands (connected regions of 1’s), finding shortest paths in a labyrinth, performing flood fill in image or color regions, and exploring connected components in a map. The key insight is that the grid does not need an explicit adjacency list — the adjacency relationships are determined by the possible movement directions (usually 4-directional: up, down, left, right; or 8-directional if diagonals are allowed). Each cell can be thought of as a graph vertex connected to its valid neighbors within the grid bounds. Traversing a matrix systematically requires visiting every cell exactly once while avoiding revisits, making it crucial to maintain a visited tracking mechanism, either by marking cells in-place or maintaining a separate boolean grid. This concept turns ordinary matrix operations into elegant graph problems that can be reasoned about and optimized using classical graph theory techniques.

⚙️ Technical Explanation

Technically, matrix traversal is an implicit graph traversal technique, meaning that instead of explicitly constructing a graph data structure, we infer the neighbors of each cell from its coordinates and movement directions. Each cell (r, c) has up to four or eight valid neighbors defined by direction vectors, such as (r+1, c), (r-1, c), (r, c+1), and (r, c-1) for 4-directional movement. The traversal typically begins by iterating over every cell in the grid. When an unvisited cell that meets the problem’s condition (e.g., a land cell in an island problem) is encountered, a DFS or BFS is initiated from that cell to explore its entire connected region. During traversal, bounds checking ensures we don’t access invalid indices, and visited marking prevents revisiting the same cell. DFS explores deeply through recursion or an explicit stack, marking cells as visited until no unvisited neighbors remain, whereas BFS explores layer by layer using a queue — making it ideal for shortest-path problems since it naturally visits cells in order of increasing distance. In more complex cases, the traversal might include constraints like obstacles, weights, or direction limitations, in which case algorithms like Dijkstra’s or A* may be layered on top of the grid model. Practical implementations also require optimization: minimizing redundant checks, using in-place modifications to save memory, and converting between (row, column) and one-dimensional indices when necessary. On large grids, recursion depth can cause stack overflow in DFS, so an iterative version or BFS is often safer. Overall, the matrix-as-graph abstraction provides a uniform and powerful framework to reason about two-dimensional spatial problems as graph traversal tasks.

💡 Simple Explanation

Imagine a grid or a chessboard — each square represents a place you can stand, and from each square, you can move up, down, left, or right. If you think of each square as a point (node) and each possible move as a connection (edge), you’ve just turned your grid into a graph! This idea helps solve many real-world problems. For instance, suppose you’re counting islands on a map, where 1’s represent land and 0’s represent water. You scan the grid cell by cell, and when you find an unvisited piece of land, you explore all the land connected to it (using DFS or BFS) and mark it as part of the same island. Once that’s done, you continue scanning for the next unvisited piece of land — each time you find one, you’ve discovered a new island. Similarly, if you’re finding the shortest path in a maze, you can start from the entry cell and explore neighboring cells layer by layer using BFS until you reach the exit. The key is to visit each cell once and to keep track of where you’ve already been, just like coloring visited squares so you don’t step on them twice. DFS goes as deep as possible before backtracking, like following a single path until it ends, while BFS spreads out evenly, finding the shortest path naturally. So, matrix traversal is really about walking through a grid intelligently, following connections, avoiding repetition, and keeping track of what’s been seen — much like exploring every street in a city map systematically without ever getting lost.

"""


# Matrix traversal example: number of islands using DFS (4-directional adjacency)
def num_islands(grid):  # grid is list of list of '1'/'0' strings
    if not grid:  # empty grid guard
        return 0
    rows, cols = len(grid), len(grid[0])  # dimensions of grid
    visited = [
        [False] * cols for _ in range(rows)
    ]  # visited matrix initialized with False

    def dfs(r, c):  # inner DFS to mark connected land
        if r < 0 or r >= rows or c < 0 or c >= cols:  # out-of-bounds guard
            return
        if grid[r][c] != "1" or visited[r][c]:  # if water or already visited, stop
            return
        visited[r][c] = True  # mark cell as visited
        dfs(r + 1, c)  # explore down
        dfs(r - 1, c)  # explore up
        dfs(r, c + 1)  # explore right
        dfs(r, c - 1)  # explore left

    count = 0
    for r in range(rows):  # iterate all cells
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:  # found unvisited land
                dfs(r, c)  # flood-fill the island
                count += 1  # increment island count
    return count


g = [
    ["1", "1", "0", "0"],
    ["1", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "0", "0", "1"],
]
print(num_islands(g))  # prints 3


"""
----------------------------------------------------------------------
14. BACKTRACKING PATTERN
----------------------------------------------------------------------

🧩 Definition

Backtracking is a systematic search technique used to explore all potential configurations or solutions of a problem by incrementally building candidates and abandoning those that violate constraints. It’s most commonly applied to combinatorial, constraint-satisfaction, and enumeration problems, such as generating permutations, solving Sudoku puzzles, or placing N queens on a chessboard so that none attack each other. The essence of backtracking lies in its recursive exploration of decision trees — at each level, a choice is made, and the algorithm explores deeper with that choice fixed. If at any point the partial solution is found to be invalid or cannot possibly lead to a complete solution, the algorithm “backtracks” — meaning it reverses the last decision and tries another path. This approach ensures that all feasible possibilities are considered while pruning infeasible paths early, making it more efficient than brute-force enumeration. Backtracking does not guarantee polynomial time complexity in the worst case but is often highly effective in practice due to intelligent pruning and early exits. It represents one of the most elegant algorithmic paradigms that bridges search, recursion, and optimization into a single structured framework.

⚙️ Technical Explanation

Technically, backtracking can be seen as a depth-first traversal of a state space tree, where each node represents a partial solution, and each branch represents a possible choice or decision extending that solution. At every recursive call, the algorithm decides whether to include or exclude a certain element or make a specific move. This decision expands the current partial configuration into one or more subproblems. The recursive call then continues exploring until a full solution is found or until the configuration violates a constraint, at which point the algorithm returns (“backtracks”) to the previous step and explores a different branch. Efficient backtracking depends on constraint checking and pruning — rejecting infeasible paths as early as possible to minimize unnecessary computation. For example, in the N-Queens problem, the algorithm immediately stops exploring any partial configuration where two queens attack each other. Implementation typically involves maintaining a mutable data structure (like a list or matrix) that represents the current partial state, and performing three critical operations: (1) choose — select a candidate option; (2) explore — recursively proceed with that choice; and (3) unchoose — undo the last decision to restore the state for alternative choices. These three steps are often embedded within a recursive function, where the “undo” step ensures the search can continue from previous branches without residual side effects. Additionally, backtracking algorithms may integrate heuristics such as variable ordering, forward checking, or domain reduction to dramatically reduce search space in complex constraint problems like Sudoku or graph coloring. While the theoretical complexity remains exponential, these optimizations make backtracking viable for many real-world cases by cutting down the number of explored states.

💡 Simple Explanation

Think of backtracking as a smart trial-and-error approach that remembers where it went wrong and avoids repeating mistakes. Imagine you’re solving a maze: at each junction, you pick a path and move forward. If you hit a dead end, you walk back to the last junction and try a different path — that’s exactly what backtracking does. In the same way, when solving puzzles like Sudoku or arranging queens on a chessboard, the algorithm tries placing numbers or queens one by one. If a placement breaks the rules (for example, two queens attack each other), it goes back a step, removes the conflicting piece, and tries another position. This process continues until a complete valid arrangement is found. You can also picture it as exploring a tree of decisions — each branch is a possible move, and you climb back up whenever a branch doesn’t work. What makes backtracking powerful is pruning — the ability to recognize and skip unpromising paths early, rather than exploring every possible configuration blindly. It’s like knowing a certain path in the maze leads to a wall, so you don’t bother walking all the way there. In everyday terms, backtracking teaches us a powerful principle: try, test, and correct — systematically exploring possibilities while learning from each mistake and using that knowledge to find a solution efficiently.
"""


# Backtracking example: generate all subsets (power set) of a list
def subsets(nums):  # returns all subsets of nums
    res = []  # final list of subsets
    subset = []  # current working subset

    def backtrack(i):  # backtracking recursion with index i
        if i == len(nums):  # base case: processed all elements
            res.append(subset.copy())  # append a copy of current subset to results
            return
        # choice 1: exclude nums[i]
        backtrack(i + 1)  # recurse without including current element
        # choice 2: include nums[i]
        subset.append(nums[i])  # choose element nums[i]
        backtrack(i + 1)  # recurse after choosing it
        subset.pop()  # backtrack: remove last element to restore state

    backtrack(0)  # start backtracking from index 0
    return res  # return list of all subsets


print(subsets([1, 2, 3]))  # prints all 8 subsets


"""
----------------------------------------------------------------------
15. DYNAMIC PROGRAMMING (DP)
----------------------------------------------------------------------

🧩 Definition

Dynamic Programming (DP) is a powerful problem-solving technique used in computer science to solve problems 
that can be broken down into smaller, overlapping subproblems. It is particularly useful for optimization and
counting problems, where multiple smaller decisions lead to an overall best solution.
The central idea behind DP is to solve each subproblem only once and store its result, so that when the same subproblem appears again,
we can retrieve the previously computed value instead of recalculating it. This reuse of solutions transforms problems 
that might take exponential time using naive recursion into efficient algorithms with polynomial time complexity.
DP fundamentally relies on two key properties: optimal substructure, meaning that the optimal solution to the overall
problem can be derived from the optimal solutions of its subproblems; and overlapping subproblems, meaning that 
the same smaller problems are solved multiple times in a naive approach. Dynamic programming can be implemented
using two complementary strategies: top-down (memoization), where we start from the main problem and recursively
solve and store results for smaller subproblems as needed; and bottom-up (tabulation), where we iteratively build
solutions for smaller subproblems first and combine them to solve larger ones. Through careful identification of
the problem’s state, recurrence relation, and base cases, DP allows us to design efficient, predictable, and elegant
solutions to complex computational problems.

⚙️ Technical Explanation

From a technical standpoint, dynamic programming is based on mathematical recurrence relations that define the 
relationship between a problem’s substructures. The first step in any DP design is to define the state, which 
uniquely represents a subproblem — for instance, the number of items processed, the remaining capacity of a bag,
or the current index in a sequence. The second step is to formulate the recurrence relation, which expresses how 
the current state’s value can be derived from one or more smaller states. For example, in the Fibonacci sequence,
F(n) = F(n-1) + F(n-2) is the recurrence relation that relates a state to its two smaller states. The next step is 
to define the base cases, which represent the simplest, smallest possible subproblems whose solutions are known directly.
Implementations can follow either a top-down or bottom-up strategy. The top-down approach uses 
recursion with memoization — a dictionary or array stores results of computed subproblems to prevent redundant calls.
The bottom-up approach uses tabulation — iterating systematically through subproblems in an order that guarantees 
dependencies are resolved before use. The complexity of a DP algorithm is determined by the number of
unique states (N) multiplied by the time it takes to compute each state (T), often yielding an overall
complexity of O(N*T). DP solutions must be carefully structured: the state space should be neither too broad
(causing unnecessary computation) nor too narrow (missing dependencies). Optimization techniques such as space
compression, rolling arrays, or iterative state transitions are often applied to reduce memory usage. Ultimately, 
DP is not just about caching — it is about transforming recursive relationships into iterative or memoized computations
through structured state modeling, ensuring both efficiency and mathematical correctness.

# 💡 Simple Explanation
#
# Imagine you’re trying to climb a staircase with a certain number of steps,
# and you can take either one or two steps at a time. If you try to calculate
# how many different ways you can reach the top by exploring all combinations,
# you’ll quickly notice you’re repeating the same calculations again and again —
# the number of ways to climb 5 stairs depends on the number of ways to climb 4
# and 3 stairs, and those in turn depend on smaller ones.
#
# Instead of recalculating, you can simply remember results for smaller steps —
# once you know how many ways there are to reach step 3 and step 4, you can
# directly compute step 5 without recomputation. This is the essence of dynamic
# programming: you remember past results to avoid redoing work.
#
# The same concept applies to countless computer problems — whether it’s finding
# the shortest path in a grid, the longest common subsequence between strings, or
# the maximum value you can carry in a knapsack.
#
# In human terms, DP is like keeping notes while solving a complex puzzle —
# each note saves you from starting over when a familiar piece reappears.
#
# The top-down approach is like solving the puzzle naturally and writing down
# partial results as you go, while the bottom-up approach is like starting from
# the smallest pieces and building up to the full picture.
#
# Dynamic programming teaches us to think systematically: break problems into
# repeatable parts, store results efficiently, and construct bigger answers
# using what we already know.
#
# It’s not just a technique; it’s a mindset — a way of approaching problems that
# rewards planning and memory over brute force.

C) CODE:
"""


# Dynamic programming example: coin change (minimum coins to make amount) - bottom-up DP
def coin_change(coins, amount):  # returns min coins or -1 if impossible
    INF = float("inf")  # infinity sentinel for unreachable states
    dp = [INF] * (amount + 1)  # dp[x] = min coins to make x
    dp[0] = 0  # base case: 0 coins to make amount 0
    for a in range(1, amount + 1):  # iterate all sub-amounts 1..amount
        for c in coins:  # try each coin value
            if c <= a:  # coin usable only if <= current amount
                dp[a] = min(
                    dp[a], dp[a - c] + 1
                )  # recurrence: choose best among options
    return dp[amount] if dp[amount] != INF else -1  # if reachable, return value else -1


print(coin_change([1, 2, 5], 11))  # prints 3 (5+5+1)
