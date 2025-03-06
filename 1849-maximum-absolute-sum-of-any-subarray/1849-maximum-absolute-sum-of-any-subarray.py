class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix = 0
        max_prefix = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix = min(min_prefix, prefix_sum)
            max_prefix = max(max_prefix, prefix_sum)

        return max_prefix - min_prefix
        