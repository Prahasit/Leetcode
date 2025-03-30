class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
       
        directions = [[0, 1], [0, -1], [1, 0], [-1,0]]
        dist = [[float('inf')] * n for _ in range(m)]
        heap = []
        heapq.heappush(heap, (0 , 0 , 0))

        dist[0][0] = 0
        while heap:
            diff, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return diff

            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n:
                    new_effort = max(abs(heights[row][col] - heights[r][c]),diff)
                    if new_effort < dist[row][col]:
                        dist[row][col] = new_effort
                        heapq.heappush(heap, (new_effort, row, col))

        return 0
            

