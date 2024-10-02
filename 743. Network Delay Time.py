import sys
class Solution:
    def networkDelayTime(self, times, n, k):
        dp = [sys.maxsize] * n
        dp[k - 1] = 0

        for _ in range(n - 1):
            for s, e, w in times:
                if dp[e - 1] > dp[s - 1] + w:
                    dp[e - 1] = dp[s - 1] + w

        ans = 0
        for i in range(n):
            if i != k - 1:
                ans = max(ans, dp[i])
        return ans if ans != sys.maxsize else -1

ans = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(ans.networkDelayTime(times,n,k))