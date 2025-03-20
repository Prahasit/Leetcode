# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        slow = head
        fast = head
        while n > 0 and fast.next:
            fast = fast.next
            n -= 1
        if n > 0: # if n > len(list)
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        del_node = slow.next
        slow.next = slow.next.next
        del_node = None
    
        return head

        