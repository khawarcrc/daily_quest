# Problem Statement:
# Given an array of integers and a target sum, find all unique triplets in the array that add up to the target sum.
# The function should return a list of all such triplets (sets of three numbers) that sum up to the given target.
# The triplets should be returned in ascending order, and no duplicate triplets should be included in the output.

# Steps to Solve the Problem:

# 1. **Sort the Array**:
#    - First, sort the input array in ascending order. Sorting simplifies the process of finding triplets by allowing us to use a two-pointer approach.

# 2. **Initialize Triplets List**:
#    - Create an empty list to store the valid triplets that sum up to the target.

# 3. **Iterate Over the Array**:
#    - Use a for loop to iterate through the array from the first element to the third-to-last element. 
#    - For each element in the loop, consider it as the first element of the potential triplet.

# 4. **Set Up Two Pointers**:
#    - For each element at index `i`, set up two pointers: 
#      - `left` starting at the element immediately after `i` (i.e., `i + 1`).
#      - `right` starting at the last element of the array.

# 5. **Find Triplets Using Two-Pointer Approach**:
#    - Calculate the sum of the three elements (`i`, `left`, and `right`).
#    - There are three possible outcomes for the sum:
#      - If the sum is equal to the target, the triplet is valid and should be added to the result list.
#      - If the sum is less than the target, increment the `left` pointer to increase the sum.
#      - If the sum is greater than the target, decrement the `right` pointer to decrease the sum.

# 6. **Continue Adjusting Pointers**:
#    - Repeat the process of adjusting the `left` and `right` pointers while the `left` pointer is less than the `right` pointer.
#    - For each valid triplet found, both pointers should move inward to explore other potential triplets.

# 7. **Avoid Duplicates**:
#    - Since the array is sorted, avoid adding duplicate triplets by ensuring that the same combination is not added more than once.

# 8. **Return the Result**:
#    - After iterating through the array and checking all possible triplets, return the list of valid triplets that sum to the target.



def threeNumberSum(array, targetSum):
    #  Sort the input array for proper pointer movement
    array.sort()

    #  Initialize an empty list to store the triplets
    triplets = []

    #  Loop through the array, leaving out the last two elements for the pointers
    for i in range(len(array) - 2):
        # Initialize the left pointer to the element next to i
        left = i + 1
        # Initialize the right pointer to the last element of the array
        right = len(array) - 1

        #  Use a while loop to move the left and right pointers
        while left < right:
            # Calculate the sum of the three elements
            currentSum = array[i] + array[left] + array[right]

            #  Check if the current sum is equal to the target sum
            if currentSum == targetSum:
                # If a valid triplet is found, add it to the triplets list
                triplets.append([array[i], array[left], array[right]])
                # Move both pointers inward to check for other potential triplets
                left += 1
                right -= 1
            #  If the current sum is less than the target, increment the left pointer
            elif currentSum < targetSum:
                left += 1
            #  If the current sum is greater than the target, decrement the right pointer
            elif currentSum > targetSum:
                right -= 1

    #  Return the list of triplets that sum to the target value
    return triplets


# Test the function with a sample array and target sum
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
result = threeNumberSum(array, targetSum)

# Print the result
print(result)  # Expected output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
