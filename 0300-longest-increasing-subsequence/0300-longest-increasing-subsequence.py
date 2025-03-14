class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(ind, prev_ind):
            if ind == n:
                return 0
            if dp[ind][prev_ind + 1] != -1 :
                return dp[ind][prev_ind + 1]

            not_take = solve(ind + 1, prev_ind)

            take = float('-inf')
            if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                take = 1 + solve(ind + 1, ind)
            
            dp[ind][prev_ind] = max(not_take, take)
            return dp[ind][prev_ind]

        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return solve(0, -1)