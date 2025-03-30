class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # apply bfs to get the distances of '0's from '1's.
        #then apply dikstra usng max_heap to traverse the maximum paths

        def bfs():
            q = deque()
            min_dist = {}
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i,j , 0))
                        min_dist[(i, j)] = 0
            
            while q:
                r, c, dist = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if 0 <= row < n and 0<= col < n and (row, col) not in min_dist:
                        min_dist[(row, col)] = dist + 1
                        q.append((row, col, dist + 1))

            return min_dist

        n = len(grid)
        directions = [[0,1], [0,-1], [1,0], [-1, 0]]
        min_dist = bfs()
        

        heap = [(-min_dist[(0,0)], 0, 0)]
        visit = set()
        visit.add((0, 0))

        while heap:
            dist, r, c = heapq.heappop(heap)
            dist = -dist
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if 0 <= row < n and 0 <= col < n:
                    if (row, col) not in visit:
                        visit.add((row, col))
                        distance = min(dist, min_dist[(row,col)])
                        heapq.heappush(heap, (-distance, row, col))

        
        return 0