class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(idx, total):
            nonlocal res
            if idx >= len(nums):
                res = max(res, total)
                return total
            if (idx, total) in memo:
                return memo[(idx, total)]

            not_take = solve(idx + 1, total)
            take = solve(idx + 2, total + nums[idx]) 

            memo[(idx, total)] = max(take, not_take)
            return memo[(idx, total)]

        res = 0
        memo = {}
        solve(0, 0)
        return res