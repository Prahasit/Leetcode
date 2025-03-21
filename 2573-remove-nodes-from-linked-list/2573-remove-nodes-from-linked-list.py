# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse it and using max elemnt remove less than the max values come
        #again reverse the list to return
        def reverse(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        temp = reverse(head)
        prev = temp
        res = prev.val
        while prev.next:
            
            if prev.next.val  <  res:
                prev.next = prev.next.next
            else:
                res = prev.next.val
                prev = prev.next
                
        answer = reverse(temp)
        return answer

