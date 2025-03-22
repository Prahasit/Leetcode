# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)
        cur = head
        temp = 0
        while cur:
            if cur.val in nums_set:
                temp += 1
            else:
                if temp > 0:
                    ans += 1
                temp = 0
            
            cur = cur.next
            
        if temp > 0:
            ans += 1

        return ans
