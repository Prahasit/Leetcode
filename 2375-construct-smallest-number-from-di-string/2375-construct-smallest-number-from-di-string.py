class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        res = []
        stack = []

        # we will use digits 1..len(pattern)+1
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))

            # if end OR we see 'I', flush stack
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())

        return "".join(res)
