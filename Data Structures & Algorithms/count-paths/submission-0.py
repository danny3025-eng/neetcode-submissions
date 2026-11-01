class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[c] represents paths to column c
        # in the current row
        dp = [1] * n

        # First row has one path to every cell
        # Process the remaining rows
        for r in range(1, m):

            # First column always has one path
            # Process columns from left to right
            for c in range(1, n):

                # dp[c] = paths from above
                # dp[c - 1] = paths from left
                dp[c] = dp[c] + dp[c - 1]

        # Last column of final row contains the answer
        return dp[-1] 