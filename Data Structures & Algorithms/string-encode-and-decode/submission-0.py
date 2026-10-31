class Solution:

    def encode(self, strs: list[str]) -> str:
        # Initialize an empty string to store the combined, encoded output
        res = ""

        # Loop through each individual string in the input list
        for s in strs:
            # Append the length of the string, a delimiter "#", and the string itself
            # Example: "hello" becomes "5#hello"
            res += str(len(s)) + "#" + s

        # Return the final fully encoded string
        return res

    def decode(self, s: str) -> list[str]:
        # Initialize an empty list to store the recovered original strings
        res = []

        # Pointer 'i' tracks our current position in the encoded string
        i = 0

        # Process the entire encoded string until the pointer reaches the end
        while i < len(s):

            # Create a secondary pointer 'j' to find where the length prefix ends
            j = i

            # Move 'j' forward until it hits the delimiter "#"
            while s[j] != "#":
                j += 1

            # Slice the string from 'i' to 'j' to grab the length digits, then convert to an integer
            # Example: If s[i:j] is "5", length becomes 5
            length = int(s[i:j])

            # Slice the actual string content which starts right after "#" (at j + 1)
            # and spans for the duration of 'length'
            res.append(s[j + 1 : j + 1 + length])

            # Jump the main pointer 'i' past the processed string to the start of the next length prefix
            i = j + 1 + length

        # Return the list of completely decoded original strings
        return res