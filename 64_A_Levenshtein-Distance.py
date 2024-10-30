# """
# Problem Statement:
# The Levenshtein distance between two strings is defined as the minimum number of
# single-character edits (insertions, deletions, or substitutions) required to transform
# one string into the other. Given two strings, 'str1' and 'str2', write a function to
# compute their Levenshtein distance.

# Code Execution Theory:
# 1. Initialize a 2D matrix 'edits' where edits[i][j] represents the minimum edit
#    distance between the first i characters of str2 and the first j characters of str1.
#    - The first row represents progressively converting an empty string into str1
#      by insertions.
#    - The first column represents progressively deleting characters from str2 to
#      achieve an empty string.

# 2. Fill the first column incrementally since transforming any prefix of str2 into
#    an empty string requires deletions (cost of 1 per character).

# 3. Iterate through each character in both strings to update the matrix:
#    - If characters match, copy the diagonal value (no additional cost).
#    - If characters differ, compute the minimum edit distance by considering
#      substitution, deletion, or insertion.

# 4. The final answer, or minimum edit distance, will be located in the bottom-right
#    cell of the matrix, representing the transformation cost of str2 into str1.

# Edge Cases:
# - Both strings are empty (distance = 0).
# - One string is empty and the other is not (distance = length of non-empty string).
# - Strings with no common characters (distance = length of the longer string).
# """


def levenshteinDistance(str1, str2):
    # Initialize a 2D list where edits[i][j] will hold the minimum edit distance
    # between the first i characters of str2 and the first j characters of str1.
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    # Fill the first column with incremental values, representing the cost
    # of deleting characters from str2 to make it an empty string.
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    # Iterate over each cell in the matrix starting from the first row.
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # If characters match, take the diagonal value (no extra cost).
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            # If characters differ, take the minimum cost of three operations:
            # substitution, deletion, or insertion.
            else:
                edits[i][j] = 1 + min(
                    edits[i - 1][j - 1],  # substitution
                    edits[i - 1][j],      # deletion
                    edits[i][j - 1]       # insertion
                )
                
    # The bottom-right cell contains the minimum edit distance for the entire strings.
    return edits[-1][-1]

# Dummy data for testing the function
str1 = "kitten"
str2 = "sitting"
print(f"The Levenshtein distance between '{str1}' and '{str2}' is: {levenshteinDistance(str1, str2)}")




# """
# Example:
# Let's calculate the Levenshtein distance between the strings:
# - str1 = "kitten"
# - str2 = "sitting"

# Steps:
# 1. Initialize a matrix 'edits' of size (len(str2) + 1) x (len(str1) + 1).
#    - For "kitten" (length 6) and "sitting" (length 7), we create a matrix of size 8 x 7.
#    - The first row and column are initialized to represent the cost of converting
#      from an empty string to the target substring.

#    Initial 'edits' matrix:
#        k  i  t  t  e  n
#     [[0, 1, 2, 3, 4, 5, 6], 
#   s [1, 0, 0, 0, 0, 0, 0], 
#   i [2, 0, 0, 0, 0, 0, 0], 
#   t [3, 0, 0, 0, 0, 0, 0], 
#   t [4, 0, 0, 0, 0, 0, 0], 
#   i [5, 0, 0, 0, 0, 0, 0], 
#   n [6, 0, 0, 0, 0, 0, 0], 
#   g [7, 0, 0, 0, 0, 0, 0]]

# 2. Populate the matrix using the following rules:
#    - If characters match (str1[j-1] == str2[i-1]), copy the diagonal value.
#    - If characters don't match, set edits[i][j] to 1 + minimum of:
#        a) edits[i-1][j-1] for substitution
#        b) edits[i-1][j] for deletion
#        c) edits[i][j-1] for insertion

# 3. Populate matrix for the example:
#    - For 's' in str2 and 'k' in str1, they differ, so we compute the minimum:
#        min(substitution, deletion, insertion) and set edits[1][1] = 1.
#    - For 'i' in str2 and 'i' in str1, they match, so we copy the diagonal: edits[2][2] = 1.
#    - Continue this for each cell until the matrix is filled.

# 4. Final 'edits' matrix after filling all cells:
#     [[0, 1, 2, 3, 4, 5, 6],
#      [1, 1, 2, 3, 4, 5, 6],
#      [2, 2, 1, 2, 3, 4, 5],
#      [3, 3, 2, 1, 2, 3, 4],
#      [4, 4, 3, 2, 1, 2, 3],
#      [5, 5, 4, 3, 2, 2, 3],
#      [6, 5, 5, 4, 3, 3, 2],
#      [7, 6, 6, 5, 4, 4, 3]]

# 5. Result:
#    - The Levenshtein distance is found at the bottom-right corner of the matrix.
#    - In this example, 'edits[7][6]' = 3, meaning the minimum edit distance
#      between "kitten" and "sitting" is 3.
# """
