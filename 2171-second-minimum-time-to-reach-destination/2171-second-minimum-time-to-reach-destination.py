class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        dist1 = [float('inf')] * (n + 1)
        dist2 = [float('inf')] * (n + 1)
        freq = [0] * (n + 1)
        heap = []
        heapq.heappush(heap,(0, 1)) #time, node

        dist1[1] = 0

        while heap:
            time_taken, node = heapq.heappop(heap)
            freq[node] += 1

            if freq[node] == 2 and node == n:
                return time_taken

            # as week to skip the 2nd time as first time we take and on second change we need to skip
            if (time_taken // change)  % 2 == 1:
                time_taken = change * (time_taken// change + 1) + time
            else:
                time_taken = time_taken + time

            
            for nei in adj_list[node]:
                if freq[nei] == 2: # we can skip more than 2 occurances
                    continue

                # assigning distance to dist1 and infinity to dist 2
                if time_taken < dist1[nei]:
                    dist2[nei] = dist1[nei]
                    dist1[nei] = time_taken
                    heapq.heappush(heap, (time_taken, nei))

                elif time_taken < dist2[nei] and dist1[nei] != time_taken:
                    dist2[nei] = time_taken
                    heapq.heappush(heap, (time_taken, nei))

        return dist2[n]