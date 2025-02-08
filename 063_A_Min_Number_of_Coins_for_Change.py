# Problem Statement:
# Given an integer `n` representing a target amount of money, and a list `denoms` representing
# the available denominations of coins, write a function that determines the minimum number
# of coins required to make up exactly `n` units. If it's not possible to make the target
# amount with the available denominations, return -1.

# Execution Theory:
# 1. We initialize a list, `numOfCoins`, where each index represents the minimum number of coins
#    required to reach that amount. Initially, all values are set to infinity (`float("inf")`)
#    to represent unachievable amounts.
# 2. We set `numOfCoins[0] = 0` as 0 coins are needed to make an amount of 0.
# 3. For each denomination, we iterate through `numOfCoins` starting from the value of the denomination.
# 4. For each amount that can be achieved by adding the current denomination, we update the
#    minimum number of coins required to reach that amount.
# 5. If the final amount `n` has not changed from infinity, we return -1 as it is not achievable
#    with the available denominations; otherwise, we return `numOfCoins[n]`.


# Function to calculate minimum number of coins for change
def minNumberOfCoinsForChange(n, denoms):
    # Initialize an array to store minimum coins required for each amount
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0  # Base case: no coins needed for amount 0

    # Loop through each denomination
    for denom in denoms:
        # Loop through each amount from the denomination value up to n
        for amount in range(denom, n + 1):
            # Update minimum coins if the current denomination can be used
            numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)

    # Return result for amount n, or -1 if not achievable
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


# Dummy data
n = 7  # Target amount
denoms = [1, 5, 10]  # Available denominations

# Calling the function with dummy data
print(minNumberOfCoinsForChange(n, denoms))  # Expected output: 3 (as 7 = 5 + 1 + 1)


# Reasoning for Solving the Minimum Coins for Change Problem Using Dynamic Programming:

# 1. Optimal Substructure:
#    The problem can be divided into smaller subproblems: if we know the minimum coins needed to
#    reach all amounts less than `n`, we can use this information to calculate the minimum coins
#    required for `n`. By checking if adding a denomination results in fewer coins for a target
#    amount, we can iteratively build an optimal solution.

# 2. Avoiding Repeated Work (Memoization):
#    Using the `numOfCoins` array, we memoize the minimum number of coins required to reach each
#    amount up to `n`. This prevents recalculating solutions for amounts we've already solved,
#    reducing the overall computational effort and improving efficiency.

# 3. Efficiency:
#    Without Dynamic Programming, a recursive approach would involve branching out and recalculating
#    solutions for the same amounts repeatedly, resulting in exponential time complexity. The DP
#    approach, by contrast, has a time complexity of O(n * d), where `n` is the target amount and `d`
#    is the number of denominations, making it far more efficient.

# 4. Bottom-Up Approach:
#    This solution uses a bottom-up approach: starting with the smallest amount (0) and incrementally
#    building up to `n`. By solving each smaller amount optimally before moving to larger amounts,
#    we ensure that when we reach `n`, we have already calculated the minimum coins required for
#    all previous amounts, resulting in an optimal solution for the target amount.



# Problem Explanation:
# Suppose you have a target amount of money, `n`, that you want to make up using a limited set of coin
# denominations (for example, coins worth 1, 5, and 10 units). The goal is to determine the smallest 
# number of coins required to reach exactly the target amount, `n`.

# Example:
# If `n = 7` and the denominations are `[1, 5, 10]`:
# - You could make 7 using seven 1-unit coins, but that's inefficient.
# - A better solution would be to use one 5-unit coin and two 1-unit coins, totaling only 3 coins.
# So, the function should return `3` since that's the minimum number of coins needed to make 7.

# Special Case:
# If it's impossible to make up the target amount with the given denominations (e.g., if `n = 3` and
# denominations are `[2, 4]`, where no combination of 2 and 4 adds up to 3), then the function
# should return `-1` to indicate that reaching `n` is not achievable.

# The Dynamic Programming approach used in this solution helps us efficiently find the minimum
# number of coins required by building up solutions for smaller amounts and using them to solve 
# for larger amounts.
