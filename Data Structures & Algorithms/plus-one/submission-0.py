class Solution:
    # Define the method taking a list of integers and returning a list of integers
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the total number of digits in the list
        n = len(digits)
        
        # Loop backward through the list from the last index (n - 1) down to 0
        for i in range(n - 1, -1, -1):
            # Check if the current digit is less than 9 (no carry-over needed)
            if digits[i] < 9:
                # Add 1 to the current digit
                digits[i] += 1
                # Return the updated list immediately since we are done
                return digits
            
            # If the digit was 9, it rolls over to 0 and the loop continues to carry the 1 left
            digits[i] = 0
            
        # If the loop finishes, every digit was a 9 (e.g., [9, 9] became [0, 0]); prepend 1
        return [1] + digits
