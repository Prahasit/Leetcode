class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        
        courses.sort(key = lambda x: x[1])
        heap = []
        total = 0
        for duration, end in courses:
            heapq.heappush(heap, -duration)
            total += duration

            if total > end:
                total += heapq.heappop(heap)
        
        return len(heap)
