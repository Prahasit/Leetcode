class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        pq = [(-val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(pq)
        while k > 0:
            val, idx = heapq.heappop(pq)
            score += -val
            new_val = math.ceil(-val / 3)
            heapq.heappush(pq, (-new_val, idx))
            k -= 1
        return score
