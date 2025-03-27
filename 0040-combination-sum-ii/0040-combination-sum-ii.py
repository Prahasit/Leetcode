class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def explore(subset, idx, total):
            if total == target:
                res.append(subset[:])
                return
            if total > target or idx >= len(candidates):
                return

            
            subset.append(candidates[idx])
            explore(subset, idx + 1, total + candidates[idx])
            subset.pop()
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            explore(subset, idx + 1, total)
            
        explore([], 0, 0)
        return res

        