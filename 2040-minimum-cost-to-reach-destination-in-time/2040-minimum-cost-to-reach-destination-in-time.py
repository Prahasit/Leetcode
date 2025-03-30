class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        times = [float('inf')] * n
        times[0] = 0
        heap = []
        heapq.heappush(heap, (passingFees[0], times[0], 0)) # fees, distance, node
        min_cost = float('inf')


        while heap:
            passfee, time, node = heapq.heappop(heap)

            if node == n - 1:
                if time <= maxTime:
                    min_cost = min(min_cost, passfee)
                    print(min_cost)


            for nei, t in adj_list[node]:
                if time + t < times[nei]:
                    times[nei] = time + t
                    heapq.heappush(heap, (passfee + passingFees[nei], times[nei],nei))
        # while heap:
        #     time, passfee, node = heapq.heappop(heap)

        #     if node == n - 1:
        #         if time <= maxTime:
        #             min_cost = min(min_cost, passfee)
        #             print(min_cost)


        #     for nei, t in adj_list[node]:
        #         if time + t < times[nei]:
        #             times[nei] = time + t
        #             heapq.heappush(heap, (times[nei], passfee + passingFees[nei], nei))


        return min_cost if min_cost != float('inf') else - 1