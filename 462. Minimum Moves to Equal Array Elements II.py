class Solution:
    def minMoves2(self, nums):
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            ans += abs(nums[i] - nums[len(nums) // 2])

        return ans

ans = Solution()
nums = [1,2,3]
print(ans.minMoves2(nums))