class Solution:

    def foreignDictionary(self, words: list[str]) -> str:
        # Build adjacency list for all characters
        # Create a dictionary where every unique character across all words is a key mapped to an empty set to track its outgoing edges (dependencies).
        adj = {c: set() for word in words for c in word}

        # Compare adjacent words to extract ordering rules
        # Loop through the list of words up to the second-to-last word to compare each word with the one immediately following it.
        for i in range(len(words) - 1):
            # Assign the current word to 'word1' and the next word to 'word2' for step-by-step comparison.
            word1, word2 = words[i], words[i + 1]
            # Check for an invalid prefix case: if 'word1' is longer than 'word2' but starts with 'word2' (e.g., "abc" before "ab"), it violates lexicographical order, so return an empty string.
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            # Iterate through the characters of both words up to the length of the shorter word to find the first differing character.
            for j in range(min(len(word1), len(word2))):
                # Identify the first position where the characters in the two words do not match.
                if word1[j] != word2[j]:
                    # Add a directed edge from the character in 'word1' to the character in 'word2', establishing that word1[j] comes before word2[j].
                    adj[word1[j]].add(word2[j])
                    # Stop comparing the current pair of words immediately after finding the first mismatch, as subsequent characters do not determine their relative order.
                    break

        # DFS topological sort with cycle detection
        # 0 = unvisited, 1 = visiting, 2 = visited
        # Initialize a dictionary tracking the visit state of each unique character, setting all of them to 0 (unvisited) initially.
        state = {c: 0 for c in adj}
        # Initialize an empty list to store the ordered characters in reverse post-order during the depth-first search.
        result = []

        # Define a helper function to perform Depth-First Search (DFS) for topological sorting and cycle detection.
        def dfs(c):
            # Mark the current character 'c' as 1 (visiting) to indicate it is on the current recursion path.
            state[c] = 1  # Mark as visiting
            # Iterate through all the characters that must come after the current character 'c'.
            for neighbor in adj[c]:
                # If a neighbor is already marked as 1 (visiting), a cycle (contradiction in character rules) exists.
                if state[neighbor] == 1:  # Cycle detected
                    # Return False to flag that a valid topological sort is impossible due to the detected cycle.
                    return False
                # If the neighbor hasn't been visited yet (state 0), recursively run DFS on it.
                if state[neighbor] == 0:
                    # If any recursive DFS call detects a cycle and returns False, propagate False upwards.
                    if not dfs(neighbor):
                        return False
            # Mark the current character 'c' as 2 (visited) once all its neighbors/dependencies have been completely processed.
            state[c] = 2  # Mark as visited
            # Append the character to the result list since all its dependencies are resolved.
            result.append(c)  # Add in reverse post-order
            # Return True to signal that this branch of the graph was successfully sorted without any cycles.
            return True

        # Loop through every unique character in the graph to ensure all disconnected components are visited.
        for c in adj:
            # Check if the character has not been visited yet.
            if state[c] == 0:
                # Run the DFS starting from this unvisited character, and if it detects a cycle (returns False), return an empty string.
                if not dfs(c):
                    return ""

        # Reverse the completed result list and join it into a final string to output the correct topological order.
        return "".join(reversed(result))
