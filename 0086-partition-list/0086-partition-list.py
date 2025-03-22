# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        less = dummy1
        
        dummy2 = ListNode()
        more = dummy2

        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
                cur = cur.next
            else:
                more.next = cur
                more = more.next
                cur = cur.next
        
        more.next = None
        less.next = dummy2.next
        return dummy1.next