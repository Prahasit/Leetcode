class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
            max_sum = max(max_sum, total)

            if total < 0:
                total = 0

        return max_sum
