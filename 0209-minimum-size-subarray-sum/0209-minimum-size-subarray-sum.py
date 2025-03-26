class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        sub_sum = 0
        minlen = float('inf')
        while r < n:
            sub_sum += nums[r]
            
            while sub_sum >= target:
                minlen = min(minlen, r - l + 1)
                sub_sum -= nums[l]
                l += 1
            
            

            r += 1
        return minlen if minlen != float('inf') else 0

