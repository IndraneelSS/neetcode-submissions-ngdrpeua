# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            left_check = sameTree(p.left, q.left)
            right_check = sameTree(p.right, q.right)
            if left_check and right_check:
                return True
            else:
                return False

        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        else:
            left_result = self.isSubtree(root.left, subRoot)
            right_result = self.isSubtree(root.right, subRoot)
            if left_result or right_result:
                return True
            else:
                return False
    



        