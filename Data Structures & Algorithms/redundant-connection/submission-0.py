class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            # Check if u and v are already connected
            if self.is_connected(graph, u, v, n):
                return [u, v]
            # Add edge to graph
            graph[u].append(v)
            graph[v].append(u)

        return []

    def is_connected(self, graph, src, dst, n):
        visited = [False] * (n + 1)
        stack = [src]
        visited[src] = True

        while stack:
            node = stack.pop()
            if node == dst:
                return True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return False
        