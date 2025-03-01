class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def solve(perms, idx):
            if idx == n:
                res.append(perms)
                return

            if s[idx].isalpha():
                solve(perms + s[idx].lower(), idx + 1)
                solve(perms + s[idx].upper(), idx + 1)
            else:
                solve(perms + s[idx], idx + 1)

        solve("", 0)
        return res