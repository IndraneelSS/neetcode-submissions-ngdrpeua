# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])

# when focussing on the root node, q.popleft 
# contains a root value which is stored in the node 
# so , now node has 3 components -  value , left , right  
# when ever we are working on tree , we need to focus on this 
# 3 concepts       
        res = []
        while q:
            level_order_items = []

            for i in range(len(q)):
                node = q.popleft()
                level_order_items.append(node.val)





                if node.left:

                    q.append(node.left)

                if node.right:

                     q.append(node.right)

            res.append(level_order_items)  
        return res              



        