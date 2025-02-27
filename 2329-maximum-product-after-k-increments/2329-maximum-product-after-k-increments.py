class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        #need to make the lowest values increment as medium * medium > highest * lowest

        MOD = 10 ** 9 + 7
        heapq.heapify(nums)
        while k > 0:
            least = heapq.heappop(nums)
            heapq.heappush(nums, least + 1)
            k -= 1
        
        val = 1
        while len(nums) > 0:
            val *= heapq.heappop(nums)

        return val % MOD
