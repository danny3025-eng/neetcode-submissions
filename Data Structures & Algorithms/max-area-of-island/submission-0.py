class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) 

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1: # checking if we are inbound in grid and not going up or down high too much
                return 0
            else:
                grid[i][j] = 0
            # recursive 
                return 1 + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j) + dfs(i, j+1)
        
        max_area = 0
        for i in range(m):
            for j in range(n): # this for loops are kind of going to allow us to itrate through entire grid top to bottom, left to right
                if grid[i][j] == 1: # becuase we only care about the land picese which is at "1"
                    max_area = max(max_area, dfs(i,j))

        return max_area


        