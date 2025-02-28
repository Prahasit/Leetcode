class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if 1 <= i <= len(nums):
                res.append(i)
        res.sort()
        k = 1
        for i in res:
            if i == k:
                k += 1
        
        return k
        
        