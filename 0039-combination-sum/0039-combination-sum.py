class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def solve(idx, total, subset):
            if total > target or idx >= len(candidates):
                return
            if total == target:
                result.append(subset[:])
                return 

            
            subset.append(candidates[idx])
            solve(idx,total + candidates[idx], subset)
            subset.pop()
            solve(idx + 1, total, subset)
                


        solve(0, 0, [])
        return result