# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        prev = dummy
        curr = head
        count = 0
        
        # Move curr n nodes ahead
        while count < n and curr is not None:
            curr = curr.next
            count += 1
        
        # Move both pointers until curr reaches end
        while curr is not None:
            prev = prev.next
            curr = curr.next
        
        # Remove the nth node from end
        prev.next = prev.next.next
        
        return dummy.next  # Return the actual head (not dummy)         





        