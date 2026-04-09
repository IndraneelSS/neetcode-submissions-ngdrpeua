# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor (LCA) of two nodes in a BST.
        
        Args:
            root: Root node of the BST
            p: First node to find LCA for
            q: Second node to find LCA for
            
        Returns:
            TreeNode: The lowest common ancestor node
        """
        if root is None:
            return None
        
        # If both nodes are greater than current, LCA is in right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both nodes are less than current, LCA is in left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Current node is LCA (either:
        # 1. p and q are on different sides, or
        # 2. current node is p or q)
        return root    
            




        