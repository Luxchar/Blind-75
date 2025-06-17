# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if node is None:
                return
            # Traverse left subtree
            inorder(node.left)
            # Visit root (add to result)
            result.append(node.val)
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return result
        