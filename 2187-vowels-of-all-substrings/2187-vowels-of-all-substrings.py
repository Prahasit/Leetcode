class Solution:
    def countVowels(self, word: str) -> int:
        VOWEL_SET = {'a', 'e', 'i', 'o', 'u'}
        N = len(word)
        memo = {}

        def solve(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]

            if word[i-1] in VOWEL_SET:
                memo[i] = solve(i-1) + i
            else:
                memo[i] = solve(i-1)

            return memo[i]

        return sum(solve(i) for i in range(1, N + 1))
