class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        heapq.heappush(heap, (grid[0][0], 0 , 0))
        visit = set()
        directions = [[0,1], [0, -1], [ 1, 0], [-1, 0]]

        while heap:
            elevation, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return elevation

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < n and 0 <= col < n and (row, col) not in visit:
                    visit.add((row, col))
                    heapq.heappush(heap, (max(elevation, grid[row][col]), row, col))