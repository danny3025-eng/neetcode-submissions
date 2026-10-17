class Solution:
    def __init__(self):
        self.clones = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # If already cloned, return the clone (handles cycles)
        if node in self.clones:
            return self.clones[node]

        # Create clone and add to map before recursing
        clone = Node(node.val)
        self.clones[node] = clone

        # Recursively clone all neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))

        return clone

        