class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r, c) in visit or r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            visit.add((r,c))

            land = 1
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return land + up + down + left + right

        #finding the area of land for each grid element
        max_area = 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, - 1], [1, 0], [-1,0]]
        visit = set()
        island_id = 2
        island_areas = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visit.clear()
                    area = dfs(i, j)
                    #store all in the same visit to the same area value
                    for r,c in visit:
                        grid[r][c] = island_id
                    max_area = max(max_area, area)
                    island_areas[island_id] = area #store island area
                    island_id += 1

        #changing cell 0 to 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    adj_islands = set()
                    area = 1
                    for dx, dy in directions:
                        new_r, new_c = i + dx, j + dy
                        if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] > 1:
                            adj_islands.add(grid[new_r][new_c])

                    for island in adj_islands:
                        area += island_areas[island]
                    max_area = max(max_area, area)
        return max_area
