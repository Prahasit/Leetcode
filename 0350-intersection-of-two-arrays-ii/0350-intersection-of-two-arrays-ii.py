class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # nums1 is shorter

        freq = Counter(nums1)
        res = []

        for x in nums2:
            if freq.get(x, 0) > 0:
                res.append(x)
                freq[x] -= 1
                if freq[x] == 0:
                    del freq[x]   # optional

        return res