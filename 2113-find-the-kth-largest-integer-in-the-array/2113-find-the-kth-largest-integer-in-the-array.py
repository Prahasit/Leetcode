class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq = [-int(s) for s in nums]
        heapq.heapify(pq)
        while k > 0:
            val = -heapq.heappop(pq)
            k -= 1
        return str(val)

