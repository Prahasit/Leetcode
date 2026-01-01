class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = float('inf')
        memo = {}
        m, n = len(grid), len(grid[0])

        def solve(r, c):
            nonlocal res
            if r == 0 and c == 0:
                return grid[r][c]
            if r < 0 or c < 0:
                return float('inf')

            if (r,c) in memo:
                return memo[(r,c)]


            up = solve(r - 1, c)
            left = solve(r, c - 1)

            memo[(r,c)] = grid[r][c] + min(up , left)
            return memo[(r,c)]

        return solve(m - 1, n - 1)
