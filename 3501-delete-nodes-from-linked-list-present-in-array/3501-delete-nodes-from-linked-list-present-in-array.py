# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode()
        prev = dummy
        cur = head
        while cur:
            if cur.val in nums_set:
                cur = cur.next
            else:
                node = ListNode(cur.val)
                prev.next = node
                prev = prev.next
                cur = cur.next

        return dummy.next