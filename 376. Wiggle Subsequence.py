class Solution:
    def wiggleMaxLength(self, nums):

        L = len(nums)
        dp = [(0, None)] * L
        for i in range(1, L):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff != 0 and ((diff > 0) != dp[j][1]):
                    if 1 + dp[j][0] > dp[i][0]:
                        dp[i] = (1 + dp[j][0], diff > 0)
        return max(dp, key=lambda x: x[0])[0] + 1

ans = Solution()
nums = [1,17,5,10,13,15,10,5,16,8]
print(ans.wiggleMaxLength(nums))