class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        #max 2 are taken first
        score = 0
        pq = []
        pq.append(-a)
        pq.append(-b)
        pq.append(-c)
        heapq.heapify(pq)

        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if -x - 1 != 0:
                heapq.heappush(pq, x + 1)
            if -y - 1 != 0:
                heapq.heappush(pq, y + 1)
            
            score += 1
        return score


