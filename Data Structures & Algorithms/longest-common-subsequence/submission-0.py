class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

  # Get the length of the first string (text1) and store it in variable 'm'
        m = len(text1)

  # Get the length of the second string (text2) and store it in variable 'n'
        n = len(text2)

  # Create a 2D list (table) of size (m+1) x (n+1) filled with zeros to store subproblem results
        dp = [[0] * (n + 1) for _ in range(m + 1)]

  # Loop through each character position 'i' in the first string (from 1 to m)
        for i in range(1, m + 1):
    # Loop through each character position 'j' in the second string (from 1 to n)
            for j in range(1, n + 1):
      # Check if the current character in text1 matches the current character in text2
                if text1[i - 1] == text2[j - 1]:
        # Add 1 to the length from the diagonal cell (previous subproblem where both chars matched)
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
        # Characters do not match; take the maximum value from either the cell above or the cell to the left
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  # Return the bottom-right value in the table, which holds the length of the longest common subsequence
        return dp[m][n]


# # Call the function with test strings "abcde" and "ace", then print the result (Output: 3)
# print(longestCommonSubsequence("abcde", "ace"))