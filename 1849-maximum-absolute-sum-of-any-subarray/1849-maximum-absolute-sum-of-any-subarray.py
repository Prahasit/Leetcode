class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # cannot be solved with take, not take as its subarray not subsequence
        #max_sum is max +Ve sum and max -ve sum
        n = len(nums)
        res_max, res_min = 0, 0
        total_max_sum = 0
        total_min_sum = 0
        result = 0
        for i in range(n):
            total_max_sum += nums[i]
            res_max = max(res_max, total_max_sum)
            if total_max_sum < 0:
                total_max_sum = 0
        
        
            total_min_sum += nums[i]
            res_min = min(res_min, total_min_sum)
            if total_min_sum > 0:
                total_min_sum = 0

        result = max(res_max, abs(res_min))
        return result