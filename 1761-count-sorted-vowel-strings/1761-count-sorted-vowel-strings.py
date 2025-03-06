class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        memo = {}

        # Helper function with memoization
        def solve(i, prev_vowel):
            # If we have computed this subproblem before, return the cached result
            if (i, prev_vowel) in memo:
                return memo[(i, prev_vowel)]
            
            # Base case: If the string length is equal to n, return 1 (valid string)
            if i == n:
                return 1
            
            count = 0
            # Recur for the next vowel, ensuring lexicographical order
            for j in range(prev_vowel, 5):
                count += solve(i + 1, j)
            
            # Store the result in the memoization table
            memo[(i, prev_vowel)] = count
            return count
        
        # Start the recursion with length 0 and the first vowel index 0 (can start with any vowel)
        return solve(0, 0)