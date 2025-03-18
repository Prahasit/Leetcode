class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        #we need to do reverse xor where a ^b = c theb b = a^c
        n = len(pref)
        arr = []
        arr.append(pref[0])
        for i in range(1, n):
            arr.append(pref[i-1] ^pref[i])
        return arr
