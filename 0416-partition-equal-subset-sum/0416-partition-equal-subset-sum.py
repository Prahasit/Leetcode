class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # S1 + S2 = SUM where S1 = S2 so find sum/2
        # so we just need to find the subset sum //2
        n = len(nums)

        def SubsetSum(nums, s):
            nonlocal n
            dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]
            for i in range(n + 1):
                for j in range(s + 1):
                    if i == 0:
                        dp[i][j] = False
                    if j == 0:
                        dp[i][j] = True

            for i in range(1, n + 1):
                for j in range(s + 1):
                    if nums[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[n][s]
        # if sum of elements is.odd cannot partition equally
        if sum(nums) % 2 != 0:
            return False 
        elif sum(nums) % 2 == 0:
            return SubsetSum(nums, sum(nums) // 2)
        

        
        
