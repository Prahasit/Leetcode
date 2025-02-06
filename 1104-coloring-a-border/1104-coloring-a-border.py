class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    
        m, n = len(grid), len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        directions = [[0,1], [-1, 0], [0, -1], [1, 0]]
        q = deque([(row, col)])
        target_color = grid[row][col]
        visit[row][col] = True

        while q:
            r, c = q.popleft()
            visit[r][c] = True
            #color boundary elements with given color
            if r == m - 1 or c == n - 1 or r == 0 or c == 0:
                grid[r][c] = color
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and not visit[new_r][new_c]:                   #color if adjacent elemnt has different color
                    if grid[new_r][new_c] != target_color:
                        grid[r][c] = color
                    else:
                        q.append((new_r, new_c))
        return grid