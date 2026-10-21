class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False

                if pairs[stack[-1]] != char:
                    return False

                stack.pop()

        return len(stack) == 0
