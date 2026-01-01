class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = ListNode(0, 0)
        self.right = ListNode(0 , 0)

        self.left.next, self.right.prev = self.right, self.left

        
    def insert(self, node):
        pre, nxt = self.right.prev, self.right
        pre.next = nxt.prev = node
        node.next, node.prev = nxt, pre
    
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)