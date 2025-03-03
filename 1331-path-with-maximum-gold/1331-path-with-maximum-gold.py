class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            if (r,c) in visit:
                return 0
            visit.add((r,c))

            temp = grid[r][c]
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            visit.remove((r, c))
            return temp + max(up, down, left, right)

        m, n = len(grid), len(grid[0])
        visit = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j))
        return res