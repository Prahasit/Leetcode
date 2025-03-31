class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # dont try to emove 
        #try to find with the obstacle and return the minimum value i.e minimum obstacles occur in that path
        #so use dijkstra with first val as obstacle

        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = []
        heapq.heappush(heap, (0, 0, 0)) # obstacles, row, col
        visit = set()

        while heap:
            obstacles, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return obstacles
            if (r, c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < m and 0 <= col < n:
                    if (row, col) not in visit:
                        if grid[row][col] == 0:
                            heapq.heappush(heap, (obstacles, row, col))
                        else:
                            heapq.heappush(heap, (obstacles + 1, row, col))



            
