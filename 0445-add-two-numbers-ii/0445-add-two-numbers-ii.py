# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # c1, c2 = 0, 0
        # cur1, cur2 = l1, l2
        # while cur1:
        #     c1 += 1
        #     cur1 = cur1.next
        # while cur2:
        #     c2 += 1
        #     cur2 = cur2.next
        
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        list1 = reverse(l1)
        list2 = reverse(l2)
        print(list1)
        print(list2)

        dummy = ListNode()
        current = dummy
        carry = 0
        while list1 or list2 or carry:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            temp = val1 + val2 + carry
            carry =  temp // 10
            temp = temp % 10
            current.next = ListNode(temp)
            current = current.next
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next

        return reverse(dummy.next)
            
