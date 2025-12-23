class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        minlen = float('inf')
        cur_sum = 0

        while r < n:
            cur_sum += nums[r]

            while cur_sum >= target:
                minlen = min(minlen, r - l + 1)
                cur_sum -= nums[l]
                l += 1

            r += 1

        return minlen if minlen != float('inf') else 0