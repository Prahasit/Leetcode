class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        heap = [(grid[0][0], 0, 0)]
        time = 0
        while heap:
            dist, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return dist
            visit.add((r,c))
            time += 1
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n  and (row, col) not in visit:
                    visit.add((row,col))
                    time = max(dist, grid[row][col])
                    heapq.heappush(heap, (time, row, col))
        
        

    