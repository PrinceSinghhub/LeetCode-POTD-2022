import heapq
class Solution:
    def scheduleCourse(self, courses):
        time  = 0
        heap = []
        for c in sorted(courses,key = lambda x:x[1]):
            if c[0]<=c[1]:
                if c[0]+time<=c[1]:
                    heapq.heappush(heap,-c[0])
                    time+=c[0]
                else:
                    if -heap[0]>c[0]:
                        time+=heapq.heappop(heap)
                        time+=c[0]
                        heapq.heappush(heap,-c[0])
        return len(heap)

ans = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(ans.scheduleCourse(courses))