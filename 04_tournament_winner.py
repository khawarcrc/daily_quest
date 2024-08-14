# # Constants
# HOME_TEAM_WON = 1  # This constant represents the result when the home team wins.

# # Function to determine the tournament winner
# def tournamentWinner(competitions, results): 
#     # Initialize the current best team as an empty string
#     currentBestTeam = ""
#     # Initialize the scores dictionary with the current best team having 0 points
#     scores = {currentBestTeam: 0}
    
#     # Loop through each competition and corresponding result
#     for idx, competition in enumerate(competitions): 
#         result = results[idx]  # Get the result of the current competition
#         homeTeam, awayTeam = competition  # Unpack the home and away teams
        
#         # Determine the winning team based on the result
#         winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        
#         # Update the score of the winning team
#         updateScores(winningTeam, 3, scores)
        
#         # Check if the current winning team's score is greater than the current best team's score
#         if scores[winningTeam] > scores[currentBestTeam]:
#             # Update the current best team
#             currentBestTeam = winningTeam
    
#     # Return the team with the highest score at the end of the tournament
#     return currentBestTeam

# # Function to update the scores
# def updateScores(team, points, scores): 
#     # If the team is not already in the scores dictionary, add it with a score of 0
#     if team not in scores: 
#         scores[team] = 0
        
#     # Add the points to the team's score
#     scores[team] += points          

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


# Constants
HOME_TEAM_WON = 1  # This constant represents the result when the home team wins.

# Function to determine the tournament winner
def tournamentWinner(competitions, results): 
    # Initialize the current best team as an empty string
    currentBestTeam = ""
    # Initialize the scores dictionary with the current best team having 0 points
    scores = {currentBestTeam: 0}
    
    print("Initial state:")
    print(f"Current best team: {currentBestTeam}")
    print(f"Scores: {scores}")
    
    # Loop through each competition and corresponding result
    for idx, competition in enumerate(competitions): 
        result = results[idx]  # Get the result of the current competition
        homeTeam, awayTeam = competition  # Unpack the home and away teams
        
        print(f"\nCompetition {idx + 1}: {homeTeam} (home) vs {awayTeam} (away)")
        print(f"Result: {'Home team won' if result == HOME_TEAM_WON else 'Away team won'}")
        
        # Determine the winning team based on the result
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        print(f"Winning team: {winningTeam}")
        
        # Update the score of the winning team
        updateScores(winningTeam, 3, scores)
        print(f"Updated Scores: {scores}")
        
        # Check if the current winning team's score is greater than the current best team's score
        if scores[winningTeam] > scores[currentBestTeam]:
            # Update the current best team
            currentBestTeam = winningTeam
            print(f"New current best team: {currentBestTeam}")
    
    # Return the team with the highest score at the end of the tournament
    print(f"\nFinal winner: {currentBestTeam}")
    return currentBestTeam

# Function to update the scores
def updateScores(team, points, scores): 
    # If the team is not already in the scores dictionary, add it with a score of 0
    if team not in scores: 
        scores[team] = 0
        print(f"Added {team} to scores with initial score of 0")
        
    # Add the points to the team's score
    scores[team] += points          
    print(f"Added {points} points to {team}'s score")

# Sample input data
competitions = [
    ["HTML", "C#"],  # Competition 1: Team A (home) vs Team B (away)
    ["C#", "Python"],  # Competition 2: Team B (home) vs Team C (away)
    ["Python", "HTML"]   # Competition 3: Team C (home) vs Team A (away)
]

results = [0, 0, 1]  # Results: Team A wins, Team C wins, Team C wins

# Call the function and print the result
winner = tournamentWinner(competitions, results)
print("The winning team is:", winner)  # Output the winning team



# Overall Process Explanation:

# 1. Define Constants:
#    - Create a constant HOME_TEAM_WON to represent when the home team wins.

# 2. tournamentWinner Function:
#    - Initialize Variables: 
#      - Start with an empty string for currentBestTeam and a dictionary scores 
#        to keep track of each team's points.
#    - Loop Through Competitions: 
#      - For each competition, determine the winner based on the results list.
#    - Update Scores: 
#      - Use the updateScores function to add points to the winning team's total.
#    - Check for the Best Team: 
#      - After each game, compare the winning team's score with the current best 
#        team's score. Update the best team if necessary.
#    - Return the Best Team: 
#      - After all competitions, return the team with the highest score.

# 3. updateScores Function:
#    - Check Team in Dictionary: 
#      - If the team is not already in the scores dictionary, add it with an 
#        initial score of 0.
#    - Update Points: 
#      - Add the points to the team's total.

# 4. Main Execution:
#    - Sample Data: 
#      - Define the sample competition data and corresponding results.
#    - Run the Function: 
#      - Call tournamentWinner with the sample data.
#    - Print the Result: 
#      - Output the name of the team with the highest score.
