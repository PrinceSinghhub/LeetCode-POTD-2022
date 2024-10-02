class Solution:
    def checkPossibility(self, nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]<0:
                count += 1
            if (i>1 and nums[i]-nums[i-2]<0 and nums[i+1]-nums[i-1]<0) or count>1:
                return False
        return True

ans = Solution()
nums = [4,2,3]
print(ans.checkPossibility(nums))