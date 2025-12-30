class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        n = len(temperatures)
        for i in range(n - 1, - 1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i 
            stack.append(i)

        return res




