class Solution:

    def TabulatonMethode(self,n):



        dp = [0]*(n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        print(dp)
        return dp


    def climbStairs(self, n):

        ans = self.TabulatonMethode(n)
        return ans[-1]