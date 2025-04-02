class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #finding leftmax and rightmax for every element
        n = len(nums)
        res = 0
        left_max = [0] * n
        right_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i - 1])
            right_max[n - i - 1] = max(right_max[n - i], nums[n - i])
        print(left_max)
        for j in range(1, n - 1):
            res = max(res, (left_max[j] - nums[j]) * right_max[j])

        
        return res