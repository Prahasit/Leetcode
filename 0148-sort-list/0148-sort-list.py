# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next= None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val  < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next

            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

        return dummy.next


