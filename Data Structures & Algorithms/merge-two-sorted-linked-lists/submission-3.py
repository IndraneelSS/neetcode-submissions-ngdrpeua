# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)  # Dummy node to start the merged list
        output_pointer = dummy

        l1_pointer = list1
        l2_pointer = list2

        while l1_pointer is not None and l2_pointer is not None:
            if l1_pointer.val < l2_pointer.val:
                output_pointer.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                output_pointer.next = l2_pointer
                l2_pointer = l2_pointer.next

            output_pointer = output_pointer.next

        # If any remaining nodes are left in either list, attach them
        if l1_pointer is not None:
            output_pointer.next = l1_pointer
        if l2_pointer is not None:
            output_pointer.next = l2_pointer

        return dummy.next  # Return the merged list, starting from the node after dummy




        