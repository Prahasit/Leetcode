class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = Counter(nums)
        max_rows = max(freq.values())
        
        for _ in range(max_rows):
            temp = []
            for i in list(freq.keys()):
                temp.append(i)
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
            res.append(temp)
        return res
            
