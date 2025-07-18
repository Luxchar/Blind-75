"""
make function that will go through the tree recursively and count +1 for each node going down
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     return max(left, right) + 1
        # return dfs(root)

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))