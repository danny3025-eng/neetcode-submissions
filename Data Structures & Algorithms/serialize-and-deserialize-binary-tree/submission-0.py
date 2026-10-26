class Codec:
    def serialize(self, root):
        result = []
        self._serialize_dfs(root, result)
        return ",".join(result)

    def _serialize_dfs(self, node, result):
        if node is None:
            result.append("N")
            return
        result.append(str(node.val))
        self._serialize_dfs(node.left, result)
        self._serialize_dfs(node.right, result)

    def deserialize(self, data):
        tokens = data.split(",")
        self.index = 0
        return self._deserialize_dfs(tokens)

    def _deserialize_dfs(self, tokens):
        if self.index >= len(tokens) or tokens[self.index] == "N":
            self.index += 1
            return None
        node = TreeNode(int(tokens[self.index]))
        self.index += 1
        node.left = self._deserialize_dfs(tokens)
        node.right = self._deserialize_dfs(tokens)
        return node