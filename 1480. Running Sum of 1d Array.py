class Solution:
    def runningSum(self, nums):
        num = []

        for i in range(len(nums)):
            num.append(sum(nums[0:i + 1]))

        return num

ans = Solution()
nums = [1,2,3,4]
print(ans.runningSum(nums))