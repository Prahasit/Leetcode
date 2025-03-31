class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit = set()
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while heap:
            time, r, c = heapq.heappop(heap)
        
            if r == m - 1 and c == n - 1:
                return time
            if (r, c) in visit:
                continue
            visit.add((r, c))

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n:
                    if (row, col) not in visit:
                        if (grid[row][col] - time) % 2 == 0:
                            wait_time = 1
                        else:
                            wait_time = 0
                        next_time = max(grid[row][col] + wait_time, time + 1)
                        heapq.heappush(heap, (next_time, row, col))

        
        return - 1