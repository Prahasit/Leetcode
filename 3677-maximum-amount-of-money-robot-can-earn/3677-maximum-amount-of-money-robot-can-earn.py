class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m=len(coins)
        n=len(coins[0])
        inf=float('inf')
        dp=[[[inf]*3 for _ in range(n)]for _ in range(m)]

        def solve(i,j,k):
            if i>=m or j>=n or k<0:return -inf
            if i==m-1 and j==n-1:
                if coins[i][j]<0 and k>0:
                    dp[i][j][k]=0
                else: 
                    dp[i][j][k]=coins[i][j]
                return dp[i][j][k]
            if dp[i][j][k]!=float('inf'):
                return dp[i][j][k]
            ans=coins[i][j]+max(solve(i+1,j,k),solve(i,j+1,k))
            if coins[i][j]<0:
                ans=max(ans,max(solve(i+1,j,k-1),solve(i,j+1,k-1)))
            dp[i][j][k]=ans
            return dp[i][j][k]

        return solve(0,0,2)