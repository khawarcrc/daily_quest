# ------------------------------------------------------------
# Problem: Minimum Characters For Words
# ------------------------------------------------------------
# Given a list of words, return the minimum set of characters
# required to be able to form each word individually.
# For every character, include it as many times as the maximum
# number of occurrences it has in ANY single word.
#
# Example:
# words = ["this", "that", "did", "deed", "them!"]
# max counts: t:2, h:1, i:1, s:1, a:1, d:2, e:2, m:1, !:1
# Output (order irrelevant): ['t','t','h','i','s','a','d','d','e','e','m','!']
#
# ------------------------------------------------------------
# Execution Flow:
# 1. If the list is empty → return [].
# 2. Create a global counter (max_char_count) for maximum frequency
#    of each character across all words.
# 3. For each word:
#       - Count characters in the word.
#       - Update max_char_count with the max frequency found.
# 4. Build the result list by adding each character repeated
#    max_char_count[c] times.
# 5. Return the final list (sorted if deterministic order is needed).
# ------------------------------------------------------------


from collections import Counter
from typing import List

def minimumCharactersForWords(words: List[str]) -> List[str]:
    # Edge case: empty input
    if not words:
        return []

    # This will store the maximum count of each character
    max_char_count = Counter()

    # Step 1: Process each word
    for word in words:
        # Count characters in this word
        char_count = Counter(word)

        # Update global maximum character counts
        for ch, cnt in char_count.items():
            max_char_count[ch] = max(max_char_count[ch], cnt)

    # Step 2: Build the output list
    result = []
    for ch, cnt in max_char_count.items():
        result.extend([ch] * cnt)

    # Optional: sort for deterministic output (not required for logic)
    return sorted(result)


# ------------------------------------------------------------
# Dummy Test Cases
# ------------------------------------------------------------
if __name__ == "__main__":
    test_data = [
        ["this", "that", "did", "deed", "them!"],
        [],
        [""],
        ["a", "bbb", "cc"],
        ["aa", "aaa", "aaaa"],
        ["Ab", "aB"],
        ["123", "3123"]
    ]

    for i, words in enumerate(test_data, 1):
        print(f"Test {i}: Input = {words}")
        print("Output:", minimumCharactersForWords(words))
        print("-" * 50)
