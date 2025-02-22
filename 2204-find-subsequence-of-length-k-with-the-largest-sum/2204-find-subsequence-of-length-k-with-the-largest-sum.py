class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # to optimize the Tc, need to use heaps 
        #we need to sort the array while maintaining the index
        order = {} #index, value
        pq = [(-val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(pq)

        while k > 0:
            val, idx = heapq.heappop(pq)
            order[idx] = -val
            k -= 1
        
        res = []
        
        for key in sorted(order.keys()):
            res.append(order[key])
        
        return res