class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # for every index previous smaller element(pse) and next smaller lement(nse)
        # for every index it will be pse * nse
        n = len(arr)
        total_sum = 0
        stack1, stack2 = [], []
        pse = [-1] * n
        nse = [-1] * n
        MOD = (10 ** 9) + 7

        #finding next smaller element(NSE)
        for i in range(n - 1, - 1, -1):
            while stack1 and arr[i] <= arr[stack1[-1]]:
                stack1.pop()

            if not stack1:
                nse[i] = n
            else:
                nse[i] = stack1[-1]
            stack1.append(i)
        
        #finding previous smaller element (PSE)
        for i in range(n):
            while stack2 and arr[i] < arr[stack2[-1]]:
                stack2.pop()
            if not stack2:
                pse[i] = -1
            else:
                pse[i] = stack2[-1]
            
            stack2.append(i)
        print(nse)
        print(pse)
        for i in range(n):
            right = nse[i] - i
            left = i - pse[i]
            total_sum = (total_sum + arr[i] * left * right) % MOD
        return total_sum


