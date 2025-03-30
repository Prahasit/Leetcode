class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for edge in flights:
            adj_list[edge[0]].append((edge[1], edge[2]))

        dist = [float('inf')] * n
        heap = []
        heapq.heappush(heap, (0, 0, src)) # k, distance, src
        dist[src] = 0

        while heap:
            stops, distance, node = heapq.heappop(heap)

            for nei, w in adj_list[node]:
                if distance + w < dist[nei] and stops <= k:
                    dist[nei] = distance + w
                    heapq.heappush(heap, (stops + 1, dist[nei], nei))

                
        return dist[dst] if dist[dst] != float('inf') else -1
            