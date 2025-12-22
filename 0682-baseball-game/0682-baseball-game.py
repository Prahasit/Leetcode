class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for score in operations:
            if score == '+':
                stack.append(stack[-1] + stack[-2])
            elif score == 'D':
                stack.append(2 * stack[-1])
            elif score == 'C':
                stack.pop()

            else:
                stack.append(int(score))
        
        return sum(stack)