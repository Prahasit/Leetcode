class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we are taking prev_ind as - 1 but we cant store index as - 1 in array so we do coordinate change where - 1 will be 0, 0 will be 1 etc so adding + 1
        #hence len of dp is dp[n][n + 1]
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        def dfs(ind, prev_ind):
            if ind == n:
                return 0
            if dp[ind][prev_ind] != -1:
                return dp[ind][prev_ind]
            len = 0 + dfs(ind + 1, prev_ind) #not take
            if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                len = max( len, 1 + dfs(ind + 1, ind)) # max of take and not take
            dp[ind][prev_ind] = len
            return dp[ind][prev_ind]
        return dfs(0, - 1)