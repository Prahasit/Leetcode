class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #removing from the front reduces the num rather than from the end
        # eg in 1432219: remove 4->132219 , remove 9-> 143221 where 132219 < 143221
        n = len(num)
        stack = []
        for i in range(n):
            while stack and k > 0 and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            if k == 0:
                stack.append(num[i])
                continue
            
            stack.append(num[i])
        print(stack)

        # edge case if k >0 after iteration:
        if k >= len(stack):
            return '0'
        elif k <= len(stack):
            while k > 0 and stack:
                
                stack.pop() # as stack in increasing order only after the for loop iteration so we can delete from the top as it contains max value
                k -= 1 
        # taking stack and converting to string
        s = ""
        while stack:
            no = stack.pop()
            s = no + s

        print(s)
        

        
        # trimming the leading zeroes
        for i in range(len(s)):
            if s[i] != '0':
                s = s[i:]
                break
        else:
            s = '0' #if all are zeroes keep only one zero
        print(s)

        return s
