# Problem Statement:
# The problem is to generate all possible letter combinations for a given phone number based on the mapping of digits 
# to letters found on a phone keypad. Each digit maps to a set of letters (e.g., 2 -> ["a", "b", "c"]). 
# Digits 0 and 1 map to themselves as they do not have associated letters. 
# The goal is to return all possible combinations of letters (mnemonics) that can be formed by the given phone number.


# Code Execution Theory:
# 1. The function `phoneNumberMnemonics` is the entry point and initializes variables to track the current mnemonic and store all found mnemonics.
# 2. A helper function `phoneNumberMnemonicsHelper` is used for recursive traversal, generating combinations by iterating over possible letters for each digit.
# 3. Base case: When the current index reaches the length of the phone number, the current mnemonic is added to the result list.
# 4. Recursive case: Iterate through the letters for the current digit, update the current mnemonic, and recurse for the next index.
# 5. The result is a list of all possible mnemonics for the given phone number.

# Code Implementation:

def phoneNumberMnemonics(phoneNumber): 
    # Initialize a list to store the current combination (mnemonic).
    # Each position starts with "0" to match the length of the phone number.
    currentMnemonic = ['0'] * len(phoneNumber)
    
    # List to store all mnemonics found during the recursive traversal.
    mnemonicsFound = []
    
    # Call the helper function to start generating mnemonics.
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
    
    # Return the list of all possible mnemonics.
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound): 
    # Base case: If the current index reaches the end of the phone number,
    # join the current mnemonic into a string and add it to the result list.
    if idx == len(phoneNumber): 
        mnemonics = ''.join(currentMnemonic)
        mnemonicsFound.append(mnemonics)
    else: 
        # Get the current digit from the phone number.
        digit = phoneNumber[idx]
        
        # Retrieve the list of letters corresponding to the current digit.
        letters = DIGIT_LETTERS[digit]
        
        # Iterate through each letter for the current digit.
        for letter in letters: 
            # Update the current position in the mnemonic with the current letter.
            currentMnemonic[idx] = letter 
            
            # Recur to the next digit in the phone number.
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)

# Mapping of digits to their corresponding letters as found on a phone keypad.
DIGIT_LETTERS = {
    "0": ["0"],  # 0 maps to itself.
    "1": ["1"],  # 1 maps to itself.
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

# Example usage with dummy data:
# Input phone number is "23".
# Expected output: All combinations of letters for "2" and "3".
dummy_phone_number = "23"
print(phoneNumberMnemonics(dummy_phone_number))
