# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # go to mid reverse the 2nd half
        # now take 1 element from front and one from back with linkage
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        res = slow.next
        slow.next = None
        prev = None

        while res:
            temp = res.next
            res.next = prev
            prev = res
            res = temp

        left, right = head, prev
        while right:
            temp1 = left.next
            temp2 = right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2

        