class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0,1], [0, - 1], [1, 0], [-1,0], [-1,-1], [1,1],[-1,1],[1,-1]]
        visit = set()
        q = deque()
        if grid[0][0] == 1:
            return - 1
        else:
            q.append((0, 0, 1))

        while q:
            r, c, path = q.popleft() 
            if r == n - 1 and c == n - 1 and grid[r][c] == 0:
                return path
            
            for dr, dc in directions:
                row, col = dr+ r, dc+ c
                if 0 <= row < n and 0 <= col < n:
                    if (row, col) not in visit and grid[row][col] == 0:
                        q.append((row, col, path + 1))
                        visit.add((row, col))
            
                
        return - 1
        