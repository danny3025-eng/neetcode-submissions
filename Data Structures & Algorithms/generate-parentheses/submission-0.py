class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] # resulting array to append all our combinations initialize it to 0

        def genrate(o, c, curr): # genrating function to have a open and close and current values
            if o == c == 0: # base case 
                result.append(curr)
                return 
            if o > 0: # recursive case
                genrate(o-1, c, curr + "(") # o-1 adding new open parentheses to curr string
            if o < c:
                genrate(o, c-1, curr + ")") # c-1 adding new close parentheses to curr string
        genrate(n, n, "") # n--> open, n --> close, ""--> curr string
        return result