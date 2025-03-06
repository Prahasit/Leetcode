class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        def solve(i ,j):
            if i  == n1 or j == n2:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if nums1[i] == nums2[j]:
                dp[(i,j)]  = 1 + solve(i + 1, j + 1)
            else:
                dp[(i,j)] = max(solve(i, j + 1), solve(i + 1, j))

            return dp[(i,j)]

        n1, n2 = len(nums1), len(nums2)
        dp = {}
        return solve(0 , 0)