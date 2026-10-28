class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # Build Trie using nested dictionaries
    root = {}
    for word in words:
      node = root
      for ch in word:
        if ch not in node:
          node[ch] = {}
        node = node[ch]
      node['#'] = word  # mark end of word  <-- Stores the complete word string at the last character's node in the Trie

    m, n = len(board), len(board[0])  #<-- Get the number of rows (m) and columns (n) in the board
    result = []  #<-- Initialize a list to store all found words

    def dfs(r, c, parent):
      ch = board[r][c]  #<-- Get the character at the current board position (r, c)
      node = parent[ch]  #<-- Move down to the corresponding child node in the Trie

      # Found a complete word
      if '#' in node:  #<-- Check if the special marker '#' exists, meaning a valid word ends here
        result.append(node['#'])  #<-- Add the found word to the result list
        del node['#']  # avoid duplicates  <-- Remove the marker so the same word is not added again

      board[r][c] = '!'  # mark visited  <-- Temporarily change the cell to '!' to prevent reusing the same letter in a single path

      # Explore all 4 adjacent directions (down, up, right, left)
      for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc  #<-- Calculate the coordinates of the neighbor cell
        # Check if the neighbor is inside the board and its character exists in the current Trie node
        if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
          dfs(nr, nc, node)  #<-- Recursively call DFS for the neighbor cell and advance the Trie node

      board[r][c] = ch  # backtrack  <-- Restore the original character on the board after exploring all paths

      # Prune empty branches
      if not node:  #<-- If the current Trie node has no children left after search
        del parent[ch]  #<-- Delete this branch from the parent dictionary to speed up future searches

    # Iterate through every cell on the board as a starting point for DFS
    for r in range(m):
      for c in range(n):
        if board[r][c] in root:  #<-- Only start DFS if the cell's character is a starting letter in our Trie
          dfs(r, c, root)  #<-- Begin depth-first search from this cell

    return result  #<-- Return the list of all found words
