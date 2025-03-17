

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        heap = [1]
        heapq.heapify(heap)
        res = []
        res_set = set()
        while len(res) < n:
            num = heapq.heappop(heap)
            if num not in res_set:
                res_set.add(num)
                res.append(num)
            
            if num * 2 not in res_set:
                heapq.heappush(heap, num * 2)
            if num * 2 not in res_set:
                heapq.heappush(heap, num * 3)
            if num * 2 not in res_set:
                heapq.heappush(heap, num * 5) 
            
        
        return max(res)

        