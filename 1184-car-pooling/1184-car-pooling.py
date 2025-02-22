class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        trips.sort(key = lambda x: x[1])

        for cap, start, end in trips:
            while heap and heap[0][0] <= start: #if end time of top of heap is less than the start time of new value
                capacity += heap[0][1]
                heapq.heappop(heap)

            if cap > capacity:
                return False

            else:
                capacity -= cap
                heapq.heappush(heap, (end, cap)) #end time, capacity

        return True