class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()

        def explore(row, col):
            row_inbounds = 0 <= row < len(grid)
            col_inbounds = 0 <= col < len(grid[0])
            if not row_inbounds or not col_inbounds:
                return False
            
            if grid[row][col] == "0":
                return False

            pos = (row, col)
            if pos in visited:
                return False
            visited.add(pos)

            explore(row - 1, col)
            explore(row + 1, col)
            explore(row, col - 1)
            explore(row, col + 1)

            return True

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if explore(row, col):
                    count += 1
        return count

        