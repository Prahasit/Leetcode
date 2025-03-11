class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def solve(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len (s2)
            if (i, j) in memo:
                return memo[(i,j)]

            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = res or solve(i + 1, j ,k + 1)
                    
            if j < len(s2) and s2[j] == s3[k]:
                res = res or solve(i, j + 1, k + 1)
            #used or above as res calculate firest can be changed if calculated afterwards.
            memo[(i,j)] = res
            return memo[(i,j)]

        memo = {}
        return solve(0, 0, 0)