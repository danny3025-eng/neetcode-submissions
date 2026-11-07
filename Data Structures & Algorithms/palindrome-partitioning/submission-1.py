from typing import List

class Solution:
    # Defines the main function that takes a string 's' and returns all possible palindrome partitions
    def partition(self, s: str) -> List[List[str]]:
        # Initializes an empty list to store all the valid palindrome combinations found
        result = []
        
        # Starts the recursive backtracking helper function from index 0 with an empty current path
        self._backtrack(s, 0, [], result)
        
        # Returns the final list containing all the valid palindrome partition lists
        return result

    # The backtracking helper function that explores all possible splitting choices
    def _backtrack(self, s, start, current, result):
        # Base case: checks if the 'start' pointer has reached the end of the string
        if start == len(s):
            # Appends a copy of the 'current' valid partition path to the final result list
            result.append(current[:])
            # Returns to exit the current recursive call level
            return
            
        # Iterates through all possible end positions for the current substring slice
        for end in range(start, len(s)):
            # Checks if the current substring slice from 'start' to 'end' is a palindrome
            if self._is_palindrome(s, start, end):
                # If valid, adds the substring slice (inclusive of 'end') to the current path list
                current.append(s[start:end + 1])
                
                # Recursively calls backtrack to process the remaining string starting after 'end'
                self._backtrack(s, end + 1, current, result)
                
                # Backtracks by removing the last added substring to try other splitting options
                current.pop()

    # Helper function that verifies if a specific substring window is a palindrome
    def _is_palindrome(self, s, left, right):
        # Continues checking characters moving inward until the pointers meet or cross
        while left < right:
            # If the characters at the left and right pointers mismatch, it is not a palindrome
            if s[left] != s[right]:
                # Returns False immediately to reject this substring slice
                return False
            # Moves the left pointer one step to the right
            left += 1
            # Moves the right pointer one step to the left
            right -= 1
        # Returns True if all characters matched symmetrically
        return True