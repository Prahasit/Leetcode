class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        #1. we add the '1' in queue
        #2. find the min distance of each '0' from '1'
        #3. now apply dijkstra's algorithm
        n = len(grid)
        directions = [[0, 1], [0, - 1], [1, 0], [-1, 0]]

        def bfs():
            q = deque()
            min_dist = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        q.append((r, c, 0)) # adding '1'  in queue with dist = 0
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if 0 <= row < n and 0 <= col < n and (row, col) not in min_dist:
                        min_dist[(row, col)] = dist + 1
                        q.append((row, col, dist + 1))
            return min_dist

        min_dist = bfs()

        max_heap = [(-min_dist[(0,0)],0, 0)]
        visit = set()
        visit.add((0 , 0))

        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = -dist
            if r == n - 1 and c == n - 1:
                return dist
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < n and 0 <= col < n and (row, col) not in visit:
                    visit.add((row, col))
                    distance = min(dist, min_dist[(row, col)]) # as we need minimum manhattan distance
                    heapq.heappush(max_heap, (-distance, row, col)) # we need to push max -ve number 
            
