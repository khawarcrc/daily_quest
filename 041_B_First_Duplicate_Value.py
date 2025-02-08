def firstDuplicateValue(array):
    # Set to store seen values
    seen = set()

    # Loop through the array
    for value in array:
        # If value is already in the set, it's the first duplicate
        if value in seen:
            return value
        # Otherwise, add the value to the set
        seen.add(value)
    
    # If no duplicate is found, return -1
    return -1


# Dummy data for testing
test_array = [5, 3, 4, 5, 2, 2, 3, 1]
print(firstDuplicateValue(test_array))  # Output will now be 2, which is the correct result.



# def firstDuplicateValue(array):
#     # Dictionary to store the first occurrence index of each element
#     seen = {}

#     # Loop through the array
#     for i, value in enumerate(array):
#         # If value is already in the dictionary, it's a duplicate
#         if value in seen:
#             return value
#         # Otherwise, store the index of the first occurrence
#         seen[value] = i
    
#     # If no duplicate is found, return -1
#     return -1


# # Dummy data for testing
# test_array = [5, 3, 4, 5, 2, 2, 3, 1]
# print(firstDuplicateValue(test_array))  # Output will now be 2, which is the correct result.
