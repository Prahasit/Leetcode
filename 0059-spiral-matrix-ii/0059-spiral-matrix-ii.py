class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            #1. top row taversing
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1

            #2. right column
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1

            #3. bottom column
            if top <= bottom:
                for i in range(right, left - 1, - 1):
                    res[bottom][i] = num
                    num += 1
                bottom -= 1

            #4. left column
            if left <= right:
                for i in range(bottom, top - 1, - 1):
                    res[i][left] = num
                    num += 1
                left += 1

        return res
        