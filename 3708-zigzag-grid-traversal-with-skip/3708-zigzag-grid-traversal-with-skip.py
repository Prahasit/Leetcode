class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []
        skip = False
        for i in range(m):
            if i % 2 == 0:
                row = range(n)
            else:
                row = range(n - 1, - 1, -1)
            
            for j in row:
                if not skip:
                    result.append(grid[i][j])
                skip = not skip
        return result
        