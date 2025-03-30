class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for edge in times:
            adj_list[edge[0]].append((edge[1], edge[2]))
            
        print(adj_list)
        dist = [float('inf')] * (n + 1)
        heap = []
        heapq.heappush(heap, (0, k)) #dist, node
        dist[k] = 0

        while heap:
            distance, node = heapq.heappop(heap)

            for nei, w in adj_list[node]:
                if distance + w < dist[nei]:
                    dist[nei] = distance + w
                    heapq.heappush(heap, (dist[nei], nei))

        time = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return  - 1
            else:
                time = max(time , dist[i])
        
        return time