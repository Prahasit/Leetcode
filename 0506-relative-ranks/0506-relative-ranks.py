class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        pq = [(-score, idx) for idx, score in enumerate(score)]
        place = 1
        heapq.heapify(pq)
        rank = [0] * n
        while pq:
            scores, idx = heapq.heappop(pq)
            if place == 1:
                rank[idx] = "Gold Medal"
            elif place == 2:
                rank[idx] = "Silver Medal"
            elif place == 3:
                rank[idx] = "Bronze Medal"
            else:
                rank[idx] = str(place)

            
            
            place += 1

        return rank
                