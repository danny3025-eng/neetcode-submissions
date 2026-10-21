class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the target number of stairs to climb (in this case, 2 steps) 
        ways = [1, 1, 2]  

        for step in range(3, n + 1): 
        # Calculate ways for current step by adding the previous two steps, then add it to the list
            ways.append(ways[step - 1] + ways[step - 2])  
        
        # Look up and return the total number of unique ways stored at index 'n' of the list
        return ways[n]  