class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        m, n = len(mat),len(mat[0])
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            
            heapq.heappush(pq,(count, i))
        
        res = []
        while k > 0:
            count, idx = heapq.heappop(pq)
            res.append(idx)
            k -= 1

        return res


