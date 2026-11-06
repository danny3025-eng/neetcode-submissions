class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        # If the input string of digits is empty, immediately return an empty list.
        if digits == "": 
            return [] 

        # Define a dictionary mapping each phone digit string to its corresponding letters.
        d = { 
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' 
        } 

        # Initialize the list with an empty string so the inner loops have a starting point to build upon.
        combinations = [""] 

        # Loop through each individual digit in the input 'digits' string one by one.
        for digit in digits: 
            # Create a temporary empty list to hold the new combinations generated for the current digit.
            new_comb = [] 
        
            # Loop through all the partial letter combinations built up so far.
            for combo in combinations: 
                # Loop through each possible letter that corresponds to the current digit.
                for letter in d[digit]: 
                    # Append the existing partial combination combined with the new letter to the temporary list.
                    new_comb.append(combo+letter) 
                
            # Update the main combinations list with the newly expanded combinations, preparing for the next digit.
            combinations = new_comb 

        # Return the final list containing all possible letter combinations.
        return combinations