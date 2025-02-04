class Solution:
    def calculateScore(self, s: str) -> int:
        mark = [[] for _ in range(26)]
        res = 0
        for i, ch in enumerate(s):
            cur = ord(ch) - 97
            if mark[25 - cur]:
                res += i - mark[25 - cur].pop()
            else:
                mark[cur].append(i)
        return res

