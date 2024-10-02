from heapq import heappush, heappop


class Solution(object):
    def maxResult(self, A, k):
        pq = [(0, -k)]
        for i, a in enumerate(A):
            while i - pq[0][1] > k:
                heappop(pq)
            a -= pq[0][0]
            heappush(pq, (-a, i))
        return a


ans = Solution()
nums = [1,-1,-2,4,-7,3]
k = 2
print(ans.maxResult(nums,k))