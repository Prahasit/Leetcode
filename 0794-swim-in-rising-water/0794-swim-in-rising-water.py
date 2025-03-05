class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # same at finding  min among the path and find at last max(found, grid[m - 1][n - 1])
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visit = set()
        directions = [[0, 1], [0 , -1], [1, 0], [-1, 0]]
        while heap:
            elevation, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return elevation
            
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n and (row,col) not in visit:
                    visit.add((row, col))
                    heapq.heappush(heap, (max(elevation, grid[row][col]), row, col))
        