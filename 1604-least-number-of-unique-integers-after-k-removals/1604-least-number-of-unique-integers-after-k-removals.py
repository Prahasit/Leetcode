class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        pq = [(count, num) for num, count in freq.items()]
        heapq.heapify(pq)  # Min-heap based on frequency

        while k > 0 and pq:
            count, num = heapq.heappop(pq)
            k -= count  # Remove `count` occurrences from k
            if k < 0:  
                return len(pq) + 1  # If `k` over-deletes, count the current element

        return len(pq)