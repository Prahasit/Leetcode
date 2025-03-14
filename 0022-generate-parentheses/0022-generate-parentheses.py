class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def solve(open, closed):
            if open == n and closed == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                solve(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                solve(open, closed + 1)
                stack.pop()

        solve(0, 0)
        return res