class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # we need to insert the lowest pair
        res = []
        m, n = len(nums1), len(nums2)
        visit = set()

        heap = [(nums1[0] + nums2[0], (0, 0))] #inserting first element as its non decreasing 

        while k > 0 and heap:
            val, (i, j) = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visit:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visit.add((i + 1, j))

            if j + 1 < n and (i, j  + 1) not in visit:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visit.add((i, j + 1))
            
            k -= 1
        
        return res

        