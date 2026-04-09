# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr  = dummy 
        carry = 0 
        while (l1!=None or l2!= None) or carry:
            sum_ = 0
            if l1 != None:
                sum_ = l1.val + sum_
                l1 = l1.next

            if l2!= None:
                sum_ = sum_ + l2.val
                l2 = l2.next

            sum_ = sum_ + carry 
            carry = sum_ // 10
            node = ListNode(sum_ % 10)
            curr.next = node
            curr = curr.next 

        return dummy.next     




        