// Problem Statement
// The goal of this function is to match interns to teams based on their preferences, while
// also considering each team's preferred ranking of interns. Each intern has a ranked list
// of team preferences, and each team has a ranked list of intern preferences. The function
// ensures that the final matching is "stable," meaning no intern-team pair would rather be
// matched with each other over their current assignments.

// Code Execution Theory

// Initialization:
// - Begin by initializing:
//   - `chosenInterns` as an object to store each team’s current assigned intern.
//   - `freeInterns` list, initially holding all intern indices as they start "unmatched."
//   - `currentInternChoices` array to track each intern's next choice from their preferences.

// Team Ranking Maps:
// - Convert each team’s list of preferences into an array of maps (`teamMaps`) for quick
//   access to each intern’s rank according to that team.

// Matching Process:
// - While there are free interns:
//   - An intern chooses their top team from the remaining untried preferences.
//   - If the team is free, the intern is matched with that team.
//   - If the team already has an intern, the function compares the team’s preference
//     for the current intern versus the previous one.
//   - If the new intern is preferred, the previous intern is freed and the new intern
//     is assigned. Otherwise, the current intern remains free and moves on to their
//     next preferred team.

// Output Matches:
// - After all interns are matched stably, the function returns the list of matches
//   as intern-team pairs.

function stableInternships(interns, teams) {
  // Initialize object to store chosen intern for each team
  const chosenInterns = {};

  // List of free interns, initially all interns are free
  const freeInterns = Array.from({ length: interns.length }, (_, i) => i);

  // Track the current choice index of each intern
  const currentInternChoices = Array(interns.length).fill(0);

  // Convert each team's list into a ranking map for easy lookup
  const teamMaps = teams.map((team) => {
    const rank = {};
    team.forEach((internNum, i) => {
      rank[internNum] = i;
    });
    return rank;
  });

  // Process each free intern until there are none left
  while (freeInterns.length > 0) {
    // Get the current free intern
    const internNum = freeInterns.pop();

    // Intern's team preference list and next choice
    const intern = interns[internNum];
    const teamPreference = intern[currentInternChoices[internNum]];

    // Move to the next team in this intern's preference list
    currentInternChoices[internNum] += 1;

    // If the preferred team is not currently occupied by any intern
    if (!(teamPreference in chosenInterns)) {
      // Assign this intern to the team
      chosenInterns[teamPreference] = internNum;
      continue;
    }

    // Team is already taken; check if this intern has higher priority
    const previousIntern = chosenInterns[teamPreference];
    const previousInternRank = teamMaps[teamPreference][previousIntern];
    const currentInternRank = teamMaps[teamPreference][internNum];

    // If the new intern is preferred over the current one, replace them
    if (currentInternRank < previousInternRank) {
      // Previous intern becomes free again
      freeInterns.push(previousIntern);
      chosenInterns[teamPreference] = internNum;
    } else {
      // Current intern remains free if not preferred
      freeInterns.push(internNum);
    }
  }

  // Prepare the final match results
  const matches = Object.entries(chosenInterns).map(([teamNum, internNum]) => [
    parseInt(internNum),
    parseInt(teamNum),
  ]);
  return matches;
}

// Dummy data to test the function
const interns = [
  [1, 0], // Intern 0 prefers Team 1, then Team 0
  [0, 1], // Intern 1 prefers Team 0, then Team 1
];

const teams = [
  [1, 0], // Team 0 prefers Intern 1, then Intern 0
  [0, 1], // Team 1 prefers Intern 0, then Intern 1
];

// Call the function with the dummy data
console.log(stableInternships(interns, teams));
