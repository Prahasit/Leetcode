class Solution:
    def frequencySort(self, s: str) -> str:
        #using max_heap
        freq = Counter(s)
        pq = [(-f, char) for char, f in freq.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            f, char = heapq.heappop(pq)
            result += char * -f
        return result