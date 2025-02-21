class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n > 1:
            return (nums[n - 1] - 1) * (nums[n - 2] - 1)

        else:
            return nums[0] - 1