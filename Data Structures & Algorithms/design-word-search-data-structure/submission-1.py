class TrieNode:
    def __init__(self):  # Initialize a new node for the prefix tree
        self.children = {}  # Dictionary to store child characters mapping to new TrieNode instances
        self.is_end = False  # Boolean flag to mark if this node represents the end of a valid word


class WordDictionary:
    def __init__(self):  # Initialize the dictionary containing the root of the Trie
        self.root = TrieNode()  # Create an empty root TrieNode

    def addWord(self, word: str) -> None:  # Insert a word character by character into the Trie
        current = self.root  # Start traversing from the root node
        for char in word:  # Loop through every character in the input word
            if char not in current.children:  # Check if the character path does not exist yet
                current.children[char] = (
                    TrieNode()
                )  # Create a new TrieNode for this character
            current = current.children[char]  # Move down to the child node
        current.is_end = True  # Mark the final node as the end of a complete word

    def search(self, word: str) -> bool:  # Search for a word or wildcard pattern
        return self._dfs(
            self.root, word, 0
        )  # Start depth-first search from root at index 0

    def _dfs(
        self, node: TrieNode, word: str, index: int
    ) -> bool:  # Recursive helper for searching with wildcards (.)
        if index == len(word):  # Base case: if we have processed all characters in the word
            return (
                node.is_end
            )  # Return True only if the current node marks the end of a valid word

        char = word[index]  # Grab the character at the current string index
        if char == ".":  # Wildcard character found (matches any single letter)
            # Wildcard: try every existing child
            for (
                child
            ) in (
                node.children.values()
            ):  # Loop through all possible child nodes at this level
                if self._dfs(
                    child, word, index + 1
                ):  # Recursively search the next character
                    return True  # If any branch matches, return True
            return False  # If no child branches match the rest of the pattern, return False
        else:  # Regular character matching
            # Regular character: follow the specific child
            if char not in node.children:  # If the required character path does not exist
                return False  # Word or pattern cannot be found
            return self._dfs(
                node.children[char], word, index + 1
            )  # Continue searching down the matching child path
