# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 
        stack = []
        curr = root 

        while curr or stack:  # Corrected the condition here
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1 
            if n == k:
                return curr.val 
            curr = curr.right

        return -1  # Return -1 if k is not valid (not found)   

        