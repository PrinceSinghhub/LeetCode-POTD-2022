class Solution:
    def countElements(self, nums):
        Min = min(nums)
        Max = max(nums)

        ans = [1 for i in nums if Min < i < Max]
        return sum(ans)


ans = Solution()
nums = [11,7,2,15]
print(ans.countElements(nums))