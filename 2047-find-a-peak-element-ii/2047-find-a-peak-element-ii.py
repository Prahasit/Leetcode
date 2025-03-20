class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        #apply binary search on column and scan through the row for max element
        #as we get max element on row, we only need to check for left and right and no need to check for up and down as it is already max element i. col 
        m, n = len(mat), len(mat[0])
        l, r = 0, n - 1

        def maxelement(mid):
            res  = - 1
            for i in range(m):
                if mat[i][mid] >= res:
                    res = mat[i][mid]
                    index = i
            return index

        while l<= r:
            mid = (l + r) // 2
            row_ind = maxelement(mid)
            left = mat[row_ind][mid - 1] if mid -1 >= 0 else - 1
            right = mat[row_ind][mid + 1] if mid + 1 < n else - 1

            # if the maximum element of all rows in mid column is greater than left and right return
            if mat[row_ind][mid] > left and mat[row_ind][mid] > right:
                return [row_ind, mid]
            elif left > mat[row_ind][mid]:
                r = mid - 1
            else:
                l = mid + 1
                


        