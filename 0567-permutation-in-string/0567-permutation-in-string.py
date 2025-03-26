class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s2)
        freq_s1 = Counter(s1)
        window = len(s1)
        freq_s2 = defaultdict(int)
        for i in range(window):
            freq_s2[s2[i]] += 1
        
        if freq_s1 == freq_s2:
            return True

        for i in range(window, n):
            freq_s2[s2[i]] += 1
            freq_s2[s2[i - window]] -= 1

            if freq_s2[s2[i - window]] == 0:
                del freq_s2[s2[i - window]]
            
            if freq_s1 == freq_s2:
                return True
        return False


