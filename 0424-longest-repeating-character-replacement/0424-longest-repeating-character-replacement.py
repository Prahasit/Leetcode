class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        l, r = 0, 0
        maxlen = 0
        while r < n:
            freq[s[r]] += 1
            
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r - l + 1)

            r += 1
        
        return maxlen
