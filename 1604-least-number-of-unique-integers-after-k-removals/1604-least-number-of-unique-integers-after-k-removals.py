class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        #least no of unique integers means first remove the least frequency elements so there will be less frequent elemts
        freq = Counter(arr)
        pq = [(count, num) for num, count in freq.items()]
        heapq.heapify(pq)

        while k > 0:
            count, num = heapq.heappop(pq)
            count = count - 1
            if count > 0:
                heapq.heappush(pq, (count, num))
            k-= 1

        return len(pq)