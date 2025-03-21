class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return - 1
        slow = self.head.next # as head here is dummy node
        while index > 0:
            slow = slow.next
            index -= 1
        return slow.val

        

    def addAtHead(self, val: int) -> None:
        cur = ListNode(val)
        cur.next = self.head.next
        self.head.next = cur
        self.size += 1   

    def addAtTail(self, val: int) -> None:
        temp = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = temp
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return 

        slow = self.head
        while index > 0:
            slow = slow.next
            index -= 1
        node = ListNode(val)
        node.next = slow.next
        slow.next = node

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        slow = self.head
        while index > 0:
            slow = slow.next
            index -= 1
        slow.next = slow.next.next

        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)