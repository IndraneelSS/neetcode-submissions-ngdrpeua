# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to handle edge cases (e.g., removing the first node)
        dummy.next = head
        slow = dummy
        fast = dummy
        prev = dummy

        # Move fast pointer `n` steps ahead
        for _ in range(n):
            if fast is not None:
                fast = fast.next

        # Move both fast and slow pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            prev = slow
            slow = slow.next

        # Remove the nth node from the end
        prev.next = slow.next
        slow.next = None  # Optional step to help with garbage collection

        return dummy.next  # Return the updated list head
   





        