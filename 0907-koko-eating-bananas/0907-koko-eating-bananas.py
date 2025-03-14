class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = -1
        def solve(num):
            total = 0
            for i in range(len(piles)):
                total += ceil(piles[i]/ num)
            return total
        while l <= r:
            mid = (l + r) // 2
            if solve(mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res