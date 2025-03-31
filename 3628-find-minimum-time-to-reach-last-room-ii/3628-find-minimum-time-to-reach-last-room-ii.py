class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 1)] # time, row, col, steps
        visit = set()
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        seconds = 0
        while heap:
            time, r, c, steps = heapq.heappop(heap)
            seconds += 1
            print(seconds)
            if (r, c) == (n - 1, m - 1):
                return time
                
            # If the cell has already been visited with a smaller time, skip it
            if (r, c) in visit:
                continue

            # Mark the cell as visited
            visit.add((r, c))

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < n and 0 <= new_c < m:
                    next_time = max(time, moveTime[new_r][new_c]) + steps
                    if steps == 1:
                        next_steps = 2
                    else:
                        next_steps = 1
                    heapq.heappush(heap, (next_time, new_r, new_c, next_steps))
                    
                    