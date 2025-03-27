class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return - 1
            if (r,c) in visit or grid[r][c] == 1:
                return True
            
            visit.add((r,c))

            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            if up == - 1 or down == - 1 or left == - 1 or right == -1:
                return - 1
            
            return True
                
        m, n = len(grid), len(grid[0])
        res = 0
        visit = set()
        for i in range(m):
            for j in range(n):
                if (i, j ) not in visit and grid[i][j] == 0:
                    if dfs(i, j) != -1:
                        res += 1

        return res

                    