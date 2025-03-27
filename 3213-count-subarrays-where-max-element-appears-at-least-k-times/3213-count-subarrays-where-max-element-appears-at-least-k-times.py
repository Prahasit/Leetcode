class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #Brute force
        n = len(nums)
        result = 0
        max_val = max(nums)
        l, r = 0, 0
        count = 0
        while r < n:
            if nums[r] == max_val:
                count += 1
            
            while count == k:
                if nums[l] == max_val:
                    count -= 1
                l += 1
# as example 1,3,2,3,3 supoose l = 3, r = 4 ,no fo subarrys can be [1,3,2,3,3],[3,2,3,3], [2,3,3], [3,3]
# which means the we need ad l times because at l there are atleast k times so before l index all indexes will also become possible subarrys so need to add l not 1
            result += l 
            r += 1

        return result