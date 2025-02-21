class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq = [- num for num in nums]
        heapq.heapify(pq)
        while pq:
            x = -heapq.heappop(pq)
            return (x - 1) * (-heapq.heappop(pq) - 1)