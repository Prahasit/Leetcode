class Solution:
    def countAndSay(self, n: int) -> str:

        def explore(s):
            res = []
            count = 1
            for i in range(len(s)):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(s[i])
                    count = 1
            return ''.join(res)
                

        seq = '1'
        for _ in range(n - 1):
            seq = explore(seq)
        return seq
        