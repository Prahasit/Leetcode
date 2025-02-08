class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        tot_sum = sum(nums)
        for i in range(len(nums) - 1, 1, -1):
            tot_sum -=nums[i]
            if tot_sum > nums[i]:
                return tot_sum + nums[i]
        return - 1
        