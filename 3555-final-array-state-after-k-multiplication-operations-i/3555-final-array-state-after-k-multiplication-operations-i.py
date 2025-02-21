class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(pq)
        while pq and k > 0:
            val, idx = heapq.heappop(pq)
            nums[idx] = val * multiplier
            heapq.heappush(pq, (nums[idx], idx))
            k -= 1
        return nums


        