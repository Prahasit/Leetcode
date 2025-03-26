class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #first try to find the string "t"  which occurs in the substring "s".
        # then try to shrink the window by increasing l = l + 1
        # for every window find the minimum window which contains "t"
        if len(t) > len(s):
            return ""
        n = len(s)
        l, r = 0, 0
        freq_t = Counter(t)
        count_t = len(freq_t)
        minlen = float('inf')
        result = ""
        while r < n:
            if s[r] in freq_t:
                freq_t[s[r]] -= 1
                if freq_t[s[r]] == 0:
                    count_t -= 1
            
            while count_t == 0: # i. e all chars in t are found in s
                if r - l + 1 < minlen:
                        minlen = r - l + 1
                        result = s[l:r + 1]
                if s[l] in freq_t: # shrinking 
                    freq_t[s[l]] += 1
                    if freq_t[s[l]] > 0:
                        count_t += 1
                        
                l += 1

            r += 1
                    
        
        return result



