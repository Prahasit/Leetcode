class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)

        if freq_s == freq_t:
            return True
        else:
            return False