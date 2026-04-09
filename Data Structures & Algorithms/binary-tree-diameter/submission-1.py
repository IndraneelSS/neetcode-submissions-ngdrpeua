# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#diameter of the binary tree depends on 
#self.max_diameter = max(self.max_diameter, left_height + right_height)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # A list to store the maximum diameter found
        self.max_diameter = 0

        def calculate_height(node):
            if node is None:
                return 0

            # Recursively calculate the height of left and right subtrees
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)

            # Update the maximum diameter by considering the path through this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return the height of the subtree rooted at this node
            return 1 + max(left_height, right_height)

        # Initialize the recursion
        calculate_height(root)

        # The maximum diameter is stored in self.max_diameter
        return self.max_diameter   


        