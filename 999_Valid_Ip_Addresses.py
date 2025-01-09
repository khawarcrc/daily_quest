"""
------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Given a numeric string, generate all possible valid IPv4 addresses 
that can be formed by inserting three dots in the string.

Rules of a valid IPv4 address:
1. It must consist of exactly four integer parts separated by dots.
   Example: A.B.C.D
2. Each part must be between 0 and 255.
3. No part can contain leading zeros unless the part is exactly "0".
   Example: "0", "10" are valid, but "01", "00" are invalid.

Example:
Input: "1921680"
Output: ["1.92.168.0", "19.216.8.0", "192.16.8.0"]
------------------------------------------------------------


------------------------------------------------------------
Problem Explanation:
------------------------------------------------------------
We are given a continuous string of digits like "25525511135".
We must insert three dots (".") to split it into four valid parts.

- Example split: "255.255.11.135"
   Part A = "255"
   Part B = "255"
   Part C = "11"
   Part D = "135"

Each part is valid because:
- They are between 0 and 255.
- They don’t contain leading zeros.

We must explore all possible placements of dots and collect only 
those combinations that form valid IPv4 addresses.
------------------------------------------------------------


------------------------------------------------------------
Execution Theory (How Code Works Step by Step):
------------------------------------------------------------
1. Start with an empty list `ipAddressesFound` to store results.

2. The function tries all possible places to insert the 1st dot.
   - Loop variable `i` decides where the first part ends.

3. For each possible first part:
   - If it's valid, move to the next step.
   - Otherwise, skip this split.

4. Try all possible places to insert the 2nd dot.
   - Loop variable `j` decides where the second part ends.

5. For each valid second part:
   - Try all possible places to insert the 3rd dot.
   - Loop variable `k` decides where the third part ends.

6. Now, the string is split into 4 parts:
   - First part: string[:i]
   - Second part: string[i:j]
   - Third part: string[j:k]
   - Fourth part: string[k:]

7. Validate each part using helper function `isValidPart`:
   - Convert to integer and check if 0 ≤ part ≤ 255.
   - Check if no leading zeros exist.

8. If all 4 parts are valid:
   - Join them with dots (".".join(...)).
   - Append the result to `ipAddressesFound`.

9. After all iterations:
   - Return the complete list of valid IP addresses.
------------------------------------------------------------
"""


# ------------------------------------------------------------
# Function to generate all valid IP addresses
# ------------------------------------------------------------
def validIPAddresses(string):
    # Store all valid IP addresses we find
    ipAddressesFound = []

    # --------------------------------------------------------
    # First Loop: Decide where the first part ends
    # --------------------------------------------------------
    for i in range(1, min(len(string), 4)):  # first part length ≤ 3
        currentIPAddressParts = ["", "", "", ""]  # placeholder for 4 parts
        currentIPAddressParts[0] = string[:i]  # first part

        # Validate first part
        if not isValidPart(currentIPAddressParts[0]):
            continue  # skip if invalid

        # --------------------------------------------------------
        # Second Loop: Decide where the second part ends
        # --------------------------------------------------------
        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i:j]  # second part

            # Validate second part
            if not isValidPart(currentIPAddressParts[1]):
                continue

            # --------------------------------------------------------
            # Third Loop: Decide where the third part ends
            # --------------------------------------------------------
            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k]  # third part
                currentIPAddressParts[3] = string[k:]   # fourth part

                # Validate third and fourth parts
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    # If valid, form the IP address and store it
                    ipAddressesFound.append(".".join(currentIPAddressParts))

    # Return all collected valid IP addresses
    return ipAddressesFound


# ------------------------------------------------------------
# Helper function to check if a part of IP is valid
# ------------------------------------------------------------
def isValidPart(string):
    # Convert string to integer
    stringAsInt = int(string)

    # Condition 1: must be between 0 and 255
    if stringAsInt > 255:
        return False

    # Condition 2: no leading zeros unless it is "0"
    return len(string) == len(str(stringAsInt))


# ------------------------------------------------------------
# Dummy Data for Testing
# ------------------------------------------------------------
testString = [
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
# Expected Output: ["255.255.11.135", "255.255.111.35"]
print(validIPAddresses(testString))

"""
------------------------------------------------------------
Industry Equivalent Real-Time Application:
------------------------------------------------------------
1. **Networking / System Tools**
   - Validating or generating possible IP configurations 
     from raw inputs during system setup.

2. **Cybersecurity**
   - Parsing logs or packet data where IP addresses may be 
     stored in compressed or concatenated form. 
   - Helps reconstruct original IPs.

3. **Form Validation**
   - User inputs a number string and system checks 
     all possible valid IP addresses before confirming.

4. **Data Cleaning / ETL Pipelines**
   - Raw datasets may contain corrupted IP fields (without dots). 
     This algorithm can reconstruct valid addresses 
     before storing them in a database.

In short, this helps in **validating, reconstructing, and parsing IP addresses** 
in any system that works with internet/networking data.
------------------------------------------------------------
"""
