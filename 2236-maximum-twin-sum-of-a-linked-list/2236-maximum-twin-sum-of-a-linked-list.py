# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # go to middle and revers 2nd half of linked list
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        res = slow.next
        slow.next = None
        prev = None

        while res:
            temp = res.next
            res.next = prev
            prev = res
            res = temp

        l, r = head, prev
        res = 0
        while r:
            val = l.val + r.val
            res = max(res, val)
            l = l.next
            r = r.next
            
        return res

        