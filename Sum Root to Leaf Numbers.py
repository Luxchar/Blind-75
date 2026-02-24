"""
we need to do a dfs of the tree and keep the last node value and concat the current value
then we add that value to an array that we will sum up
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            path = path * 10 + node.val

            if not node.left and not node.right:
                return path
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)