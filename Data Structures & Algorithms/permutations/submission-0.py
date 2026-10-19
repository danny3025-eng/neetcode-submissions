from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack():
            # Base case: if our current solution has all numbers
            if len(sol) == n:
                res.append(sol[:]) # Append a copy of sol
                return 
            
            for i in nums:
                if i not in sol:      # Check if number is already in current path
                    sol.append(i)     # Choose
                    backtrack()       # Explore
                    sol.pop()         # Unchoose (backtrack)

        backtrack()
        return res
