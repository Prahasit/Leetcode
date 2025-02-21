class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = [(-maxval, idx) for idx, maxval in enumerate(gifts)]
        heapq.heapify(pq)
        while k  > 0:
            max_val, idx = heapq.heappop(pq)
            gifts[idx] = math.isqrt(-max_val) #isqrt() is used for floor of square root        
            heapq.heappush(pq, (-gifts[idx], idx))
            k -= 1

        return sum(gifts)