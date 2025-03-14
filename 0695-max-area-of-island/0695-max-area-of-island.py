class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def solve(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            if (r, c) in visit:
                return 0
            visit.add((r,c))

            length = 1
            up = solve(r - 1, c)
            down = solve(r + 1, c)
            left = solve(r, c - 1)
            right = solve(r, c + 1)

            return length + up + down + left + right

        m, n = len(grid), len(grid[0])
        visit = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and grid[i][j] == 1:
                    count = solve(i, j)
                    res = max(count, res)
        
        return res


        