class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1

        freq_pairs = sorted(freq.items(), key = lambda x: x[1], reverse =True)

        for char, count in freq_pairs:
            result.append(char * count)

        return ''.join(result)


        
        
    
        