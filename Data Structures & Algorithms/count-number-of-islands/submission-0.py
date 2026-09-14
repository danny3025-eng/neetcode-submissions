from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    queue = deque([(r, c)])
                    grid[r][c] = "0"

                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"
        return island_count
