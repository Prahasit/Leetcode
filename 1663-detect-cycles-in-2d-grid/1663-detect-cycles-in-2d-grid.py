class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # we need to save the initial position somewhere 
        # if positio i. visit and equals to intial then there is cycle
        #also given cycle is length 4 or more
        def bfs(i, j):
            val = grid[i][j]
            visit.add((i,j))
            q = deque([(i, j, None)])

            while q:
                r, c, prev = q.popleft()
                
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == val:
                        if (new_r,new_c) not in visit:

                            visit.add((new_r,new_c))
                            q.append((new_r, new_c, (r,c)))
                        elif (new_r, new_c) != prev:
                            return True

            return False




        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit:
                    if bfs(i, j):
                        return True
        return False
        