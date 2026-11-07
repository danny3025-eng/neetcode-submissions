class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []   # Stores all valid palindrome partitioning combinations
        part = []  # Acts as a temporary list/stack to hold the current partition path

        # Helper function to check if a substring from index 'l' to 'r' is a palindrome
        def ispali(s, l, r): 
            # Use a two-pointer approach, moving inward from the boundaries
            while l < r: 
                # If characters at opposite ends don't match, it's not a palindrome
                if s[l] != s[r]: 
                    return False 
                # Move pointers closer together
                l, r = l + 1, r - 1 
            return True # All characters matched, meaning it is a palindrome 

        def dfs(i): 
            # Base case: if the index 'i' reaches or exceeds the length of the string,
            # it means we have successfully partitioned the entire string.
            if i >= len(s): 
                # We append a copy of the current path 'part' to the final results 
                # because 'part' is modified globally and would otherwise be empty at the end.
                res.append(part.copy()) 
                return 
        
            # Loop through all possible ending positions 'j' for the substring starting at index 'i'
            for j in range(i, len(s)):
                # Check if the substring from index 'i' to 'j' (inclusive) is a palindrome
                if ispali(s, i, j): 
                    # If it's a palindrome, include this substring in our current partition path
                    part.append(s[i:j+1]) 
                
                    # Recursively move to the next index (j + 1) to partition the remaining string
                    dfs(j + 1) 
                
                    # Backtrack: remove the last added substring to explore other partitioning choices
                    part.pop() 
                
        dfs(0) # Start the depth-first search from the very beginning of the string (index 0)
        return res # Return the final list containing all unique palindrome partitions
