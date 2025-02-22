class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for row in matrix:
            for num in row:
                heapq.heappush(pq, -num)
                if len(pq) > k:
                    heapq.heappop(pq)
        

        return -heapq.heappop(pq)
            

        