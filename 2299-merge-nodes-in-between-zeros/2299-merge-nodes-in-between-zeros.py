# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy
        cur = head.next

        temp = 0
        while cur:
            if cur.val != 0:
                temp += cur.val
                
            else:
                prev.next = ListNode(temp)
                prev = prev.next
                temp = 0
            
            cur = cur.next

        return dummy.next