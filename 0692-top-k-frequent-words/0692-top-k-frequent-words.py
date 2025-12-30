class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)

        pq = [(-val, key) for key, val in freq.items()]
        heapq.heapify(pq)
        res =[]

        while k > 0:
            count, word = heapq.heappop(pq)
            res.append(word)
            k -= 1

        return res