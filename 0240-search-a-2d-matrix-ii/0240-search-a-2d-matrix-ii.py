class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == target:
                    return True

        return False