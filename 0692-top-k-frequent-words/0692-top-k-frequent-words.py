class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        freq = Counter(words)
        #to sort in descending order based on frequency and if equal sort in ascending order based on key
        sorted_order = sorted(freq.items(), key = lambda x : (-x[1], x[0]))
        for key, val in sorted_order[:k]: #extracting only k elements
            res.append(key)
        return res