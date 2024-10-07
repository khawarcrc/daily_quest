def arrayOfProducts(array):
    # Initialize the products array, where each element will eventually hold
    # the product of all elements except the one at the current index.
    products = [1 for _ in range(len(array))]

    # Initialize two auxiliary arrays:
    # - leftProducts stores the product of all elements to the left of index 'i'
    # - rightProducts stores the product of all elements to the right of index 'i'
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    # This variable will track the running product of elements to the left of 'i'
    leftRunningProduct = 1

    # Fill leftProducts array with the cumulative product of elements to the left of each index
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct  # Assign the current left running product
        leftRunningProduct *= array[
            i
        ]  # Update left running product by multiplying with current element

    # This variable will track the running product of elements to the right of 'i'
    rightRunningProduct = 1

    # Fill rightProducts array with the cumulative product of elements to the right of each index
    for i in reversed(range(len(array))):
        rightProducts[i] = (
            rightRunningProduct  # Assign the current right running product
        )
        rightRunningProduct *= array[
            i
        ]  # Update right running product by multiplying with current element

    # Multiply corresponding values from leftProducts and rightProducts
    # to get the final product for each index
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    # Return the final array where each index has the product of all other elements
    return products


# Dummy data
array = [1, 2, 3, 4]

# Call the function and print the final result
result = arrayOfProducts(array)
print(f"\nFinal result: {result}")
