class Solution:
    def numberOfArithmeticSlices(self, A):
        le = len(A)
        dp=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i]=1+dp[i-1]
        return sum(dp)


ans = Solution()
nums = [1,2,3,4]
print(ans.numberOfArithmeticSlices(nums))