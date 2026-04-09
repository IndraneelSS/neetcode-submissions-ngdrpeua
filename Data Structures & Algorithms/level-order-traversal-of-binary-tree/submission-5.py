# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# It is also called as Breadth First Search
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        q = deque([root])    
        
        res = []

        while q:
            level_order_items = []

            for i in range(len(q)): #this keeps the bound check for number
            # of nodes in each level 
                 node = q.popleft()
                 level_order_items.append(node.val)

                 if node.left:
                    q.append(node.left)

                 if node.right:
                    q.append(node.right)
            res.append(level_order_items)     

        return res       





        