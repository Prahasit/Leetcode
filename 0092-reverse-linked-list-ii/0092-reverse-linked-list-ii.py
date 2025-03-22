# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        leftprev = dummy

        while left - 1 > 0:
            cur = cur.next
            leftprev = leftprev.next
            left -= 1
            right -= 1
        prev = None
        for _ in range(right):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        #over hear leftprev is at 1
        # prev is at 4
        #cur is at 5
        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next
            