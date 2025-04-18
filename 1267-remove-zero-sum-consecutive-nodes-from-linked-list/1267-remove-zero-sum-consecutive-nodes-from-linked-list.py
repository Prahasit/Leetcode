# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        start = dummy
        while start:
            end = start.next
            cur_sum = 0
            while end:
                cur_sum += end.val
                if cur_sum == 0:
                    start.next = end.next
                
                end = end.next
            
            start = start.next

        return dummy.next
        