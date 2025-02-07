class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #use dfs and store all the points of an island
        #then find closet "1" which does not belong to the island.
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r,c) not in visit:
                visit.add((r,c))
                q.append([r,c])

                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)

        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        found = False
        for i in range(m):
            if found :
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            
        
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visit:
                        if grid[new_r][new_c] == 1:
                            return steps
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
            
            steps += 1

        return - 1
