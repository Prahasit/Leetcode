class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}': '{', ']':'['}
        stack = []
        for bracket in s:
            if bracket in mapping:
                if stack and stack[-1] == mapping[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False

