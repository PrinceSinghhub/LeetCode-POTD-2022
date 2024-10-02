class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #rows = zeros
        #columns = unos
        for s in strs:
            z = s.count('0')
            o = len(s)-z
            for i in range(m, z-1, -1):
                for j in range(n, o-1 , -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-z][j-o])
        return dp[m][n]