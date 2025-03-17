class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        heapq.heapify(closest_points)
        for x, y in points:
            heapq.heappush(closest_points,((x**2 + y**2), x, y))
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(closest_points)
            res.append([x, y])
            k -= 1
        return res
        