# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(curr: TreeNode, max_value: int) -> int:
            if curr is None:
                return 0

            # Check if the current node is a "good" node
            good_count = 1 if curr.val >= max_value else 0

            # Update the maximum value seen so far
            max_value = max(max_value, curr.val)

            # Count good nodes in the left and right subtrees
            good_count += count_good_nodes(curr.left, max_value)
            good_count += count_good_nodes(curr.right, max_value)

            return good_count  # Return the count for this subtree

        # Start the recursion with the root node and its value as the max value
        return count_good_nodes(root, root.val)

        







        