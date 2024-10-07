# Problem Statement:
# Given an array of integers, return a new array where each element at index `i` is the product
# of all the numbers in the original array except the one at index `i`.
# The solution should not use division to calculate the result.

# Steps to Solve the Problem:
# 1. Create an empty array called `products` of the same length as the input array, initialized with 1.
# 2. Loop through each element in the input array (using index `i`).
#    - For each element at index `i`, initialize a variable `runningProduct` to 1.
#    - Then, loop through the input array again (using index `j`).
#       - If `i` is not equal to `j` (i.e., skip the current element), multiply `runningProduct` by `array[j]`.
#    - After completing the inner loop, assign the value of `runningProduct` to `products[i]`.
# 3. Return the `products` array as the final result.


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
