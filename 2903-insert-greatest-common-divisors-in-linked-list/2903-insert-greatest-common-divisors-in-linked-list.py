# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        def gcd(x, y): # where y is the greater value
            while y != 0:
                x, y = y, x % y

            return x

        while cur and cur.next:
            if cur.val > cur.next.val:
                x, y = cur.next.val, cur.val
                num = gcd(x, y)

            else:
                x, y = cur.val, cur.next.val
                num = gcd(x, y)

            gcd_node = ListNode(num)
            gcd_node.next = cur.next
            cur.next = gcd_node
            cur = gcd_node.next


        return dummy.next


        