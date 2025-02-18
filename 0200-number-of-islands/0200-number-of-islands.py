class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0' or (r,c) in visit:
                return False
            
            visit.add((r,c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visit:
                    if dfs(i,j):
                        count += 1

        return count