class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        res = -1
        def smallestdivisor(limit):
            total = 0
            for i in range(len(nums)):
                total += ceil(nums[i]/ limit)
            return total
        while l <= r:
            mid = (l + r) // 2
            if smallestdivisor(mid) <= threshold:
                res = mid
                r = mid - 1  
            else:
                l = mid + 1

        return res
