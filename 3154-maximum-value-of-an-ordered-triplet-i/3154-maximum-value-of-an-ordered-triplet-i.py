class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # O(n^2) --> need to maximize the k and i only
        n = len(nums)
        res = 0
        
        for k in range(2, n):
            max_prefix = nums[0]
            for j in range(1, k):
                res = max(res, (max_prefix - nums[j]) * nums[k])
                max_prefix = max(max_prefix, nums[j])
        return res
                