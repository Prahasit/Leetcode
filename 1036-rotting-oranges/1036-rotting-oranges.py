class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh_orange = 0
        time = 0
        directions = [[0,1], [0, -1], [1,0], [-1,0]]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_orange += 1
        if fresh_orange == 0:
            return time
        while q:
            if fresh_orange == 0:
                return time
            for _ in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        if (row, col) not in visit:
                            q.append((row, col))
                            grid[row][col] = 2
                            fresh_orange -= 1

            
            time += 1

        
        return - 1
                        


        