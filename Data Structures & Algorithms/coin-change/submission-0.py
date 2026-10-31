class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Infinity represents an amount we cannot make yet
        INF = float('inf')

        # dp[a] = minimum coins needed for amount a
        dp = [INF] * (amount + 1)

        # Zero coins are needed to make amount 0
        dp[0] = 0

        # Calculate answers for amounts 1 through target
        for a in range(1, amount + 1):

            # Try every available coin
            for coin in coins:

                # Coin can be used only if it fits the amount
                if a >= coin:

                    # dp[a - coin] is the answer for remaining amount
                    # Add 1 because we are using this coin
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If target remains infinity, no combination exists
        if dp[amount] == INF:
            return -1

        # Otherwise return minimum number of coins
        return dp[amount]

        