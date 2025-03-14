class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(ind, prev_val):
            if ind == n:
                return 0
            if (ind, prev_val) in memo:
                return memo[(ind, prev_val)]

            not_take = solve(ind + 1, prev_val)

            take = float('-inf')
            if nums[ind] > prev_val:
                take = 1 + solve(ind + 1, nums[ind])
            
            memo[(ind, prev_val)] = max(not_take, take)
            return memo[(ind, prev_val)]

        memo = {}
        return solve(0, float('-inf'))