class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #if "abcabc" if we are at index 2 i.e 'c' "abc" are taken, even we move forward, condition of three characters will also satisfy so we need just add length of n - r

        n = len(s)
        l, r = 0,0
        result = 0
        freq = defaultdict(int)
        while r < n:
            freq[s[r]] += 1
            while len(freq) == 3:
                result += n - r
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            r += 1

        return result