class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = 0
        freq = Counter(arr)
        heap = [-val for num,val in freq.items()]
        heapq.heapify(heap)
        i = 0
        cur = 0

        while cur < len(arr) // 2:
            cur += -heapq.heappop(heap)
            count += 1
            
        return count


