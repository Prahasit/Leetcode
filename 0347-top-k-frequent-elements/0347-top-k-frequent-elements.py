class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        heap = [(-val, key) for key,val in freq.items()]
        heapq.heapify(heap)
        while k > 0:
            val, key = heapq.heappop(heap)
            result.append(key)
            k -= 1
        
        return result

        