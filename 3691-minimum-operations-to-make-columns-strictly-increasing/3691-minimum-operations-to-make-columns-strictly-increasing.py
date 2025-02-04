class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        operations = 0
        for i in range(m - 1):
            for j in range(n):
                if grid[i + 1][j] - grid[i][j] <= 0:
                    operations += grid[i][j] + 1 - grid[i + 1][j]
                    grid[i + 1][j] = grid[i][j] + 1
        return operations      