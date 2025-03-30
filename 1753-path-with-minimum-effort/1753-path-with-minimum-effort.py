class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pq = []
        heapq.heappush(pq,(0, 0, 0)) #dist, row, col
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        abs_min = float('-inf')
        while pq:
            diff, row, col, = heapq.heappop(pq)
            if row == m - 1 and col == n - 1:
                return diff
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n:
                    new_effort = max(abs(heights[row][col]- heights[r][c]), diff)
                    if new_effort < dist[r][c]:
                        dist[r][c] = new_effort
                        heapq.heappush(pq, (new_effort, r, c))


        return 0