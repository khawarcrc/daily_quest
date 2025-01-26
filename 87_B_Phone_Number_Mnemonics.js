// Function to generate all possible mnemonics for a given phone number
function phoneNumberMnemonics(phoneNumber) {
    // Base case: If the phone number is empty, return an empty array.
    if (!phoneNumber.length) return [];
  
    // Start with a list containing an empty string as the initial combination.
    let mnemonicsFound = [''];
  
    // Iterate through each digit in the phone number using a while loop.
    let index = 0;
    while (index < phoneNumber.length) {
      // Retrieve the list of letters corresponding to the current digit.
      const digit = phoneNumber[index];
      const letters = DIGIT_LETTERS[digit];
  
      // Generate new combinations by appending each letter to existing mnemonics.
      const newMnemonics = [];
      for (let i = 0; i < mnemonicsFound.length; i++) {
        for (let j = 0; j < letters.length; j++) {
          newMnemonics.push(mnemonicsFound[i] + letters[j]);
        }
      }
  
      // Update mnemonicsFound with the newly generated combinations.
      mnemonicsFound = newMnemonics;
  
      // Move to the next digit.
      index++;
    }
  
    // Return the list of all possible mnemonics.
    return mnemonicsFound;
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
  