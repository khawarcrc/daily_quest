# """
# ------------------------------------------------------------
# Problem Statement:
# ------------------------------------------------------------
# We are given a list of words (strings). 
# The task is to group words that are anagrams of each other.

# An anagram is a word formed by rearranging the letters of another word.
# For example:
#     - "eat", "tea", and "ate" are anagrams of each other.
#     - "bat" and "tab" are anagrams.
#     - "cat" has no other anagram in ["cat", "dog", "tac"] except "tac".

# We need to return a list of groups, where each group contains words that are anagrams.
# ------------------------------------------------------------
# """

# """
# ------------------------------------------------------------
# Explanation of Problem:
# ------------------------------------------------------------
# 1. We are asked to identify and group anagrams together.
# 2. Anagrams are identified by checking if two words have the same characters 
#    in different order.
#    - Example: "tea" and "eat"
#      Sorted("tea") → "aet"
#      Sorted("eat") → "aet"
#      Since they are equal → they are anagrams.
# 3. The solution involves:
#    - Sorting each word to find a "signature" key.
#    - Grouping all words with the same signature.
# 4. Finally, return a list of groups of anagrams.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Execution Walkthrough with Example:
# ------------------------------------------------------------
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

# Step 1: sortedWords = ["aet", "aet", "ant", "aet", "ant", "abt"]
# Step 2: indices = [0,1,2,3,4,5]
# Step 3: Sort indices by sortedWords → [5,2,4,0,1,3]
#          (words = ["bat", "tan", "nat", "eat", "tea", "ate"])

# Step 4: Iterate:
#    - First group → "abt" → ["bat"]
#    - Next group → "ant" → ["tan", "nat"]
#    - Next group → "aet" → ["eat", "tea", "ate"]

# Final Output: [["bat"], ["tan","nat"], ["eat","tea","ate"]]
# ------------------------------------------------------------
# """


def groupAnagrams(words):
    #  Step 1: Handle the edge case
    # If the list of words is empty, return an empty list immediately
    if len(words) == 0: 
        return []

    #  Step 2: Create a "sorted signature" for each word
    # Example: words = ["eat", "tea", "bat"]
    # sortedWords = ["aet", "aet", "abt"]
    sortedWords = ["".join(sorted(w)) for w in words]

    #  Step 3: Create a list of indices [0, 1, 2, ...] 
    # that will later help us sort words by their anagram signature
    indices = [i for i in range(len(words))]

    #  Step 4: Sort the indices list based on sortedWords
    # This ensures that words with the same signature come together
    indices.sort(key=lambda x: sortedWords[x])

    #  Step 5: Prepare result container
    result = []  # This will store final groups of anagrams
    currentAnagramGroup = []  # Temporary list for current group
    currentAnagram = sortedWords[indices[0]]  # First anagram signature

    #  Step 6: Iterate over indices and group words
    for index in indices:
        word = words[index]              # Original word from list
        sortedWord = sortedWords[index]  # Its sorted signature

        if sortedWord == currentAnagram:
            # If it belongs to the same group → add it
            currentAnagramGroup.append(word)
            continue  # Move to next word

        # If it's a new anagram group:
        result.append(currentAnagramGroup)  # Save the old group
        currentAnagramGroup = [word]        # Start a new group
        currentAnagram = sortedWord         # Update current anagram signature

    #  Step 7: Append the last collected group
    result.append(currentAnagramGroup)

    #  Step 8: Return the grouped anagrams
    return result



#  Dummy data to test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))
# Expected: [["bat"], ["tan","nat"], ["eat","tea","ate"]]

# """
# ------------------------------------------------------------
# Industry Equivalent Scenario:
# ------------------------------------------------------------
# This problem is very practical in real-world applications.

# 1. **Search Engines / Spell Checkers**
#    - Detecting words that are permutations of each other (typo corrections).
#    - Example: If a user types "tca", the system should suggest "cat".

# 2. **Data Deduplication**
#    - In large datasets, anagrams may appear multiple times. 
#    - Grouping them helps in removing duplicates or organizing text data.

# 3. **Cryptography / Security**
#    - Many ciphers rearrange letters (permutations). 
#    - Grouping words by anagram signatures helps in pattern detection.

# 4. **DNA Sequencing / Bioinformatics**
#    - DNA/RNA sequences can be rearranged; detecting structural similarity 
#      can help in analysis.

# 5. **E-commerce Search**
#    - Handling queries where product names are jumbled or mistyped.
#    - Example: "stop" vs "post" → both can map to similar product groups.
# ------------------------------------------------------------
# """
