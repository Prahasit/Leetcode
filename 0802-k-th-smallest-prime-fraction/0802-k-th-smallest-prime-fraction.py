class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                res.append((arr[i]/ arr[j], arr[i], arr[j]))
        heapq.heapify(res)
        while k > 0: 
            val, i, j = heapq.heappop(res)
            k -= 1

        return [i, j]

        
        