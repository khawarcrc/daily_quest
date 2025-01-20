/**
 * OVERALL FLOW :
 * 1. Go through each word and count how many times each character appears in that word.
 * 2. For each character, keep track of the highest count found across all words.
 *    (Example: if 'd' appears 2 times in "did" and 3 times in "dodd", we keep 3.)
 * 3. After processing all words, create a final list of characters.
 * 4. Add each character repeated as many times as its highest count.
 * 5. Return the final character list (sorted for clean output).
 */

/**

/**
 * @param {string[]} words - List of words
 * @returns {string[]} - Minimum set of characters needed
 */
function minimumCharactersForWords(words) {
  
  // If words is not an array OR the array is empty → return empty list
  if (!Array.isArray(words) || words.length === 0) return [];

  // This Map will store the maximum count of each character seen in ANY word.
  // Example: if 't' appears 2 times in one word and 1 time in another → we store 2.
  const maxCount = new Map();

  // Loop through each word in the input list
  for (const word of words) {

    // Local Map to count characters inside the current word only
    // Example: for "deed" → { d:2, e:2 }
    const localCount = new Map();

    // Loop through each character inside the word
    for (const ch of word) {
      // Increase the count for this character in localCount.
      // (localCount.get(ch) || 0) means:
      //    → get existing count
      //    → if no count exists, use 0
      localCount.set(ch, (localCount.get(ch) || 0) + 1);
    }

    // Now update the global maxCount using the current word's localCount
    for (const [ch, cnt] of localCount.entries()) {
      // localCount.entries() gives pairs like ["d", 2]

      // Get the previous max count stored for this character
      const prev = maxCount.get(ch) || 0;

      // If the current word has more of this character than previous max → update it
      if (cnt > prev) maxCount.set(ch, cnt);
    }
  }

  // Now build an array that contains each character repeated max number of times
  const result = [];

  // Loop through each character and its max count from the global Map
  for (const [ch, cnt] of maxCount.entries()) {
    // Push the character 'cnt' times into the result list
    for (let i = 0; i < cnt; i++) {
      result.push(ch);
    }
  }

  // Sort the characters so the output looks consistent every time
  return result.sort();
}


const testData = [
  ["this", "that", "did", "deed", "them!"],
  [],
  [""],
  ["a", "bbb", "cc"],
  ["aa", "aaa", "aaaa"],
  ["Ab", "aB"],
  ["123", "3123"]
];

console.log("----- Minimum Characters For Words (Test Outputs) -----\n");

testData.forEach((words, index) => {
  console.log(`Test ${index + 1}`);
  console.log("Input:  ", words);
  console.log("Output: ", minimumCharactersForWords(words));
  console.log("--------------------------------------------------\n");
});