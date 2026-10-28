# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # Base case: found p, q, or empty node
        if not root or root == p or root == q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(
            root.left, p, q
        )

        # Search right subtree
        right = self.lowestCommonAncestor(
            root.right, p, q
        )

        # Both sides found targets
        if left and right:
            return root

        # Return whichever side found a target
        return left or right
