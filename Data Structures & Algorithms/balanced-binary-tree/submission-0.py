# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        # Base case: if the current node is None,
        # return 0 (height of an empty tree)
        if not root:
            return 0

        # Recursively calculate the
        # height of the left subtree
        left_height = self.dfsHeight(root.left)

        # If the left subtree is unbalanced,
        # propagate the unbalance status
        if left_height == -1:
            return -1

        # Recursively calculate the
        # height of the right subtree
        right_height = self.dfsHeight(root.right)

        # If the right subtree is unbalanced,
        # propagate the unbalance status
        if right_height == -1:
            return -1

        # Check if the difference in height between
        # left and right subtrees is greater than 1
        # If it's greater, the tree is unbalanced,
        # return -1 to propagate the unbalance status
        if abs(left_height - right_height) > 1:
            return -1

        # Return the maximum height of left and
        # right subtrees, adding 1 for the current node
        return max(left_height, right_height) + 1

        