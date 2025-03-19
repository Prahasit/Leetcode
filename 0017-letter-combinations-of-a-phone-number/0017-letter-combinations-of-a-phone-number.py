class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        combinations = { 2: 'abc', 3: 'def', 4: 'ghi', 5 :'jkl', 6:'mno',7:'pqrs', 8:'tuv', 9:'wxyz'}
        result = []
        if len(digits) == 0:
            return []
        def dfs(idx, sub_Str):
            if idx == n:
                result.append(sub_Str)
                return

            for s in combinations[int(digits[idx])]:
                dfs(idx + 1, sub_Str + s)


        dfs(0, "")
        return result