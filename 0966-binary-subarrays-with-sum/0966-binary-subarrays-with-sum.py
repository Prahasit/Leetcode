class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #if sum - k in hashmap then we are sure there is a subarray with sum k 
        cumulative_sum = defaultdict(int) # sum, no of occurences of corresponding sum
        tot_sum, count = 0, 0
        cumulative_sum[0] = 1

        for num in nums:
            tot_sum += num
            if tot_sum - goal in cumulative_sum:
                count += cumulative_sum[tot_sum - goal]
            cumulative_sum[tot_sum] += 1
        return count