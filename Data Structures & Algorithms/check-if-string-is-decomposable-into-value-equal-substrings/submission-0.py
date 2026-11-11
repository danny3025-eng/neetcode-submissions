class Solution:
    def isDecomposable(self, s: str) -> bool:
        pairs = 0
        i = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            reminder = (j-i)%3
            if reminder == 1:
                return False
            if reminder == 2:
                pairs += 1
            i = j
        return pairs == 1
