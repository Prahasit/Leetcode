class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        window = len(s1)
        for i in range(window):
            freq1[s1[i]] += 1
            freq2[s2[i]] += 1

        if freq1 == freq2:
            return True

        for i in range(window, len(s2)):
            freq2[s2[i]] += 1
            freq2[s2[i - window]] -= 1

            if freq2[s2[i - window]] == 0:
                del freq2[s2[i - window]]
            
            if freq1 == freq2:
                return True
        return False