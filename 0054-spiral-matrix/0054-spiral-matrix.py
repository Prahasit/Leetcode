class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #1. traverse 1st row, 2. traverse right column 
        #3. traverse bottom row, traverse 1st column

        res = []
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        top, bottom = 0, m
        left, right = 0, n
        while top <= bottom and left <= right:
            #1. top row taversing
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            #2. right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            #3. bottom column
            if top <= bottom:
                for i in range(right, left - 1, - 1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            #4. left column
            if left <= right:
                for i in range(bottom, top - 1, - 1):
                    res.append(matrix[i][left])
                left += 1

        return res