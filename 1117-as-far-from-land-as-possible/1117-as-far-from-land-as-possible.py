class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        res = -1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
        

        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < n and 0 <= col < n:
                    if grid[row][col] == 0:
                        grid[row][col] = dist + 1
                        res = max(res, grid[row][col])
                        q.append((row, col, grid[row][col]))
        return res

