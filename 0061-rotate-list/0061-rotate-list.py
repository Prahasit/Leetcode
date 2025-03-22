# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #use slow and fast pointers
        #first move fast pointer by k times
        #then move slow and fast pointersuntil fast reaches end
        #now end of fast becomes the head and end of slow of next is None

        if head is None:
            return 
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        

        k = k % count
        
        
        slow = head
        fast = head
        while k > 0:
            fast = fast.next
            k -= 1
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        new_head = slow.next
        slow.next = None

        return new_head