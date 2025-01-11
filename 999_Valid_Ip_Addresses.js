/*
------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Given a numeric string, generate all possible valid IPv4 addresses 
by inserting three dots.

Rules:
1. Must have exactly 4 parts (A.B.C.D).
2. Each part must be 0–255.
3. No leading zeros allowed, unless the part is "0".
------------------------------------------------------------

------------------------------------------------------------
Execution Theory (How Code Works Step by Step):
------------------------------------------------------------
1. Start with an empty array `results` to store valid IPs.

2. Use three nested loops to decide where the 3 dots go:
   - `i` → end index of the first part.
   - `j` → end index of the second part.
   - `k` → end index of the third part.

3. This splits the string into four parts:
   - part1 = str.slice(0, i)
   - part2 = str.slice(i, j)
   - part3 = str.slice(j, k)
   - part4 = str.slice(k)

4. Validate each part using `isValidPart`:
   - Convert to number and check if in range [0–255].
   - Ensure no leading zeros unless the number is exactly "0".

5. If all parts are valid, combine them into an IP string 
   using template literals (e.g., `${part1}.${part2}.${part3}.${part4}`).

6. Push the valid IP into the `results` array.

7. After all iterations, return `results` containing 
   all valid IPv4 addresses.
------------------------------------------------------------
*/

function validIPAddresses(str) {
  const results = [];

  // Outer loop for the first dot
  for (let i = 1; i <= 3 && i < str.length; i++) {
    const part1 = str.slice(0, i);
    if (!isValidPart(part1)) continue;

    // Second loop for the second dot
    for (let j = i + 1; j <= i + 3 && j < str.length; j++) {
      const part2 = str.slice(i, j);
      if (!isValidPart(part2)) continue;

      // Third loop for the third dot
      for (let k = j + 1; k <= j + 3 && k < str.length; k++) {
        const part3 = str.slice(j, k);
        const part4 = str.slice(k);

        // Fourth part must not be empty
        if (!part4) continue;

        if (isValidPart(part3) && isValidPart(part4)) {
          results.push(`${part1}.${part2}.${part3}.${part4}`);
        }
      }
    }
  }

  return results;
}

// ------------------------------------------------------------
// Helper function to check if a part of IP is valid
// ------------------------------------------------------------
function isValidPart(segment) {
  const num = Number(segment);

  // Range check
  if (num < 0 || num > 255) return false;

  // Leading zero check (e.g., "01", "00" invalid, but "0" valid)
  if (segment.length > 1 && segment.startsWith("0")) return false;

  return true;
}

// ------------------------------------------------------------
// Testing
// ------------------------------------------------------------
console.log(validIPAddresses("1921680"));
// Expected: [ "1.92.168.0", "19.216.8.0", "192.16.8.0" ]

console.log(validIPAddresses("25525511135"));
// Expected: [ "255.255.11.135", "255.255.111.35" ]
