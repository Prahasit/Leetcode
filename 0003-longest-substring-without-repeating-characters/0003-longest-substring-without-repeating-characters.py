class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        chars = defaultdict(int)
        l, r = 0 , 0
        while r < n:
            print(maxlen)
            while s[r] in chars:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            else:
                chars[s[r]] = 1
                maxlen = max(maxlen, r - l + 1)
            
            r += 1
        
        return maxlen


            
            
