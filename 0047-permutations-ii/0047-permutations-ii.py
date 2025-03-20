class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = Counter(nums)
        def solve(permutation, subset):
            if len(subset[:]) == len(nums):
                result.append(subset[:])
                return


            for key in permutation:
                if permutation[key] > 0:
                    subset.append(key)
                    permutation[key] -= 1
                    solve(permutation, subset)

                    subset.pop()
                    permutation[key] += 1

        solve(permutation, [])
        return result