class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Build adjacency list for all characters
        adj = {c: set() for word in words for c in word}

        # Compare adjacent words to extract ordering rules
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        # DFS topological sort with cycle detection
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = {c: 0 for c in adj}
        result = []

        def dfs(c):
            state[c] = 1  # Mark as visiting
            for neighbor in adj[c]:
                if state[neighbor] == 1:  # Cycle detected
                    return False
                if state[neighbor] == 0:
                    if not dfs(neighbor):
                        return False
            state[c] = 2  # Mark as visited
            result.append(c)  # Add in reverse post-order
            return True

        for c in adj:
            if state[c] == 0:
                if not dfs(c):
                    return ""

        return "".join(reversed(result))