# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        total_calls = 0
        if root is None:
            return 0


        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right) 
        total_calls = 1+ max(left,right)
        return total_calls    
        