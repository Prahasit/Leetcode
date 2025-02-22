class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # to optimize the Tc, need to use heaps 
        #we need to sort the array while maintaining the index
        res = [""] * len(nums)
        nums = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(nums)
        while k:
            val, i = heapq.heappop(nums)
            res[i] = -val
            k -= 1
        res = [val for val in res if val != ""]
        return res