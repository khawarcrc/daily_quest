// Constant representing the result when the home team wins
const HOME_TEAM_WON = 1;

// Function to determine the tournament winner
function tournamentWinner(competitions, results) {
    // Initialize the current best team as an empty string
    let currentBestTeam = "";
    // Initialize the scores object with the current best team having 0 points
    let scores = { [currentBestTeam]: 0 };
    
    console.log("Initial state:");
    console.log(`Current best team: ${currentBestTeam}`);
    console.log("Scores:", scores);
    
    // Loop through each competition and corresponding result
    for (let idx = 0; idx < competitions.length; idx++) {
        const competition = competitions[idx];
        const result = results[idx];  // Get the result of the current competition
        const homeTeam = competition[0];  // Get the home team
        const awayTeam = competition[1];  // Get the away team
        
        console.log(`\nCompetition ${idx + 1}: ${homeTeam} (home) vs ${awayTeam} (away)`);
        console.log(`Result: ${result === HOME_TEAM_WON ? 'Home team won' : 'Away team won'}`);
        
        // Determine the winning team based on the result
        const winningTeam = result === HOME_TEAM_WON ? homeTeam : awayTeam;
        console.log(`Winning team: ${winningTeam}`);
        
        // Update the score of the winning team
        updateScores(winningTeam, 3, scores);
        console.log("Updated Scores:", scores);
        
        // Check if the current winning team's score is greater than the current best team's score
        if (scores[winningTeam] > scores[currentBestTeam]) {
            // Update the current best team
            currentBestTeam = winningTeam;
            console.log(`New current best team: ${currentBestTeam}`);
        }
    }
    
    // Return the team with the highest score at the end of the tournament
    console.log(`\nFinal winner: ${currentBestTeam}`);
    return currentBestTeam;
}

// Function to update the scores
function updateScores(team, points, scores) {
    // If the team is not already in the scores object, add it with a score of 0
    if (!scores.hasOwnProperty(team)) {
        scores[team] = 0;
        console.log(`Added ${team} to scores with initial score of 0`);
    }
    
    // Add the points to the team's score
    scores[team] += points;
    console.log(`Added ${points} points to ${team}'s score`);
}

// Sample input data
const competitions = [
    ["HTML", "C#"],  // Competition 1: Team A (home) vs Team B (away)
    ["C#", "Python"],  // Competition 2: Team B (home) vs Team C (away)
    ["Python", "HTML"]  // Competition 3: Team C (home) vs Team A (away)
];

const results = [0, 0, 1];  // Results: Team A wins, Team C wins, Team C wins

// Call the function and print the result
const winner = tournamentWinner(competitions, results);
console.log("The winning team is:", winner);  // Output the winning team



// 1. Iterates through competitions and results to identify the winning team for each match.
// 2. Updates the winning team's score by adding 3 points using the updateScores function.
// 3. Tracks the team with the highest score throughout the tournament.
// 4. Returns the team with the highest score as the tournament winner after all competitions are processed.
