class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 'aeiou'
        max_vowels = 0 
        count = 0
        r = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
            r += 1
        max_vowels = max(max_vowels, count)
        print(max_vowels)
        
        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
           
            print(max_vowels)
            max_vowels = max(max_vowels, count)

        return max_vowels
                