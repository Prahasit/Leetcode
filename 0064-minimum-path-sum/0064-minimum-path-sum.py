class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp =[[-1 for _ in range(n)] for _ in range(m)] 
        res = float('inf')
        def dfs(i, j):
            nonlocal res
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            up = dfs(i - 1, j)
            left = dfs(i, j - 1)
            
            dp[i][j] = grid[i][j]+ min(up, left)
            return dp[i][j]

        return dfs(m - 1, n - 1)