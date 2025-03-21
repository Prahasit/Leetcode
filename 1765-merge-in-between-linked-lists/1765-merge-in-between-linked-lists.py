# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        slow = list1
        fast = list1
        i = 0
        while i < a - 1:
            slow = slow.next
            fast = fast.next
            i += 1
        while i < b:
            fast = fast.next
            i += 1

        temp = fast.next
        fast.next = None

        slow.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = temp

        return list1



        