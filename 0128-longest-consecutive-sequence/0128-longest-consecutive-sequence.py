class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = 1
        cur = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - nums[i - 1] == 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best


        