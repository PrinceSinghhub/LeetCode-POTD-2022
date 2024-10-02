class Solution:
    def deleteAndEarn(self, nums):
        lookup = [0] * (max(nums) + 1)
        for num in nums:
            lookup[num] += 1

        n = len(lookup)
        dp = [0] * n
        dp[0] = lookup[0]
        dp[1] = max(lookup[0], lookup[1])
        for i in range(2, n):
            dp[i] = max(i*lookup[i] + dp[i-2], dp[i-1])
        return dp[-1]

ans = Solution()

nums = [3,4,2]
print(ans.deleteAndEarn(nums))