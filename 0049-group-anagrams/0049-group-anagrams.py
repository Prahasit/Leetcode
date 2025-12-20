class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            chars = list(s)
            chars.sort()
            key = ''.join(chars)

            res[key].append(s)
    
        return list(res.values())