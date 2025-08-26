# ------------------------------------------------------------
# PROBLEM STATEMENT:
# ------------------------------------------------------------
# You are given:
# - An array "buildings", where each element represents the height of a building.
# - A string "direction" which can be either "EAST" or "WEST".
#
# Task:
# Find which buildings can see the sunset.  
#
# Rules:
# - A building can see the sunset if it is strictly taller than all the buildings
#   that come after it in the direction it faces.
# - EAST means the buildings face right → we check from left to right.
# - WEST means the buildings face left → we check from right to left.
# - Return the indices of the buildings that can see the sunset in ascending order.
#
# ------------------------------------------------------------
# PROBLEM EXPLANATION / THEORY:
# ------------------------------------------------------------
# 1. Imagine the sun is setting in the given direction.
# 2. If direction = EAST:
#    - The sun sets on the right side.
#    - This means a building can see the sunset if no taller building exists
#      to its right.
#
# 3. If direction = WEST:
#    - The sun sets on the left side.
#    - This means a building can see the sunset if no taller building exists
#      to its left.
#
# HOW TO SOLVE:
# - We traverse the array in the order of the sunset direction.
# - Maintain a list of candidate buildings (possible sunset viewers).
# - For each new building:
#   * Remove all previous candidates shorter or equal to it 
#     (since they are blocked by this taller building).
#   * Add the current building index as a new candidate.
# - In the end, reverse the result for WEST to maintain ascending order.
#
# ------------------------------------------------------------
# CODE IMPLEMENTATION WITH COMMENTS:
# ------------------------------------------------------------

def sunsetViews(buildings, direction): 
    # This will hold indices of buildings that can see the sunset
    candidateBuildings = []
    
    # Starting index depends on direction
    # - If EAST → start at 0 (leftmost) and move right
    # - If WEST → start at last index and move left
    startIdx = 0 if direction == "EAST" else len(buildings) - 1
    
    # Step defines whether we move forward (+1) or backward (-1)
    step = 1 if direction == "EAST" else -1  
    
    # Current index while iterating
    idx = startIdx 
    
    # Traverse until index goes out of range
    while idx >= 0 and idx < len(buildings): 
        buildingHeight = buildings[idx]   # Get height of current building
        
        # Remove all previous candidates that are shorter or equal
        # because they are blocked by this taller building
        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight: 
            candidateBuildings.pop() 
            
        # Add current building index to the list
        candidateBuildings.append(idx)
        
        # Move index according to step (+1 for EAST, -1 for WEST)
        idx += step 
    
    # If direction is WEST → collected indices are reversed,
    # so reverse them again to get ascending order
    if direction == "WEST": 
        return candidateBuildings[::-1]
    
    # For EAST, indices are already in ascending order
    return candidateBuildings       


# ------------------------------------------------------------
# DUMMY TEST CASES:
# ------------------------------------------------------------

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "EAST"))  # [1, 3, 6, 7]
print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "WEST"))  # [0, 1]
print(sunsetViews([10, 8, 6, 4, 2], "EAST"))          # [0, 1, 2, 3, 4]
print(sunsetViews([2, 4, 6, 8, 10], "WEST"))          # [4]
print(sunsetViews([1, 2, 2, 2, 1], "EAST"))           # [1, 2, 3, 4]

# ------------------------------------------------------------
# INDUSTRY REAL-TIME APPLICATION SCENARIOS:
# ------------------------------------------------------------
# 1. ARCHITECTURE & URBAN PLANNING:
#    - Determining which buildings will receive direct sunlight 
#      in the evening (EAST) or morning (WEST).
#    - Useful when planning solar panel installations or designing skylines.
#
# 2. COMPUTER GRAPHICS:
#    - While rendering skylines in games or simulations,
#      we need to compute visible buildings from a camera direction.
#
# 3. DATA VISUALIZATION:
#    - Similar to buildings, bars in a bar chart can be "visible"
#      if they are not blocked by taller bars in the viewing direction.
#
# 4. STOCK MARKET ANALYSIS:
#    - Identifying "dominant" peaks in stock prices where smaller values 
#      are overshadowed by bigger future values.
#
# ------------------------------------------------------------
