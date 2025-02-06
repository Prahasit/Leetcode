class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)
        operations_1, operations_2 = 0, k
        for i in range(n):
            operations_1 += abs(arr[i] - brr[i])
        
        arr.sort()
        brr.sort()
        for i in range(n):
            operations_2 += abs(arr[i] - brr[i])
        
        return min(operations_1, operations_2)
        
