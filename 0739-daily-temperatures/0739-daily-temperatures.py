class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = [] #temperature[ind], ind
        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                result[idx] = i - idx

            stack.append((temperatures[i], i))

        return result