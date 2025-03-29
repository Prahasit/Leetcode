class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if r < 0 or c < 0 or r >=m or c >= n or grid[r][c] == 0:
                return 0
            
            if (r, c) in visit:
                return 0
            visit.add((r, c))

            number = grid[r][c]
            number += dfs(r - 1,c)
            number += dfs(r + 1,c)
            number += dfs(r,c - 1)
            number += dfs(r,c + 1)

            return number


        m, n  = len(grid), len(grid[0])
        visit = set()
        max_fish = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish