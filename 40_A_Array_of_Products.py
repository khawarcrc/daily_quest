# Problem Statement:
# Given an array of integers, return a new array where each element at index `i` is the product
# of all the numbers in the original array except the one at index `i`. In other words, 
# for each index in the output array, the value should be the product of all the elements in 
# the input array except the element at that index. 
# The challenge is that you cannot use division to calculate the result.

# The task is to solve the problem without dividing the total product of all the elements by the 
# element at index `i`. Instead, you must multiply all the elements except the one at `i` directly.

# Example:
# Input:  [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Explanation:
# For index 0, the product of all numbers except 1 is 2 * 3 * 4 = 24.
# For index 1, the product of all numbers except 2 is 1 * 3 * 4 = 12.
# For index 2, the product of all numbers except 3 is 1 * 2 * 4 = 8.
# For index 3, the product of all numbers except 4 is 1 * 2 * 3 = 6.

# Steps to Solve the Problem:
# 1. Create a new array called `products` of the same length as the input array, initialized with 1s.
#    This array will store the final result where each element is the product of all other elements 
#    except the one at the corresponding index in the input array.

# 2. Loop through each element of the input array using index `i`. This loop will process each 
#    element and calculate the product for the current index `i`.
#    - For each element at index `i`, initialize a variable `runningProduct` to 1, which will 
#      temporarily store the product of all other elements except the current element.

# 3. Loop through the array again using index `j` to multiply all elements except the one 
#    at index `i`:
#    - If `i` is not equal to `j` (i.e., skip the current element at `i`), multiply `runningProduct` 
#      by `array[j]`, accumulating the product of all other elements.
#    - After completing the inner loop, assign the value of `runningProduct` to `products[i]`. 
#      This ensures that for each index `i`, the correct product is stored.

# 4. Once all the iterations are complete, return the `products` array as the final result.

# This brute-force solution involves two nested loops, which results in a time complexity of O(n^2). 
# There are more optimized approaches using prefix and suffix products to solve this problem in 
# linear time, but this approach is straightforward and easy to understand for small input sizes.

# Solution Implementation:



def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]

        products[i] = runningProduct
    return products


# Dummy data
array = [1, 2, 3, 4]

# Call the function and print the final result
result = arrayOfProducts(array)
print(f"\nFinal result: {result}")


# def arrayOfProducts(array):
#     # Initialize the products array with 1s
#     products = [1 for _ in range(len(array))]
#     print(f"Initial products array: {products}")

#     # Outer loop to go through each element in the array
#     for i in range(len(array)):
#         runningProduct = 1  # Initialize runningProduct for each element
#         print(f"\nProcessing index {i}, value = {array[i]}")

#         # Inner loop to calculate the product of all elements except the one at index i
#         for j in range(len(array)):
#             if i != j:  # Only multiply elements other than the one at index i
#                 print(
#                     f"Multiplying runningProduct {runningProduct} by array[{j}] = {array[j]}"
#                 )
#                 runningProduct *= array[j]

#         # Store the result in products[i]
#         products[i] = runningProduct
#         print(f"After processing index {i}, products = {products}")

#     # Return the final products array
#     return products


# # Dummy data
# array = [1, 2, 3, 4]

# # Call the function and print the final result
# result = arrayOfProducts(array)
# print(f"\nFinal result: {result}")
