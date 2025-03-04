class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #it is similar to MST after finding the manhattan distance
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n): # need to check from i + 1 as till i all adges are appended already
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        total_dist = 0
        visit = set()
        min_heap = [(0, 0)] # distance, index
        while len(visit) < n:
            dist, curr = heapq.heappop(min_heap)

            if curr in visit:
                continue
            
            visit.add(curr)
            total_dist += dist

            for cost, nei in adj[curr]:
                if nei not in visit:
                    heapq.heappush(min_heap, (cost, nei))
            
        return total_dist
