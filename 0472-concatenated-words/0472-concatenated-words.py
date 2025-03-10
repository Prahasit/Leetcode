class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def solve(word):
            if word in memo:
                return memo[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i :]

                if (prefix in words_set and suffix in words_set) or (prefix in words_set and solve(suffix)):
                    memo[word] =True
                    return memo[word]

            memo[word] = False
            return memo[word]


        words_set = set(words)
        res = []
        memo = {}
        for w in words:
            if solve(w):
                res.append(w)

        return res