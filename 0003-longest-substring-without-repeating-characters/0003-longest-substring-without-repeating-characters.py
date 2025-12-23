class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {}
        l, r = 0, 0
        maxlen = 0
        n = len(s)

        while r < n:
            while s[r] in mapping:
                mapping[s[l]] -= 1
                if mapping[s[l]] == 0:
                    del mapping[s[l]]
                l += 1

            if s[r] not in mapping:
                mapping[s[r]] = 1
                maxlen = max(maxlen, r - l + 1)
            
            r += 1
            

        return maxlen

