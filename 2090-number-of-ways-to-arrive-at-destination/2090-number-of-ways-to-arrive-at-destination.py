class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = (10**9) + 7
        adj_list = defaultdict(list)
        for edge in roads:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        result = defaultdict(int)
        visit = set()
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0))
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        while heap:
            time, node = heapq.heappop(heap)
            # as its a heaps its processes in order if we get 3 then after 5 no no as 3 is minimum
            if time > dist[node]: 
                continue
            for nei, t in adj_list[node]:
                if t + time < dist[nei]:
                    dist[nei] = t + time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (dist[nei], nei))
                elif t + time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        print(ways)
        print(dist)

        return ways[n - 1] % MOD

                