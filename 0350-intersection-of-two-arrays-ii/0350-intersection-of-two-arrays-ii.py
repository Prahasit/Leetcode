class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= [ ]
        freq1 = Counter(nums1)
        
        for i in nums2:
            if i in freq1 and freq1[i] > 0:
                res.append(i)
                freq1[i] -= 1

        return res