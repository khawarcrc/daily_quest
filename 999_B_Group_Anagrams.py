"""
------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
We are given a list of words. We need to group together all the words 
that are anagrams of each other.

An anagram is a word formed by rearranging the letters of another word. 
For example:
- "listen" and "silent" are anagrams.
- "eat", "tea", and "ate" are anagrams.

The goal is to return a list of grouped anagrams, where each group 
contains words that are anagrams of each other.


------------------------------------------------------------
Problem Explanation:
------------------------------------------------------------
Suppose we have a list of words:
["eat", "tea", "tan", "ate", "nat", "bat"]

- "eat", "tea", "ate" → all have the same letters when sorted → "aet"
- "tan", "nat" → both sort to "ant"
- "bat" → sorts to "abt"

So, the grouped output should look like:
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

This works because if two words are anagrams, their sorted 
letters will always form the same key (e.g., "aet").
------------------------------------------------------------


------------------------------------------------------------
Code Execution Theory (Step by Step):
------------------------------------------------------------
1. Define a dictionary called `anagrams` that will store the groups.
   - Keys = the sorted version of each word (e.g., "aet").
   - Values = a list of words that match this sorted key.

2. For each word in the input list:
   - Sort the word alphabetically (e.g., "tea" → "aet").
   - Check if this sorted word already exists in `anagrams` dictionary.
   - If yes, append the word to that group.
   - If not, create a new entry with this sorted word as the key
     and put the word in a new list.

3. Finally, return all the grouped lists of anagrams 
   by taking only the dictionary values (not the keys).

4. Execution builds the dictionary gradually and then 
   extracts the grouped words as the final result.
------------------------------------------------------------
"""


def groupAnagrams(words):
    # Dictionary to store grouped anagrams
    # Key   -> sorted version of the word (e.g., "aet")
    # Value -> list of words that are anagrams of each other
    anagrams = {}

    # Loop through each word in the list
    for word in words:
        # Sort the word alphabetically, then join it back into a string
        # Example: "tea" -> ['a','e','t'] -> "aet"
        sortedWord = "".join(sorted(word))

        # If the sorted word already exists as a key in dictionary,
        # append the current word to that list
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            # Otherwise, create a new list with this word
            anagrams[sortedWord] = [word]

    # Return the values (lists of grouped anagrams)
    # Convert dictionary values into a list before returning
    return list(anagrams.values())


# ------------------------------------------------------------
# Dummy Data for Testing
# ------------------------------------------------------------
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Expected Output:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(groupAnagrams(words))



