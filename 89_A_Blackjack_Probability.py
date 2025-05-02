# Problem: Blackjack Probability Calculation
# -------------------------------------------
# You are given a target score and a starting hand (list of integers).
# The goal is to determine how many different combinations of cards (1 through 10)
# can be drawn such that their total sum reaches exactly the given target score.
# This simulates the process of trying to reach 21 (or any other number) in Blackjack,
# where each drawn card adds a number from 1 to 10 to the hand.

# For example, if the current hand is [5, 3] and the target is 21,
# the remaining target is 13. The function must find all possible ways
# to reach 13 using any number of card draws, where each card is in the range 1-10.

# Code Execution Theory:
# ----------------------
# 1. We use recursion to simulate trying every card from 1 to 10.
# 2. The recursion continues reducing the target until it reaches 0 (successful combination)
#    or goes negative (invalid path).
# 3. We use memoization (a dictionary) to avoid recalculating probabilities for the same hand.
#    The memo key is a tuple of the current hand to ensure immutability and hashability.
# 4. The result is the total number of valid paths that reach the target sum.


def blackjackProbability(target, startingHand):
    # Dictionary to memoize already calculated results for optimization
    memo = {}

    # Calculate the remaining target by subtracting the sum of the current hand
    remaining = target - sum(startingHand)

    # Call the recursive helper function with remaining target and current hand
    return calculateProbability(remaining, startingHand, memo)


def calculateProbability(target, hand, memo):
    # Base Case 1: If the target becomes negative, this path is invalid
    if target < 0:
        return 0

    # Base Case 2: If the target is exactly 0, this is a valid combination
    if target == 0:
        return 1

    # Use memoization to return cached result if available
    if tuple(hand) in memo:
        return memo[tuple(hand)]

    total = 0  # Initialize total combinations for current path

    # Try adding each possible card value (1 to 10)
    for card in range(1, 11):
        # Recursively try adding each card to the hand and reducing the target
        total += calculateProbability(target - card, hand + [card], memo)

    # Store the result in memo to avoid re-computation
    memo[tuple(hand)] = total

    # Return total valid combinations found for this hand
    return total


# ✅ Dummy Data to test the function
target_score = 21
starting_hand = [5, 3]  # Initial hand with sum 8; need to find ways to reach 13 more

# Call the function and print the result
result = blackjackProbability(target_score, starting_hand)
print(f"Number of ways to reach {target_score} from starting hand {starting_hand}: {result}")
