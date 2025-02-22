class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        freq = Counter(words)
        pq = [(-count,word) for word, count in freq.items()]
        heapq.heapify(pq)
        res = []

        while k > 0:
            count, word = heapq.heappop(pq)
            res.append(word)
            k -= 1
        return res
