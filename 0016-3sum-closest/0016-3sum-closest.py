class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = []
        closest_sum = float('inf')
        for i,a in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                totsum = a + nums[l] + nums[r]

                if abs(totsum - target) < abs(closest_sum - target):
                    closest_sum = totsum

                if totsum > target:
                    r -= 1
                elif totsum < target:
                    l += 1
                else:          
                    return totsum
        return closest_sum
