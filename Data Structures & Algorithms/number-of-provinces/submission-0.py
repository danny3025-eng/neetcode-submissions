class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True
            for j in range(n):
                # Visit unvisited neighbors (skip self-loop)
                if isConnected[city][j] == 1 and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                # Found an unvisited city, explore its entire province
                dfs(i)
                provinces += 1

        return provinces