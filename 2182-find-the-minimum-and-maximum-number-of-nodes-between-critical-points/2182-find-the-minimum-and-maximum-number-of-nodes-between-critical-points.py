# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [] #storing cirtical points indices
      
        cur = head.next
        if cur.next is None:
            return [-1, -1]
        prev = head.val
        i = 1
        while cur.next:
            i += 1
            if (cur.val > prev and cur.val > cur.next.val) or (cur.val < prev and cur.val < cur.next.val):
                res.append(i)

            prev = cur.val
            cur = cur.next
        if len(res) < 2:
            return [-1, -1]
        maxi = res[-1] - res[0]
        mini = float(inf)
        for i in range(1, len(res)):
            mini = min(mini, res[i] - res[i - 1])

        return [mini, maxi]

    
