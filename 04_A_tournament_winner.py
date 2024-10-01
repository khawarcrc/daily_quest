# Problem Statement: Determine the Tournament Winner
# Given a list of competitions between teams and their results, determine which team won the tournament.
# Each competition consists of two teams (home and away), and each result indicates whether the home team or away team won.
# The winning team earns 3 points for each win. The team with the most points at the end of the tournament is declared the winner.

# Steps to Solve:
# 1. Define a constant `HOME_TEAM_WON` to represent a win by the home team.
# 2. Define the `tournamentWinner` function to determine the tournament winner.
#    a. Initialize an empty string `currentBestTeam` to store the team with the highest score.
#    b. Create a `scores` dictionary to store the points for each team. Set the `currentBestTeam` score to 0 initially.
# 3. Loop through each competition and its corresponding result:
#    a. Unpack the home and away teams from the competition.
#    b. Determine the winning team based on the result: If the home team wins, set `winningTeam` to the home team; otherwise, set it to the away team.
#    c. Call the `updateScores` function to update the winning team's score by adding 3 points.
#    d. If the winning team's score is higher than the `currentBestTeam` score, update `currentBestTeam` to the winning team.
# 4. Define the `updateScores` function:
#    a. Check if the team is already in the `scores` dictionary. If not, initialize its score to 0.
#    b. Add the specified number of points (3) to the team's score.
# 5. After looping through all competitions, return the `currentBestTeam` with the highest score.
# 6. Use sample input data (`competitions` and `results`) to test the function and print the winning team.


# Constants
HOME_TEAM_WON = 1  # This constant represents the result when the home team wins.


# Function to determine the tournament winner
def tournamentWinner(competitions, results):
    # Initialize the current best team as an empty string
    currentBestTeam = ""
    # Initialize the scores dictionary with the current best team having 0 points
    scores = {currentBestTeam: 0}

    # Loop through each competition and corresponding result
    for idx, competition in enumerate(competitions):
        result = results[idx]  # Get the result of the current competition
        homeTeam, awayTeam = competition  # Unpack the home and away teams

        # Determine the winning team based on the result
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        # Update the score of the winning team
        updateScores(winningTeam, 3, scores)

        # Check if the current winning team's score is greater than the current best team's score
        if scores[winningTeam] > scores[currentBestTeam]:
            # Update the current best team
            currentBestTeam = winningTeam

    # Return the team with the highest score at the end of the tournament
    return currentBestTeam


# Function to update the scores
def updateScores(team, points, scores):
    # If the team is not already in the scores dictionary, add it with a score of 0
    if team not in scores:
        scores[team] = 0

    # Add the points to the team's score
    scores[team] += points


# Sample input data
competitions = [
    ["HTML", "C#"],  # Competition 1: Team A (home) vs Team B (away)
    ["C#", "Python"],  # Competition 2: Team B (home) vs Team C (away)
    ["Python", "HTML"],  # Competition 3: Team C (home) vs Team A (away)
]

results = [0, 0, 1]  # Results: Team A wins, Team C wins, Team C wins

# Call the function and print the result
winner = tournamentWinner(competitions, results)
print("The winning team is:", winner)  # Output the winning team


# # Constants
# HOME_TEAM_WON = 1  # This constant represents the result when the home team wins.

# # Function to determine the tournament winner
# def tournamentWinner(competitions, results):
#     # Initialize the current best team as an empty string
#     currentBestTeam = ""
#     # Initialize the scores dictionary with the current best team having 0 points
#     scores = {currentBestTeam: 0}

#     print("Initial state:")
#     print(f"Current best team: {currentBestTeam}")
#     print(f"Scores: {scores}")

#     # Loop through each competition and corresponding result
#     for idx, competition in enumerate(competitions):
#         result = results[idx]  # Get the result of the current competition
#         homeTeam, awayTeam = competition  # Unpack the home and away teams

#         print(f"\nCompetition {idx + 1}: {homeTeam} (home) vs {awayTeam} (away)")
#         print(f"Result: {'Home team won' if result == HOME_TEAM_WON else 'Away team won'}")

#         # Determine the winning team based on the result
#         winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
#         print(f"Winning team: {winningTeam}")

#         # Update the score of the winning team
#         updateScores(winningTeam, 3, scores)
#         print(f"Updated Scores: {scores}")

#         # Check if the current winning team's score is greater than the current best team's score
#         if scores[winningTeam] > scores[currentBestTeam]:
#             # Update the current best team
#             currentBestTeam = winningTeam
#             print(f"New current best team: {currentBestTeam}")

#     # Return the team with the highest score at the end of the tournament
#     print(f"\nFinal winner: {currentBestTeam}")
#     return currentBestTeam

# # Function to update the scores
# def updateScores(team, points, scores):
#     # If the team is not already in the scores dictionary, add it with a score of 0
#     if team not in scores:
#         scores[team] = 0
#         print(f"Added {team} to scores with initial score of 0")

#     # Add the points to the team's score
#     scores[team] += points
#     print(f"Added {points} points to {team}'s score")

# # Sample input data
# competitions = [
#     ["HTML", "C#"],  # Competition 1: Team A (home) vs Team B (away)
#     ["C#", "Python"],  # Competition 2: Team B (home) vs Team C (away)
#     ["Python", "HTML"]   # Competition 3: Team C (home) vs Team A (away)
# ]

# results = [0, 0, 1]  # Results: Team A wins, Team C wins, Team C wins

# # Call the function and print the result
# winner = tournamentWinner(competitions, results)
# print("The winning team is:", winner)  # Output the winning team
