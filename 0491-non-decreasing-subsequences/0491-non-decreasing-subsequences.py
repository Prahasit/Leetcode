class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        subset = []
        def solve(idx, prev):
            if idx == n:
                if len(subset) >= 2:
                    res.add(tuple(subset[:]))
                return

            solve(idx + 1, prev) #move forward
            if nums[idx] >= prev:
                subset.append(nums[idx])
                solve(idx + 1, nums[idx])
                subset.pop()
            
        solve(0, float(-inf))
        return list(res)
