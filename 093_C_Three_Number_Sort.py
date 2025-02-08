# -------------------------------------------------------------
# PROBLEM STATEMENT:
# -------------------------------------------------------------
# You are given:
#   - An array that contains only three distinct values.
#   - An "order" array that specifies the desired order 
#     in which these three values should appear.
#
# Task:
#   Write a function that sorts the input array so that 
#   its elements appear in the same relative order as defined 
#   in the "order" array.
#
# Example:
#   Input array = [1, 0, 0, -1, -1, 0, 1, 1]
#   Order       = [0, 1, -1]
#   Output      = [0, 0, 0, 1, 1, 1, -1, -1]
#
# -------------------------------------------------------------
# EXPLANATION OF THE PROBLEM:
# -------------------------------------------------------------
# - Normal sorting algorithms (like sort()) cannot be used directly
#   because the goal is not to sort numerically, but rather to 
#   rearrange according to the custom "order".
# - The order array acts like a "sorting rule".
#   For example:
#       If order = [X, Y, Z]
#       → First place all X's
#       → Then place all Y's
#       → Finally place all Z's
#
# -------------------------------------------------------------
# THEORY OF CODE EXECUTION:
# -------------------------------------------------------------
# 1. Count how many times each element of "order" appears 
#    inside the given array.
# 2. Reconstruct the array by placing the counted elements 
#    in the sequence defined by "order".
# 3. Each segment of the array is filled with one of the 
#    values in correct order.
# -------------------------------------------------------------

def threeNumberSort(array, order): 
    # Step 1: Create a count array of length 3 (since only 3 unique values exist).
    valueCounts = [0, 0, 0]  
    
    # Step 2: Count occurrences of each element from array according to order.
    for element in array:  
        orderIndex = order.index(element)   # Find index of element in "order"
        valueCounts[orderIndex] += 1        # Increment count for that element
    
    # 🔎 Print #1 → Show counts of each element
    print("Counts of elements according to order:", dict(zip(order, valueCounts)))
    
    # Step 3: Reconstruct the array using counts and order
    for i in range(3): 
        value = order[i]             # Current value to place
        count = valueCounts[i]       # How many times this value should appear
        
        numElementsBefore = sum(valueCounts[:i])   # Where to start placing this value
        for n in range(count): 
            currentIndex = numElementsBefore + n   # Correct position
            array[currentIndex] = value            # Place the element
            
        # 🔎 Print #2 → Show array after placing each value group
        print(f"After placing all {value}'s →", array)    
    
    return array 

# -------------------------------------------------------------
# DUMMY DATA TEST:
# -------------------------------------------------------------
sample_array = [1, 0, 0, -1, -1, 0, 1, 1]   # Unsorted with respect to "order"
order_rule   = [0, 1, -1]                   # Desired order

result = threeNumberSort(sample_array, order_rule)
print("Sorted Array:", result)  
# Expected Output → [0, 0, 0, 1, 1, 1, -1, -1]






# -------------------------------------------------------------
# REAL-TIME APPLICATION SCENARIO (E-COMMERCE):
# -------------------------------------------------------------
# Imagine you’re building an e-commerce app (like Amazon).
#
# Problem Scenario:
#   When a customer applies a filter on products — e.g., sort products 
#   by availability in this order:
#       1. In Stock
#       2. Low Stock (Only few left!)
#       3. Out of Stock
#
#      Products aren’t sorted alphabetically or by price here,
#      but instead by a custom priority order defined by the business.
#
# Mapping to Code:
#   - "array" → list of products with different stock statuses
#   - "order" → [In Stock, Low Stock, Out of Stock]
#   - Output → products rearranged in exactly that order


# -------------------------------------------------------------
# 3. E-Commerce Returns System
# -------------------------------------------------------------
# Problem Statement:
#   When processing customer return requests:
#       - “Defective Product” → highest priority
#       - “Wrong Size/Color” → medium priority
#       - “Changed Mind” → lowest priority
#
#   Sorting return cases in this custom order ensures
#   customer satisfaction and efficient operations.
#
# -------------------------------------------------------------
# 4. Healthcare System (Patient Triage)
# -------------------------------------------------------------
# Problem Statement:
#   In a hospital’s emergency room:
#       - Critical Patients (life-threatening)
#       - Serious but Stable
#       - Minor Injuries
#
#   The system must always sort and show patients 
#   in this order, no matter how they arrive.
#

