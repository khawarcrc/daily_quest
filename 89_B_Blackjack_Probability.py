# -------------------------------
#  Problem Statement and Explanation:
# -------------------------------
# Given a target score in a simplified Blackjack game and a player's current hand score,
# calculate the probability of the player *busting* (going over the target score)
# if they continue to draw cards optimally.

# Rules:
# - Player draws from cards numbered 1 to 10.
# - Each card has an equal probability of 0.1 (10%).
# - If current hand > target → the player has already busted → return probability = 1.
# - If currentHand + 4 >= target, there's a safe zone with low bust risk → return probability = 0.
# - Use memoization to avoid recalculating the same hand values (Dynamic Programming).
# - We simulate the drawing process recursively and average the probabilities of busting
#   for all possible next card draws.

# -------------------------------
#  Code Execution Theory:
# -------------------------------
# - The main function `blackjackProbability` calls the helper `calculateProbability`.
# - `calculateProbability` checks base cases:
#   → If already calculated, use memo.
#   → If hand > target, it's a bust (return 1).
#   → If hand is close to target (within 4 points), assume player stops drawing (safe zone).
# - Otherwise, recursively simulate drawing each card (1 to 10) and average the bust probability.
# - Store and return the memoized result for efficiency.
# -------------------------------


# Main function to calculate the probability of busting in Blackjack
def blackjackProbability(target, startingHand):
    memo = {}  # Dictionary to memoize previously computed probabilities
    return round(calculateProbability(startingHand, target, memo), 3)  # Call the recursive function and round result


# Recursive function to calculate probability of busting
def calculateProbability(currentHand, target, memo):
    if currentHand in memo:  # If already calculated, return stored result
        return memo[currentHand]

    if currentHand > target:  # If current hand exceeds the target, it's a bust
        return 1

    if currentHand + 4 >= target:
        # If drawing the highest card (10) won't exceed the target by more than 4,
        # assume player won't draw more → very low risk of bust → return 0
        return 0

    totalProbability = 0  # Initialize total probability

    for drawCard in range(1, 11):  # Loop through cards 1 to 10
        # Add probability of busting after drawing this card
        totalProbability += 0.1 * calculateProbability(
            currentHand + drawCard, target, memo
        )

    memo[currentHand] = totalProbability  # Store computed result for this hand
    return totalProbability  # Return the average bust probability


# -------------------------------
#  Dummy Test Case
# -------------------------------
# Let's say:
# - Target score is 21 (as in regular Blackjack)
# - Current hand is 15
# We want to know the probability of busting if the player keeps drawing optimally.

print(blackjackProbability(21, 15))  # Output: probability of busting from hand 15 toward 21
