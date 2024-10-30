def levenshteinDistance(str1, str2):
    # Initialize a 2D list where edits[i][j] will hold the minimum edit distance
    # between the first i characters of str2 and the first j characters of str1.
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    
    print("Initial matrix (after setting up first row):")
    for row in edits:
        print(row)

    # Fill the first column with incremental values, representing the cost
    # of deleting characters from str2 to make it an empty string.
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    print("\nMatrix after setting up first column:")
    for row in edits:
        print(row)

    # Iterate over each cell in the matrix starting from the first row.
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # If characters match, take the diagonal value (no extra cost).
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
                print(f"\nCharacters match ({str2[i-1]}) at str2[{i-1}] and str1[{j-1}].")
                print(f"Copying diagonal value at edits[{i-1}][{j-1}] = {edits[i-1][j-1]}.")
            # If characters differ, take the minimum cost of three operations:
            # substitution, deletion, or insertion.
            else:
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1],  # substitution
                    edits[i - 1][j],      # deletion
                    edits[i][j - 1]       # insertion
                )
                print(f"\nCharacters differ ({str2[i-1]} vs {str1[j-1]}) at str2[{i-1}] and str1[{j-1}].")
                print(f"Calculating minimum of substitution {edits[i-1][j-1]}, deletion {edits[i-1][j]}, and insertion {edits[i][j-1]}.")
                print(f"Setting edits[{i}][{j}] = {edits[i][j]}.")

        # Print the matrix after each row is computed for clarity
        print(f"\nMatrix after processing row {i}:")
        for row in edits:
            print(row)

    # The bottom-right cell contains the minimum edit distance for the entire strings.
    return edits[-1][-1]

# Dummy data for testing the function
str1 = "kitten"
str2 = "sitting"
print(f"The Levenshtein distance between '{str1}' and '{str2}' is: {levenshteinDistance(str1, str2)}")
