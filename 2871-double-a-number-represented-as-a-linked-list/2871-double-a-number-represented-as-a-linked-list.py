# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cur = head
        while cur:
            num = num * 10 + cur.val
            cur = cur.next

        num = num * 2
        if num == 0:
            return ListNode(0)
        
        dummy = ListNode()
        prev = dummy
        while num > 0:
            r = num % 10
            num = num // 10
            node = ListNode(r)
            prev.next = node
            prev = prev. next

        rev = None
        slow = dummy.next
        while slow:
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp

        return rev
            

        