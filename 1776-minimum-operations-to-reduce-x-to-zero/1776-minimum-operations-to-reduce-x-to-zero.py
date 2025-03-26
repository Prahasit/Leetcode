class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # add 1 + 1 =2 + 4 = 6 its > 5 so --> remove 5 and subtract from end 3 
        #i.e 2 + 3 = 5 save the answer also process to get the minimum no of operatiosn .
        # similar to #LC 1423

        n = len(nums)
        min_len = float('inf')
        l, r = 0, n - 1
        cur_sum = 0

        while cur_sum < x and l < n:
            cur_sum += nums[l]
            l += 1

        if cur_sum == x:
            min_len = min(min_len , l)
        if cur_sum < x:
            return -1
        
        cur_sum = cur_sum - nums[l- 1]
        l = l - 2

        # keep l the same go to right and if it is > x reduxe l
        while l <= r and l >= 0 and r >= 0:
            
            
            cur_sum += nums[r]
            print(cur_sum)
            while cur_sum > x:
                cur_sum -= nums[l]
                l = l - 1
            
            if cur_sum == x:
                min_len = min(min_len , l + 1 + n - r)
            print(min_len)
            r -= 1
# for edge case [10,1,1,1,1,1] as  nums[0] > x,  we do l =l-2 --> l = -1 
        while l < 0 and cur_sum  < x and r >= 0:
            cur_sum += nums[r]
            r -= 1

        if cur_sum == x:
            min_len = min(min_len, n - r - 1)
        return min_len if min_len != float('inf') else -1



       

            
