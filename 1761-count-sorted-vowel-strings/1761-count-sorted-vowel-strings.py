class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [ 'a', 'e', 'i', 'o','u']
        count = 0
        def solve(sub_str, idx):
            nonlocal count
            if len(sub_str) == n:
                count += 1
                return 

            for i in range(idx, len(vowels)):
                solve(sub_str + vowels[i], i)
                    
        solve("", 0)
        return count
            


    