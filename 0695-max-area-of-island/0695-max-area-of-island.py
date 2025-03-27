class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if r < 0 or c < 0 or  r >= m or c >= n or grid[r][c] == 0:
                return  0
            if (r,c) in visit:
                return  0
            visit.add((r,c))

            length = 1
            length += dfs(r - 1, c)
            length += dfs(r + 1, c)
            length += dfs(r, c - 1)
            length += dfs(r, c + 1)

            return length


        m, n = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area




        