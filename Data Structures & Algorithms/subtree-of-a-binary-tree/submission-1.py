# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
        def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            
            
            def preOrderTraversal(node: Optional[TreeNode]) -> str:
                if node is None:
                    return "null"
            
            # Use "^" as a separator for each node's value
                return f"^{node.val}" + preOrderTraversal(node.left) + preOrderTraversal(node.right)

        # Generate the pre-order traversal strings for both trees
            fullTree = preOrderTraversal(root)
            subTree = preOrderTraversal(subRoot)

        # Check if the serialized subtree string is in the full tree string
            return subTree in fullTree
        
        