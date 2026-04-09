# Trees are nearly similiar to Linked list
# but the trees have left an dright node 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # root = True , if not True;, which means false the itereturn None
           return None

        temp = root.left 
        root.left = root.right 
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 


         