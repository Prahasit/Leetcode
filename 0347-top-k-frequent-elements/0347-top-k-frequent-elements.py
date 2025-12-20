class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)

        res = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        return [num for num, freq in res[:k]]








