class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        res = 0
        visit = set()

        def solve(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            length = 1
            length += solve(r - 1, c)
            length += solve(r + 1, c)
            length += solve(r, c - 1)
            length += solve(r, c + 1)

            return length


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                
                    if (i ,j) not in visit and i in [0, m - 1] or j in [0, n - 1]:
                        res += solve(i, j)

        return total - res