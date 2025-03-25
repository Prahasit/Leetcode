class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            max_val = nums[i]
            min_val = nums[i]
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])

                result += max_val - min_val

        return result