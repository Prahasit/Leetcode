class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = mat[0][0]
        ans = [0,0]
        for i in range(m):
            for j in range(n):
                if mat[i][j] >= res:
                    res = mat[i][j]
                    ans = [i, j]
        return ans