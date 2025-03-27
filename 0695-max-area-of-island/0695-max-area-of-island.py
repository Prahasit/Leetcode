class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r, c))
            length = 0
            while q:
                row, col = q.popleft()
                length += 1
                for dr, dc in directions:
                    new_r, new_c = dr + row, dc + col
                    if  0 <= new_r < m and 0<= new_c < n and grid[new_r][new_c] == 1:
                        if (new_r, new_c) not in visit:
                            q.append((new_r, new_c))
                            visit.add((new_r, new_c))
            return length

            


        m, n = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        directions = [[0,1], [0, - 1], [-1,0], [1,0]]
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
                    print(max_area)

        return max_area




        