class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = min(bloomDay), max(bloomDay)
        res = -1
        val = m * k
        if val > len(bloomDay):
            return - 1
        def solve(days):
            total = 0
            cnt = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= days:
                    cnt += 1
                else:
                    total += cnt // k
                    cnt = 0
            total += cnt // k
            if total >= m:
                return True
            else:
                return False


        while l <= r:
            mid = (l + r) // 2
            if solve(mid):
                res = mid
                r = mid - 1

            else:
                l = mid + 1

        return res