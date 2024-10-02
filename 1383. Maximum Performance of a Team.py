import heapq


class Solution:
    def maxPerformance(self, n, speed, efficiency, k):

        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])

        result, sum_speed = 0, 0
        min_heap = []

        for i, (s, e) in enumerate(people):
            if i < k:
                sum_speed += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_speed += s - heapq.heappushpop(min_heap, s)
            else:
                continue  # don't have to update result since top k speeds are not changed and efficiency goes down

            result = max(result, sum_speed * e)

        return result % 1000000007
        # return 60