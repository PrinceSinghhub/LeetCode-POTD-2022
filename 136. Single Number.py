class Solution:
    def singleNumber(self, nums):

        for i in nums:
            element = nums.count(i)
            if element == 2:
                pass
            else:
                return i

ans = Solution()
nums = [2,2,1]
print(ans.singleNumber(nums))