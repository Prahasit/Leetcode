class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        count = 0
        postfix = sum(nums)
        for i in range(n):
            prefix += nums[i]
            postfix -= nums[i]
            if prefix >= postfix and i < n - 1:
                count += 1

        return count

        