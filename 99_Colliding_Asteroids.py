# ------------------------------------------------------------
# Problem Statement
# ------------------------------------------------------------
# You are given an array of integers called "asteroids".
# Each integer represents an asteroid in space:
#   - A positive value means the asteroid is moving to the right.
#   - A negative value means the asteroid is moving to the left.
#
# When two asteroids moving in opposite directions collide:
#   - The smaller asteroid (by absolute value) will explode (removed).
#   - If both are the same size, both will explode.
#   - If they are moving in the same direction, they will never collide.
#
# The task is to simulate all asteroid collisions and return the
# state of the asteroids after all collisions have occurred.
#
# Example:
#   Input:  [5, 10, -5]
#   Output: [5, 10]
#   Explanation:
#     - Asteroid 10 and -5 collide
#     - |10| > | -5 | → so -5 is destroyed
#     - Remaining asteroids are [5, 10]
# ------------------------------------------------------------


def collidingAsteriods(asteroids): 
    # We use a stack to simulate collisions
    resultStack = []

    # Iterate over each asteroid one by one
    for asteroid in asteroids:  

        # Case 1: If asteroid is moving right (positive),
        # it cannot collide yet, so push it to the stack
        if asteroid > 0: 
            resultStack.append(asteroid)
            continue  

        # Case 2: If asteroid is moving left (negative),
        # we must check for collisions with stack top
        while True:  

            # If stack is empty OR top of stack is also negative,
            # there is no collision → push asteroid into stack
            if len(resultStack) == 0 or resultStack[-1] < 0: 
                resultStack.append(asteroid)
                break 

            # Convert asteroid to absolute value for comparison
            # because directions are opposite, but collision 
            # depends on size (magnitude).
            absValue = abs(asteroid)

            # Case 2a: If top of stack asteroid is bigger,
            # the current asteroid explodes (do not push).
            if resultStack[-1] > absValue: 
                break 

            # Case 2b: If both are equal in size,
            # both explode → remove stack top and stop loop.
            if resultStack[-1] == absValue: 
                resultStack.pop()
                break 

            # Case 2c: If current asteroid is bigger,
            # destroy the stack top and continue checking 
            # against the next stack element.
            resultStack.pop()
            # Loop continues until either asteroid is destroyed
            # or no collision is possible.

    # Final result: stack will contain surviving asteroids
    return resultStack


# ------------------------------------------------------------
# Dummy Data Testing
# ------------------------------------------------------------

# Example 1
#  5 → moves right
# 10 → moves right
# -5 → moves left
# 10 vs -5 → 10 survives
# Output → [5, 10]
print(collidingAsteriods([5, 10, -5]))  

# Example 2
#  8 → right
# -8 → left
# both are same size, both explode
# Output → []
print(collidingAsteriods([8, -8]))  

# Example 3
# 10 → right
# 2 → right
# -5 → left → collides with 2 first, destroys 2
# then collides with 10, but 10 survives
# Output → [10]
print(collidingAsteriods([10, 2, -5]))  


# ------------------------------------------------------------
# Industry Equivalent Scenario
# ------------------------------------------------------------
# This asteroid collision problem is similar to **resource conflict resolution**
# in real-world applications.
#
# Examples:
# 1. **Network Traffic / Data Packets**
#    - Positive numbers = packets moving forward
#    - Negative numbers = packets facing congestion/block
#    - Larger packets (priority) override smaller packets
#    - If same priority, both get dropped
#
# 2. **Stock Market Orders**
#    - Positive = Buy orders (demand)
#    - Negative = Sell orders (supply)
#    - When they meet (same stock, same price), smaller order is canceled
#    - If same size, both cancel out
#
# 3. **CPU Scheduling**
#    - Positive = ongoing process
#    - Negative = interrupt process
#    - If interrupt is stronger (priority), it kills the process
#    - Otherwise, process continues
#
# In short: This logic is widely used in **conflict resolution simulations**
# where opposing forces must be evaluated and the stronger one survives.
