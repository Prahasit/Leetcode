class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-val for val in nums]
        heapq.heapify(heap)
        while k > 0:
            val = heapq.heappop(heap)
            k -= 1
        return -1*val