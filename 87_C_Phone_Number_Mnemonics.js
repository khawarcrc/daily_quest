// Function to generate all possible mnemonics for a given phone number
function phoneNumberMnemonics(phoneNumber) {
    // Base case: If the phone number is empty, return an empty array.
    if (!phoneNumber.length) return [];
  
    // Start with a generator function to handle combinations on-the-fly.
    function* generateMnemonics(index, currentMnemonic) {
      // If the index reaches the end of the phone number, yield the current mnemonic.
      if (index === phoneNumber.length) {
        yield currentMnemonic;
        return;
      }
  
      // Retrieve the list of letters corresponding to the current digit.
      const digit = phoneNumber[index];
      const letters = DIGIT_LETTERS[digit];
  
      // Iterate through each letter for the current digit.
      for (const letter of letters) {
        // Recur with the next index and updated mnemonic.
        yield* generateMnemonics(index + 1, currentMnemonic + letter);
      }
    }
  
    // Use the generator to generate mnemonics on-the-fly and collect them in an array.
    return Array.from(generateMnemonics(0, ""));
  }
  
  // Mapping of digits to their corresponding letters as found on a phone keypad.
  const DIGIT_LETTERS = {
    "0": ["0"], // 0 maps to itself.
    "1": ["1"], // 1 maps to itself.
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
  };
  
  // Example usage with dummy data:
  // Input phone number is "23".
  // Expected output: All combinations of letters for "2" and "3".
  const dummyPhoneNumber = "23";
  console.log(phoneNumberMnemonics(dummyPhoneNumber));
  


// phoneNumberMnemonics function: 
// - Generates all possible mnemonics for a given phone number.
// - Base case: If the input phone number is empty, returns an empty array.

// generateMnemonics generator function: 
// - A generator function used to recursively build all possible combinations of letters 
//   corresponding to each digit in the phone number.

// Recursive step: 
// - Retrieves the list of letters for the current digit and iterates through each letter.
// - For each letter, it recursively calls itself with the next index and the updated mnemonic.

// Base case of recursion: 
// - Once the index reaches the end of the phone number, it yields the current mnemonic (completed combination of letters).

// DIGIT_LETTERS object: 
// - Maps each digit (0-9) to a list of letters, mimicking the letter mapping on a traditional phone keypad.

// Array.from: 
// - Converts the generator’s output into an array, returning all possible mnemonics.

// Example usage: 
// - For input "23", the function outputs all combinations of letters corresponding to the digits 2 and 3 (e.g., "ad", "ae", "af", etc.).
