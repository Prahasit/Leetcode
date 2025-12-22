class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for exp in tokens:
            if exp == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)


            elif exp == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif exp == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            elif exp == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(exp))
            
        return stack[-1]    