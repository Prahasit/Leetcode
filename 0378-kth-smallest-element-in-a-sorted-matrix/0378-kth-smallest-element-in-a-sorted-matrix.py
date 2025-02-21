class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # as rows and cols values are in sorted order
        #first traverse row 0 then row 1 etc...
        n = len(matrix)
        res = []
        for i in range(n):
            for j in range(n):
                res.append(matrix[i][j])
        
        res.sort()
        return res[k - 1]