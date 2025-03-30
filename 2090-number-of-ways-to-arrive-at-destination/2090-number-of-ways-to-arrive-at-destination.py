class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for edge in roads:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1

        heap = []
        heapq.heappush(heap, (0 ,0)) # time, node

        while heap:
            time, node = heapq.heappop(heap)

            for nei, t in adj_list[node]:
                if time + t < dist[nei]:
                    dist[nei] = time + t
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (dist[nei], nei))

                elif time + t == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % (10**9 + 7)

        return ways[n - 1] % (10**9 + 7)
        
