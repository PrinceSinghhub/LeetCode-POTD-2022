class Solution:
    def missingNumber(self, nums):

        n = len(nums)

        for i in range(0, n + 1):

            if i in nums:
                continue
            else:
                return i

ans = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(ans.missingNumber(nums))

