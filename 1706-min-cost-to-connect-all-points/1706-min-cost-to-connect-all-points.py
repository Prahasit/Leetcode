class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #it is similar to MST after finding the manhattan distance
        n = len(points)
        total_dist = 0
        visit = set()
        min_heap = [(0, 0)] # distance, index
        while len(visit) < n:
            dist, curr = heapq.heappop(min_heap)

            if curr in visit:
                continue
            
            visit.add(curr)
            total_dist += dist

            for nei in range(n):
                if nei not in visit:
                    x1, y1 = points[curr]
                    x2, y2 = points[nei]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (distance, nei))
            
        return total_dist
